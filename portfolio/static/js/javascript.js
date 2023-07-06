$('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});

/**
 * References
 * 
 * https://codepen.io/ianmalobamwakha/pen/xxQXVyR
 * 
 * https://codepen.io/albizan/pen/mMWdWZ
 * 
 * 
 */