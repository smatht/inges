$(document).ready(function() {
//  Dimensiono caja dependiendo de la cantidad de lineas que haya
    var m2mLen = $('#id_facturas option').length
    if (m2mLen <= 15)
        $('#id_facturas').attr('size', m2mLen+1);

//  DEFINICION DE ESTILOS
    styleWarning = {
                        'color': '#c09853',
                        'background-color': '#fff',
                        'border': '2px solid #c09853'
                     };
    styleInfo = {
                        'color': '#3a87ad',
                        'background-color': '#fff',
                        'border': '2px solid #3a87ad'
                     };
    styleSuccess = {
                        'color': '#468847',
                        'background-color': '#fff',
                        'border': '2px solid #468847'
                     };
    styleError = {
                        'color': '#b94a48',
                        'background-color': '#fff',
                        'border': '2px solid #b94a48'
                     };
    styleNormal = {
                        'color': '#000',
                        'background-color': '#fff',
                        'border': '1px solid #ccc'
                     };

//  Campo Proveedor y totales
    var slcProv = $('#id_proveedor');
    var totalValores = $('#id_total_valores');
    var aPagar = $('#id_total_a_pagar');
    var diferencia = $('#id_diferencia');
    var rdoFactura = $('#id_tipoPago_0');
    var rdoCuenta = $('#id_tipoPago_1');
    var secFacturas = $('.field-facturas');
    totalValores.attr('readonly', true)
    totalValores.css(styleNormal)
    aPagar.attr('readonly', true);
    aPagar.css(styleNormal)
    diferencia.attr('readonly', true);
    diferencia.css(styleSuccess)

//  Cuando se elige un proveedor filtra facturas de ese proveedor
    slcProv.on('change', function (e) {
        var fltFacturas = document.getElementById('id_facturas_input');
        fltFacturas.setAttribute('readonly', 'readonly');
        var optionSelected = $(this).find("option:selected");
        var valueSelected = optionSelected.text();
        fltFacturas.value = valueSelected;
        var ev = new Event('keyup', { bubbles: true});
        ev.simulated = true;
        fltFacturas.dispatchEvent(ev);
    });

//  Si se selecciona, esconde m2m de facturas
    rdoCuenta.on('click', function (e){
        if ($(this).is(":checked"))
            secFacturas.css('visibility', 'hidden');
    });
    rdoFactura.on('click', function (e){
        if ($(this).is(":checked"))
            secFacturas.css('visibility', 'inherit');
    });

    function actualizarDiferencia(importe=0, pagar=0){
        // Determina el color del campo diferencia
        var colorearDiferencia = function (){
            if (diferencia.val()==0) {
                st = styleSuccess;
            } else if (diferencia.val()<0) {
                      st = styleWarning;
                } else {
                    st = styleError;
                }
            return st;
        };
        if (importe!=0 & pagar!=0){
            aPagar.val(pagar);
            totalValores.val(importe);
            diferencia.val(importe-pagar);
            diferencia.css(colorearDiferencia());
        } else if (importe!=0 & pagar==0){
            totalValores.val(importe);
            diferencia.val(importe-aPagar.val());
            diferencia.css(colorearDiferencia());
        } else if (importe==0 & pagar!=0){
            aPagar.val(pagar);
            diferencia.val(totalValores.val()-pagar);
            diferencia.css(colorearDiferencia());
        }
    }

//  Al select id_facturas_filter Django lo carga en tiempo de ejecucion por lo que al cargar este JS todavia no existe
//  el select entonces se espera 1000 ms antes de operar con el select.
    setTimeout(function(){
        $('#id_facturas_filter').css('display', 'none');
        slcProv.trigger("change");

        // Capturo el evento change del segundo select multiple
        $('#id_facturas_to').on('change', function (e){
            var opts = document.getElementById('id_facturas_to').options;
            $.ajax({
                type: "GET",
                dataType: "json",
                ContentType: "application/json",
                url: "http://0.0.0.0:8000/api/compras/"+opts[0].value+"/",
                success: function(inp_data, status, jqXHR){
                      actualizarDiferencia(0, inp_data.saldo);
                    },
                error: function(xhr, errMsg) {
                    alert('failure');
                    console.log(errMsg);
                    console.log(xhr.status + ": " + xhr.responseText);
                    }
            });
        });
    }, 1000);

//  Recalculo diferencia cada vez que modifico el importe
    importe = $('#id_importe');
    importe.on('keyup', function (){
        if (rdoCuenta.is(":checked")){
            actualizarDiferencia(importe.val(), importe.val())
        } else {
            actualizarDiferencia(importe.val())
        }
    });
});