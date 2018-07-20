<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
  	<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
  	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="css/bootstrap.min.css"/>
  	<script href = "js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="formulario.css"/>
  	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
  	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
    <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Slabo+27px" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Libre+Baskerville" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Quicksand" rel="stylesheet">
    <title>Formulario de Síntomas</title>
  </head>
  <body>
    <div class = "flexBox">
          <div class="dropdown">
            <a class="btn btn-secondary dropdown-toggle" id = "drop" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Menú
            </a>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
              <a class="dropdown-item" >Inicio</a>
              <a class="dropdown-item" href="#">Medicamentos</a>
              <a class="dropdown-item" href="#">Inteligencia Artificial</a>
            </div>
          </div>
          <h1 id = "main">Ingresando Síntomas</h1>
    </div>
    <div class="card mb-3" id = "mainCarro">
      <img class="card-img-top" src="Imagenes/diag.png" alt="Card image cap">
    </div>
    <p id = "instrucciones">A continuación seleccione los síntomas que presenta.</p>
    <div id = "cuestionario">
        <div class="flexBox">
            <div class="flexBox">
              <div class = "alineacion">
                <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 0, 'sintom1');">
                  <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom1"/>
                  <div class="card-img-overlay">
                    <p class="card-title">Síntoma 1</p>
                  </div>
                </div>
              </div>
              <div class = "alineacion">
                <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 1, 'sintom2');">
                  <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom2"/>
                  <div class="card-img-overlay">
                   <p class="card-title">Síntoma 2</p>
                 </div>
                </div>
              </div>
            </div>
            <div class="flexBox">
               <div class = "alineacion">
                  <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 2, 'sintom3');">
                    <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom3"/>
                    <div class="card-img-overlay">
                      <p class="card-title">Síntoma 3</p>
                    </div>
                  </div>
               </div>
            </div>
        </div>
        <div class="flexBox">
            <div class="flexBox">
              <div class = "alineacion">
                <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 3, 'sintom4');">
                  <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom4"/>
                  <div class="card-img-overlay">
                    <p class="card-title">Síntoma 4</p>
                  </div>
                </div>
              </div>
              <div class = "alineacion">
                <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 4, 'sintom5');">
                  <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom5"/>
                  <div class="card-img-overlay">
                   <p class="card-title">Síntoma 5</p>
                 </div>
                </div>
              </div>
            </div>
            <div class="flexBox">
               <div class = "alineacion">
                  <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 5, 'sintom6');">
                    <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom6"/>
                    <div class="card-img-overlay">
                      <p class="card-title">Síntoma 6</p>
                    </div>
                  </div>
               </div>
            </div>
        </div>
        <div class="flexBox">
            <div class="flexBox">
              <div class = "alineacion">
                <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 6, 'sintom7');">
                  <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom7"/>
                  <div class="card-img-overlay">
                    <p class="card-title">Síntoma 7</p>
                  </div>
                </div>
              </div>
              <div class = "alineacion">
                <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 7, 'sintom8');">
                  <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom8"/>
                  <div class="card-img-overlay">
                   <p class="card-title">Síntoma 8</p>
                 </div>
                </div>
              </div>
            </div>
            <div class="flexBox">
               <div class = "alineacion">
                  <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 8, 'sintom9');">
                    <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom9"/>
                    <div class="card-img-overlay">
                      <p class="card-title">Síntoma 9</p>
                    </div>
                  </div>
               </div>
            </div>
        </div>
        <div class="flexBox">
            <div class="flexBox">
              <div class = "alineacion">
                <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 9, 'sintom10');">
                  <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom10"/>
                  <div class="card-img-overlay">
                    <p class="card-title">Síntoma 10</p>
                  </div>
                </div>
              </div>
              <div class = "alineacion">
                <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 10, 'sintom11');">
                  <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom11"/>
                  <div class="card-img-overlay">
                   <p class="card-title">Síntoma 11</p>
                 </div>
                </div>
              </div>
            </div>
            <div class="flexBox">
               <div class = "alineacion">
                  <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 11, 'sintom12');">
                    <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom12"/>
                    <div class="card-img-overlay">
                      <p class="card-title">Síntoma 12</p>
                    </div>
                  </div>
               </div>
            </div>
        </div>
        <div class="flexBox">
            <div class="flexBox">
              <div class = "alineacion">
                <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 12, 'sintom13');">
                  <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom13"/>
                  <div class="card-img-overlay">
                    <p class="card-title">Síntoma 13</p>
                  </div>
                </div>
              </div>
              <div class = "alineacion">
                <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 13, 'sintom14');">
                  <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom14"/>
                  <div class="card-img-overlay">
                   <p class="card-title">Síntoma 14</p>
                 </div>
                </div>
              </div>
            </div>
            <div class="flexBox">
               <div class = "alineacion">
                  <div class="card bg-dark text-white col" id = "anexo" onclick="escogerOpcion('pulmonGray.jpg', 'pulmon.jpg', 14, 'sintom15');">
                    <img  src="Imagenes/pulmonGray.jpg"  class="img-fluid" alt="Responsive image" id = "sintom15"/>
                    <div class="card-img-overlay">
                      <p class="card-title">Síntoma 15</p>
                    </div>
                  </div>
               </div>
            </div>
        </div>
    </div>
    <div class="jumbotron">
        <h1 class="display-4">Enviar resultados</h1>
        <p class="lead">A coontinuación se enviarán tus resultados para poder determinar la enfermedad que puedes llegar a tener.</p>
        <hr class="my-4">
        <p>Es importante mencionar que con base a tu edad, peso y altura, se te mostrará una lista de medicamentos con porciones para poder remediar con la enfermedad o infección que puedes estar portando.</p>
        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter" id = "enviar">
          Enviar respuestas
        </button>
    </div>
    <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalCenterTitle">¿Estás seguro que has ingresado todos tus síntomas?</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            Al ingresar todos los síntomas que presentas, nos facilitas poder hacer un diagnótico con mayor precisión.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Regresar</button>
            <button type="button" class="btn btn-primary" onclick="corroborar();">Continuar</button>
          </div>
        </div>
      </div>
    </div>
    <script type="text/javascript">
          var sintomas = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]; //Tiene que tener el mismo orden de las entradas de las redes neuronales.
          function escogerOpcion(imgGray, imgCol, posCadena, id){
            var img = document.getElementById(id);
            cadena = img.src;
            var res = cadena.split("/");
            if(res[res.length-1] == imgGray){
                final = "Imagenes/"+imgCol;
                img.setAttribute("src", final);
                sintomas[posCadena] = 1;
            }
            else if(res[res.length-1] == imgCol){
                final = "Imagenes/"+imgGray;
                img.setAttribute("src", final);
                sintomas[posCadena] = 0;
            }
            console.log(sintomas);
            return sintomas;
          }
          function corroborar(){
          	var string = JSON.stringify(sintomas);
          	var ajaxe = new XMLHttpRequest();
          	ajaxe.onreadystatechange = function(){
          		if(this.readyState == 4 && this.status == 200){
          			console.log(this.response);
          		}
          	}
          	ajaxe.open("POST", "enviandoCadena.php", true);
          	ajaxe.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
          	ajaxe.send("cadena=" + string);
            return;
          }
    </script>
  </body>
</html>