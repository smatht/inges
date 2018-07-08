$(document).ready(function() {

	var rdoContado = $('#id_condPago_0');
    var rdoCredito = $('#id_condPago_1');
    var fieldsetFechaVto = $('#fieldsetcollapser0')[0]
    var fieldsetContado = $('#fieldsetcollapser1')[0]

    //  Si se selecciona, esconde m2m de facturas
    rdoCredito.on('click', function (e){
        if ($(this).is(":checked")){
        	// Si esta oculto muestro campo fecha de vencimiento
        	var thisClase = $('#fieldsetcollapser0').parent().parent().attr("class");
            if (thisClase.includes('collapsed'))
            	$('#fieldsetcollapser0')[0].click();
            // Si esta mostrando opciones de caja la oculto
            var otraClase = $('#fieldsetcollapser1').parent().parent().attr("class");
            if (!otraClase.includes('collapsed'))
            	$('#fieldsetcollapser1')[0].click();
            // Si esta activo check generar mov. caja lo desactivo y deshabilito
            $('#id_afectaCaja').attr('checked', false);
            $('#id_afectaCaja').attr('disabled', true);
            $('#id_tipoCaja').attr('disabled', true);
        }
    });
    rdoContado.on('click', function (e){
        if ($(this).is(":checked")){
        	var thisClase = $('#fieldsetcollapser1').parent().parent().attr("class");
            if (thisClase.includes('collapsed'))
            	$('#fieldsetcollapser1')[0].click();

            var otraClase = $('#fieldsetcollapser0').parent().parent().attr("class");
            if (!otraClase.includes('collapsed'))
            	$('#fieldsetcollapser0')[0].click();

            $('#id_afectaCaja').attr('checked', true);
            $('#id_afectaCaja').attr('disabled', false);
            $('#id_tipoCaja').attr('disabled', false);
        }
    });

    setTimeout(function(){
        $('#fieldsetcollapser1')[0].click();
        
    }, 1000);


 });