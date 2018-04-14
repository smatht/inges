# -*- coding: utf-8 -*-
from datetime import date, timedelta

from daterange_filter.filter import DateRangeFilter
from django.conf.urls import url
from django.contrib import admin, messages
from django.core.exceptions import ObjectDoesNotExist

from mantenimiento.models import TiposDoc, Impuesto, Configuracion

from fondos.models import Caja, MovCaja, TipoCaja, TipoMovCaja

from fondos.models import OrdenPago
from models import PedidoItem, Pedido, Remito, RemitoItem, PedidoItemConcepto, Compra, CompraItem, CompraItemConcepto
from functools32 import update_wrapper
from mantenimiento.models import ExtendUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from actions import export_OR_as_pdf, save_then_pdf
from forms import PedidoItemForm, PedidoForm, RemitoForm, CompraForm
from stock.models import Producto
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django_extensions.admin import ForeignKeyAutocompleteAdmin, ForeignKeyAutocompleteTabularInline


class UserInline(admin.StackedInline):
  model = ExtendUser
  can_delete = False
  verbose_name_plural = 'usuarios'


class UserAdmin(BaseUserAdmin):
  inlines = (UserInline,)

class PedidoItemInline(ForeignKeyAutocompleteTabularInline):
  form = PedidoItemForm
  model = PedidoItem
  related_search_fields = {
    'producto': ('descripcion',),
  }
  # fields = ('producto', 'cantidad', 'unidades')
  extra = 10


class PedidoItemConceptoInline(ForeignKeyAutocompleteTabularInline):
  form = PedidoItemForm
  model = PedidoItemConcepto
  extra = 0
  fieldsets = [
    (None, {
      'fields': ['sDescripcion', 'sCantidad', 'unidades'],
      'description': "Use linea de concepto cuando quiera agregar un producto no recurrente o alguna compra especial"}),
  ]


@admin.register(Pedido)
class PedidoAdmin(ForeignKeyAutocompleteAdmin):
  form = PedidoForm
  list_display = ('id', 'fechaPedido', 'registro', 'proveedor', 'destino', 'recepcion', 'account_actions')
  list_filter = ('proveedor__nombre_fantasia', 'destino__descripcion_corta', 'fechaPedido')
  search_fields = ('pedido__producto__descripcion',)
  exclude = ('remitente', 'usuario', 'anulado', 'fechaCarga')
  inlines = [PedidoItemInline, PedidoItemConceptoInline]
  actions = [export_OR_as_pdf]
  fieldsets = [
    (None, {'fields': ['registro', 'fechaPedido', 'proveedor','destino', 'bGeneraRemito']}),
    ('Orden de retiro', {
      'description': 'Para extender una orden de retiro complete este campo',
      'fields': ['se_autoriza', 'firmante']}),
    ]

  def wrap(self, view):
    def wrapper(*args, **kwargs):
      return self.admin_site.admin_view(view)(*args, **kwargs)
    wrapper.model_admin = self
    return update_wrapper(wrapper, view)

  def detalles(self, obj):
    dets = PedidoItem.objects.filter(pedido=obj)
    return dets

  def recepcion(self, obj):
    rem = Remito.objects.filter(pedido=obj)
    ped_det = PedidoItem.objects.filter(pedido=obj)
    cant_ped_det = 0
    cant_rem_det = 0

    rem_det_is_false = RemitoItem.objects.filter(remito=rem, bConfirmacion=False)
    for d in ped_det:
      cant_ped_det += float(d.sCantidad)
    for r in rem:
      for d in RemitoItem.objects.filter(remito=r):
        cant_rem_det += float(d.sCantidad)

    if (rem):
      if ((cant_ped_det != cant_rem_det) | (len(rem_det_is_false) >= 1)):
        return '<img src="/static/admin/img/icon-casi-yes.gif" alt="True">'
      else:
        return '<img src="/static/admin/img/icon-yes.gif" alt="True">'
    else:
      return '<img src="/static/admin/img/icon-casi-no.gif" alt="False">'
  recepcion.allow_tags = True

  def save_model(self, request, obj, form, change):
    if getattr(obj, 'remitente', None) is None:
      obj.remitente = request.user
    if getattr(obj, 'firmante', None) is None:
      obj.firmante = request.user
    if getattr(obj, 'usuario', None) is None:
      obj.usuario = request.user
    obj.save()
    # save_then_pdf(request, obj)

  def render_change_form(self, request, context, *args, **kwargs):
    context['adminform'].form.fields['firmante'].queryset = User.objects.filter(extenduser__habilitarPedido=True)
    context['adminform'].form.fields['firmante'].initial = request.user
    return super(PedidoAdmin, self).render_change_form(request, context, args, kwargs)

  def process_print(self, request, pedido_id, *args, **kwargs):
    qs = Pedido.objects.get(pk=pedido_id)
    return export_OR_as_pdf(self, request, qs)

  def process_remito(self, request, pedido_id, *args, **kwargs):
    pedido = Pedido.objects.get(pk=pedido_id)
    rem = Remito(pedido=pedido, registro=pedido.registro, proveedor=pedido.proveedor, destino=pedido.destino)
    rem.save()
    for qs in PedidoItem.objects.filter(pedido=pedido_id).order_by('pk'):
      det = RemitoItem(remito=rem, producto=qs.producto, sCantidad=qs.sCantidad, unidades=qs.unidades)
      det.save()
    return HttpResponseRedirect("../../../remito/%s?_popup=1" % rem.id)

  def get_urls(self):
    urls = super(PedidoAdmin, self).get_urls()
    custom_urls = [
      url(
        r'^(?P<pedido_id>.+)/deposit/$',
        self.admin_site.admin_view(self.process_print),
        name='process-print',
      ),
      url(
        r'^(?P<pedido_id>.+)/remito/$',
        self.admin_site.admin_view(self.process_remito),
        name='process-remito',
      ),
    ]
    return custom_urls + urls


