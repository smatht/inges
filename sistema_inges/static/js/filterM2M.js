$(document).ready(function() {
//  Dimensiono caja dependiendo de la cantidad de lineas que haya
    var m2mLen = $('#id_facturas option').length
    if (m2mLen <= 15)
        $('#id_facturas').attr('size', m2mLen+1);

//  Campo Proveedor
    var slcProv = $('#id_proveedor');
    var totalValores = $('#id_total_valores');
    var aPagar = $('#id_total_a_pagar');
    var diferencia = $('#id_diferencia');
    totalValores.attr('disabled', 'disabled')
    aPagar.attr('disabled', 'disabled');
    diferencia.attr('disabled', 'disabled');

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

//  Al select id_facturas_filter Django lo carga en tiempo de ejecucion por lo que al cargar este JS todavia no existe
//  el select entonces se espera 1000 ms antes de operar con el select.
    setTimeout(function(){
        $('#id_facturas_filter').css('display', 'none');
        slcProv.trigger("change");

        // Capturo el evento change del segundo select multiple
        $('#id_facturas_to').on('change', function (e){
            $.ajax({
                type: "GET",
                dataType: "json",
                ContentType: "application/json",
                url: "http://127.0.0.1:8000/api/compras/62/",
                success: function(inp_data, status, jqXHR){
//                    alert('success');
//                    alert(JSON.stringify(inp_data));
                      aPagar.val(inp_data.saldo);
                      diferencia.val(totalValores.val()-aPagar.val())
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
        totalValores.val(importe.val());
        diferencia.val(totalValores.val()-aPagar.val());
    });
});