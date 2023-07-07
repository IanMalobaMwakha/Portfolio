

/**
 * 
$(document).ready(function() {
    $('.navTrigger').click(function() {
      $(this).toggleClass('active');
      $("#mainListDiv").toggleClass("show_list");
    });
  
    $('.navlinks li a').click(function() {
      $('.navTrigger').removeClass('active');
      $("#mainListDiv").removeClass("show_list");
    });
  
    $(window).scroll(function() {
      if ($(document).scrollTop() > 50) {
        $('.nav').addClass('affix');
      } else {
        $('.nav').removeClass('affix');
      }
    });
  });
  

 * 
 * 
 * 
 * 
 * 
 * 
 * References
 * $('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});
 * 
 * https://codepen.io/ianmalobamwakha/pen/xxQXVyR
 * 
 * https://codepen.io/albizan/pen/mMWdWZ
 * 
 * 
 */