class RemitoItemInline(ForeignKeyAutocompleteTabularInline):
  form = PedidoItemForm
  # template = 'admin/edit_inline/stacked.html'
  model = RemitoItem
  extra = 10
  related_search_fields = {
    'producto': ('descripcion',),
  }
  # fields = ('producto',)

@admin.register(Remito)
class RemitoAdmin(ForeignKeyAutocompleteAdmin):
  ForeignKeyAutocompleteAdmin.model = Producto
  form = RemitoForm
  list_display = ('fechaRemito', 'proveedor', 'pedido_ID')
  inlines = [RemitoItemInline]
  list_filter = ('fechaRemito', 'proveedor__nombre_fantasia', 'pedido__id')
  search_fields = ('remitoitem__producto__descripcion',)
  exclude = ('factura', 'usuario', 'origen', 'afectaStock', 'fechaCarga')

  def save_model(self, request, obj, form, change):
    if getattr(obj, 'usuario', None) is None:
      obj.usuario = request.user
    obj.save()

  def pedido_ID(self, obj):
    if (obj.pedido):
      return '<a href="../%s/%d">%d</a>' % ('pedido', obj.pedido.id, obj.pedido.id)
    else:
      return '<img src="/static/admin/img/icon-casi-no.gif" alt="False">'
  pedido_ID.allow_tags = True

  def wrap(self, view):
    def wrapper(*args, **kwargs):
      return self.admin_site.admin_view(view)(*args, **kwargs)
    wrapper.model_admin = self
    return update_wrapper(wrapper, view)

  def get_urls(self):
    urlpatterns = super(RemitoAdmin, self).get_urls()
    return urlpatterns


class CompraItemInline(ForeignKeyAutocompleteTabularInline):
  model = CompraItem
  related_search_fields = {
    'producto': ('descripcion',),
  }
  extra = 10
  fieldsets = [
      (None, {
          'fields': ['producto', 'cantidad', 'alicuota', 'precio_unitario'],
          'description': "Use linea de concepto cuando quiera agregar un producto no recurrente o alguna compra especial"}),
  ]


class CompraItemConceptoInline(ForeignKeyAutocompleteTabularInline):
  model = CompraItemConcepto
  extra = 0
  fieldsets = [
    (None, {
      'fields': ['descripcion', 'cantidad', 'alicuota', 'precio_unitario'],
      'description': "Use linea de concepto cuando quiera agregar un producto no recurrente o alguna compra especial"}),
  ]

