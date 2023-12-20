document.addEventListener("DOMContentLoaded", function(){
    var mouseX, mouseY;
    var traX, traY;
    if(document.getElementById("title")){
      document.addEventListener('mousemove', function(){
        mouseX = event.pageX;
        mouseY = event.pageY;
        traX = ((4 * mouseX) / 570) + 40;
        traY = ((4 * mouseY) / 570) + 50;
        document.getElementById("title").style.backgroundPosition = traX + "%" + traY + "%";
      });
    };
  });