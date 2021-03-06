$("#rslides").responsiveSlides({
  auto: true,             // Boolean: Animate automatically, true or false
  speed: 1900,            // Integer: Speed of the transition, in milliseconds
  timeout: 5000,          // Integer: Time between slide transitions, in milliseconds
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
      $('.recetas-list').css('height', "93px");
  })

  $('.mas-recetas').on("click", function(){
    lista = $(this).data('lista');
    status = $(this).data('status');
    animation_time = $(this).data('recetas') * 35;

    if (status == 1){
      $("#"+lista).animate({
        height: "93px",
      }, animation_time);
      $(this).data('status', 0);
    } else {
      height = $(this).data('recetas') * 23;
      $("#"+lista).animate({
        height: height+"px",
      }, animation_time);
      $(this).data('status', 1);
    }
  })
})