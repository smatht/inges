$(document).ready(function() {
    var m2mLen = $('#id_facturas option').length
    if (m2mLen <= 15)
        $('#id_facturas').attr('size', m2mLen+1);

    var slcProv = $('#id_proveedor');

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
    setTimeout(function(){
        document.getElementById('id_facturas_input').setAttribute('readonly', 'readonly');
    }, 1000);
});