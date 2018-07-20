<?php
  session_start();
  $datos=$_POST['cadena'];

  $query = "UPDATE usuarioe set cadenaVal = '$datos', edad = 0, peso = 0 WHERE usuarioKey = 1";

  $mysqli = mysqli_connect('127.0.0.1', 'root', '1234567890', 'usuarioenfermedades');
  $resul = mysqli_query($mysqli, $query);
  $mysqli ->close();
?>
