
	alert("hola");
  var meses = new Array ("ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE");
  a = "{{fact_iva}}";
  b = "{{desc_iva}}";
  ivaFact = parseFloat(a.replace(",","."), 10);
  descuento = parseFloat(b.replace(",","."), 10);
  diferencia = descuento - ivaFact;
  signoDiferencia = 0;

  if (diferencia < 0){
    diferencia = diferencia * (-1);
  }

  porc = (diferencia * 100) / (ivaFact + descuento + diferencia);
  slice = ((porc < 30) ? true : false);
  var f = new Date();
  var mes = meses[f.getMonth()];
  {% if mespy %}
  mes = meses[{{mespy}}-1];
  pont = {y:10.54}
  {% endif %}

  <!-- ///////////////////////// -->
  <!--       GRAFICO             -->
  <!-- ///////////////////////// -->
  $('#grafico-iva').highcharts({
    chart: {
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false
    },
    title: {
      text: 'DISCRIMINACION DEL IVA DE '+mes
    },
    xAxis: {
            categories: ['Torta', 'Barras']
        },
    tooltip: {
      pointFormat: 'porcentaje: <b>{point.percentage:.1f} %</b>'
    },
    plotOptions: {
      pie: {
        allowPointSelect: false,
        cursor: 'pointer',
        dataLabels: {
          enabled: true,
          color: '#000000',
          connectorColor: '#000000',
          format: '<b>{point.name}</b>: ${point.y:.2f} '
        }
      }
    },
    // series: [{
    //   type: 'pie',
    //   name: 'Cantidad',
    //   data: [

    //   ['Iva a favor', ivaFact],
    //   {
    //     name: 'Diferencia (a pagar)',
    //                 //y: ({{fact_iva}} - {{desc_iva}}),
    //                 y: diferencia,
    //                 sliced: slice,
    //                 selected: true
    //               },
    //               ['Iva facturado', descuento]

    //               ]
    //             }]
    series: [{
            type: 'column',
            name: 'Iva a favor',
            data: [0,ivaFact]
        }, {
            type: 'column',
            name: 'Diferencia',
            data: [0,diferencia]
        }, {
            type: 'column',
            name: 'Iva facturado',
            data: [0,descuento]
        }, {
            type: 'pie',
            name: 'Total consumption',
            data: [{
                name: 'Jane',
                y: 13,
                color: Highcharts.getOptions().colors[0] // Jane's color
            }, {
                name: 'John',
                y: 23,
                color: Highcharts.getOptions().colors[1] // John's color
            }, {
                name: 'Joe',
                y: 19,
                color: Highcharts.getOptions().colors[2] // Joe's color
            }],
            center: [100, 80],
            size: 100,
            showInLegend: false,
            dataLabels: {
                enabled: false
            }
        }]
  });



<!-- ///////////////////////// -->
<!--       FIN GRAFICO         -->
<!-- ///////////////////////// -->