@admin.register(Compra)
class CompraAdmin(ForeignKeyAutocompleteAdmin):
    form = CompraForm
    list_display = ('tipoDoc', 'proveedor', 'numero_doc', 'fRegistro', 'fDocumento', 'fVencimiento', 'totBruto', 'totImpuestos', 'totNeto')
    exclude = ('fRegistro', 'operador', 'anulado', 'fanulacion', 'totBruto', 'totImpuesto', 'totNeto',
               'yaAfectoStock', 'totDescuentos', 'idCaja')
    list_filter = ('fRegistro', ('fDocumento', DateRangeFilter), 'condPago')
    radio_fields = {"condPago": admin.VERTICAL}
    inlines = [CompraItemInline, CompraItemConceptoInline]
    fieldsets = [
        (None, {'fields': ['afectaEmpresa', 'obra', 'fContabilizar', 'fDocumento', 'proveedor',
                           'tipoDoc', ('sucursal', 'numDoc'), 'condPago']}),
        ('Fecha vencimiento:', {
            'classes': ('collapse',),
            'fields': ['fVencimiento']}),
        ('Caja:', {
            'classes': ('collapse',),
            'fields': ['afectaCaja', 'tipoCaja']}),
        (None, {'fields': [('afectaStock', 'prFinal', 'esCopia')]}),
        ('Cai:', {
          'classes': ('collapse',),
          'fields': ['cai', 'vCai']}),
        ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'operador', None) is None:
            obj.operador = request.user
            # messages.add_message(request, messages.INFO, 'Operador registrado')
        if form.cleaned_data['generarMov']:
            if form.cleaned_data['tipoCaja'] is not None:
                try:
                    cja = Caja.objects.get(tipoCaja=form.cleaned_data['tipoCaja'], destino=obj.obra, fCierre=None)
                except ObjectDoesNotExist:
                    cja = self.abrirCaja(obj.obra, form.cleaned_data['tipoCaja'])
            else:
                try:
                    cja = Caja.objects.get(tipoCaja=1, destino=obj.obra, fCierre=None)
                except ObjectDoesNotExist:
                    cja = self.abrirCaja(obj.obra)
            obj.idCaja = cja.pk
        print(obj.idCaja)
        obj.save()

    # Colorea LIST DISPLAY dependiendo si la factura esta pagada o no, vencida o por vencer
    def suit_row_attributes(self, obj, request):
        condPago = 'info'
        if obj.condPago == 'CRE':
            if obj.pk not in OrdenPago.facturas.through.objects.values_list('compra', flat=True):
                if (obj.fVencimiento < date.today()):
                    condPago = 'error'
                elif (obj.fVencimiento <= (date.today() + timedelta(days=3))):
                    condPago = 'warning'
                else:
                    condPago = 'success'
        #condPago = {'CTD': '', 'CRE': 'warning'}.get(obj.condPago)
        # copia = {1: 'error', 0: ''}.get(obj.esCopia)
        if condPago:
            return {'class': condPago}

    # Retorna numero de factura en formato estandar 0000-00000000
    def numero_doc(self, obj):
        return '%s-%s' % (str(obj.sucursal).zfill(4), str(obj.numDoc).zfill(8))

    # Setea valores iniciales de campos de form segun configuracion
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['tipoDoc'].queryset = TiposDoc.objects.filter(tipo=1)
        context['adminform'].form.fields['condPago'].initial = Configuracion.objects.get(pk=1).compras_condPago
        context['adminform'].form.fields['afectaEmpresa'].initial = Configuracion.objects.get(pk=1).empresa
        context['adminform'].form.fields['tipoDoc'].initial = Configuracion.objects.get(pk=1).compras_tipoDoc
        context['adminform'].form.fields['prFinal'].initial = Configuracion.objects.get(pk=1).compras_usaPrFinal
        context['adminform'].form.fields['afectaStock'].initial = Configuracion.objects.get(pk=1).compras_FacAfectaStk
        return super(CompraAdmin, self).render_change_form(request, context, args, kwargs)

    # Los siguientes 3 metodos sirven para Operar con cada FacturaItem
    def response_add(self, request, new_object, **kwargs):
        obj = self.after_saving_model_and_related_inlines(request, new_object)
        return super(CompraAdmin, self).response_add(request, obj)

    def response_change(self, request, obj):
        obj = self.after_saving_model_and_related_inlines(request, obj)
        return super(CompraAdmin, self).response_change(request, obj)

    def after_saving_model_and_related_inlines(self, request, cabecera):
        lineas = CompraItem.objects.filter(factura=cabecera.pk)
        conceptos = CompraItemConcepto.objects.filter(factura=cabecera.pk)

        cabecera.totBruto = 0
        cabecera.totNeto = 0
        cabecera.totImpuestos = 0
        # Obtenemos la ultima caja abierta para esa obra
        # Si recibe tipoCaja busca ese tipo de caja de la obra seleccionada, si no recibe, busca la "caja chica" de la
        # obra seleccionada. Si no existe
        if getattr(cabecera, 'idCaja', None) is None:
            caja = Caja.objects.get(pk=cabecera.idCaja)
        else:
            caja = False
        # Bucle CompraItem
        for linea in lineas:
            precioLinea = 0 # Usamos para movCaja
            # Completa datos de cabecera con valores de las lineas dependiendo si se usa precio final o bruto por item
            if cabecera.prFinal:
                totNeto = (linea.precio_unitario * linea.cantidad)
                totBruto = ((linea.precio_unitario/(1+(linea.alicuota.valorImpuesto/100))) * linea.cantidad)
                totImpuestos = ((linea.precio_unitario - (linea.precio_unitario/(1+(linea.alicuota.valorImpuesto/100)))) * linea.cantidad)
                cabecera.totNeto = cabecera.totNeto + totNeto
                cabecera.totBruto = cabecera.totBruto + totBruto
                cabecera.totImpuestos = cabecera.totImpuestos + totImpuestos
                precioLinea = totNeto
            else:
                totBruto = (linea.precio_unitario * linea.cantidad)
                precioLinea = (linea.precio_unitario * (1 + (linea.alicuota.valorImpuesto / 100))) * linea.cantidad
                totImpuestos = (precioLinea - totBruto)
                cabecera.totBruto = cabecera.totBruto + totBruto
                cabecera.totImpuestos = cabecera.totImpuestos + totImpuestos
                cabecera.totNeto = totBruto + totImpuestos

            # Si campo Obra de linea esta vacio completamos con la Obra seleccionada en cabecera sino se deja como esta
            if not linea.obra:
                linea.obra = cabecera.obra
                linea.save()

            # Hacemos el movimiento de caja.
            if caja:
                desc = cabecera.tipoDoc.id + " Nro:" + str(cabecera.numDoc) + " Prov: " + cabecera.proveedor.razon_social \
                       + " " + linea.producto.descripcionCorta + " " + str(linea.cantidad) + " Unid."
                mc = TipoMovCaja.objects.get(pk=3)
                m = MovCaja(caja=caja, empresa=cabecera.afectaEmpresa, tipoDoc=cabecera.tipoDoc, numDoc= cabecera.numDoc,
                            descripcion=desc, operador=request.user, importe=precioLinea, tipoMovCaja=mc)
                m.save()

            # Actualizamos el campo salida de Caja
            # if caja.acumSalidas >= 0:
            #     caja.acumSalidas += precioLinea
            # else:
            #     caja.acumSalidas = precioLinea
            # caja.save()

            # Actualizamos precio de compra
            if linea.producto.precio(cabecera.proveedor):
                if linea.producto.precio(cabecera.proveedor) != linea.precio_unitario:
                    linea.producto.nuevoPrecio(cabecera.proveedor, linea.precio_unitario)
            else:
                linea.producto.nuevoPrecio(cabecera.proveedor, linea.precio_unitario)

        # Bucle CompraItemConcepto
        for concepto in conceptos:
            precioConcepto = 0  # Usamos para movCaja
            # Completa datos de cabecera con valores de las conceptos dependiendo si se usa precio final o bruto por item
            if cabecera.prFinal:
                totNeto = (concepto.precio_unitario * concepto.cantidad)
                totBruto = ((concepto.precio_unitario / (
                            1 + (concepto.alicuota.valorImpuesto / 100))) * concepto.cantidad)
                totImpuestos = ((concepto.precio_unitario - (concepto.precio_unitario / (
                            1 + (concepto.alicuota.valorImpuesto / 100)))) * concepto.cantidad)
                cabecera.totNeto = cabecera.totNeto + totNeto
                cabecera.totBruto = cabecera.totBruto + totBruto
                cabecera.totImpuestos = cabecera.totImpuestos + totImpuestos
                precioConcepto = totNeto
            else:
                totBruto = (concepto.precio_unitario * concepto.cantidad)
                precioConcepto = (concepto.precio_unitario * (
                            1 + (concepto.alicuota.valorImpuesto / 100))) * concepto.cantidad
                totImpuestos = (precioConcepto - totBruto)
                cabecera.totBruto = cabecera.totBruto + totBruto
                cabecera.totImpuestos = cabecera.totImpuestos + totImpuestos
                cabecera.totNeto = totBruto + totImpuestos

            # Si campo Obra de concepto esta vacio completamos con la Obra seleccionada en cabecera sino se deja como esta
            if not concepto.obra:
                concepto.obra = cabecera.obra
                concepto.save()

            # Hacemos el movimiento de caja.
            if cabecera.generarMov:
                desc = cabecera.tipoDoc.id + " Nro:" + str(
                    cabecera.numDoc) + " Prov: " + cabecera.proveedor.razon_social \
                       + " " + concepto.descripcion + " " + str(concepto.cantidad) + " Unid."
                mc = TipoMovCaja.objects.get(pk=3)
                m = MovCaja(caja=caja, empresa=cabecera.afectaEmpresa, tipoDoc=cabecera.tipoDoc,
                            numDoc=cabecera.numDoc,
                            descripcion=desc, operador=request.user, importe=precioConcepto, tipoMovCaja=mc)
                m.save()

            # Actualizamos el campo salida de Caja
            # if caja.acumSalidas >= 0:
            #     caja.acumSalidas += precioConcepto
            # else:
            #     caja.acumSalidas = precioConcepto
            # caja.save()

        cabecera.save()
        return cabecera

    def abrirCaja(self, obra, tipoCaja = None):
        if tipoCaja is None:
            tipoCaja = TipoCaja.objects.get(pk=1)
        c = Caja(tipoCaja=tipoCaja, destino=obra)
        c.save()
        return c


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(Pedido, PedidoAdmin)
# admin.site.register(Remito, RemitoAdmin)

