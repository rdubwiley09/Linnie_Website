$(document).ready(function(){
  $("#nav-button").on('click',function(){
    $("#dropdown").toggleClass("show");
  });
  $('[data-toggle="tooltip"]').tooltip();
  $("#myCarousel").carousel();
  $(".item").click(function(){
    $("#myCarousel").carousel(5);
  });
  $(".left").click(function(){
    $("myCarousel").carousel("prev");
  });
});
