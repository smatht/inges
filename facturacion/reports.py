from facturacion.models import *
from model_report.report import reports, ReportAdmin

class FRecibidasReport(ReportAdmin):
    title = ('Reporte de Facturas Recibidas')
    model = Factura_recibida
    fields = [
		'fecha',
		'emisor',
		'nro_factura',
		'neto',
		'iva',
    ]
    list_order_by = ('emisor',)
    type = 'report'

reports.register('anymodel-report', FRecibidasReport)