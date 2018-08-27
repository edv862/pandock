$("#rslides").responsiveSlides({
  auto: true,             // Boolean: Animate automatically, true or false
  speed: 1000,            // Integer: Speed of the transition, in milliseconds
  timeout: 3800,          // Integer: Time between slide transitions, in milliseconds
  pager: false,           // Boolean: Show pager, true or false
  nav: false,             // Boolean: Show navigation, true or false
  random: false,          // Boolean: Randomize the order of the slides, true or false
  pause: false,           // Boolean: Pause on hover, true or false
  pauseControls: true,    // Boolean: Pause when hovering controls, true or false
  prevText: "Previous",   // String: Text for the "previous" button
  nextText: "Next",       // String: Text for the "next" button
  maxwidth: "",           // Integer: Max-width of the slideshow, in pixels
  navContainer: "",       // Selector: Where controls should be appended to, default is after the 'ul'
  manualControls: "",     // Selector: Declare custom pager navigation
  namespace: "rslides"    // String: Change the default namespace used
});

$(document).ready(function(){
  $('.card-header').on('click', function(){
      $('.recetas-list').css('height', "110px");
  })

  $('.mas-recetas').on("click", function(){
    lista = $(this).data('lista');
    status = $(this).data('status');

    if (status == 1){
      $("#"+lista).animate({
        height: "110px",
      }, 750);
      $(this).data('status', 0);
    } else {
      height = $(this).data('recetas') * 28;
      $("#"+lista).animate({
        height: height+"px",
      }, 750);
      $(this).data('status', 1);
    }
  })
})