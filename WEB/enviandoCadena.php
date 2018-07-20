<?php
  session_start();
  $datos=$_POST['cadena'];
  $datosdec=json_decode($datos);
  echo $datosdec;
?>
