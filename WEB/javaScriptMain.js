var cadena = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
function escogerOpcion(imgGray, imgCol, posCadena, id){
  var img = document.getElementById(id);
  if(img == imgGray){
       img.setAttribute("src", imgCol);
       cadena[posCadena] = 1;
  }
  else if(img == imgCol){
       img.setAttribute("src", imgGray);
       cadena[posCadena] = 0;
  }
  return cadena;
}
