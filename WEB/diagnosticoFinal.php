<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="graficando.css"/>
    <!--link: https://www.highcharts.com/demo/column-placement-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
  	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
    <link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet">
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/series-label.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <script src="https://code.highcharts.com/modules/export-data.js"></script>
    <title></title>
  </head>
  <body>
    <div class="flexBox" id = "headerM">
      <a  class="btn btn-primary" id="boton" onclick="solicitarEdad();" style="color: #fff;">Comenzar</a>
      <p id = "tituloMonitoreo">Monitoreo de tus signos vitales</p>
    </div>
    <div class="flexBox" id = "flexGraph">
        <div id="pulso"></div>
        <div id="temperatura" style="height: 400px; min-width: 380px"></div>
    </div>
    <div id="respiraciones" style="min-width: 310px; height: 400px;"></div>
    <button type="button" class="btn btn-primary btn-sm" style="font-size: 1em;" onclick="cambiarPagina('resultados.php', 'Diagnostico Final');">Finalizar diagnóstico</button>
    <br />
    <br />
    <br />
    <br />
    <script src="auxiliarJavaGraficandoJS.js"></script>
  </body>
</html>
