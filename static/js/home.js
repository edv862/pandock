$(function()
{
    var ticker = function()
    {
        setTimeout(function(){
            $('.noticias li:first').animate( {'marginTop': '-275px'}, 2000, function()
            {
                $(this).detach().appendTo('.noticias').removeAttr('style'); 
            });
            ticker();
        }, 10000);
    };
    ticker();
});

$(document).ready(function() {
    $('.carousel-item, .home-slider-control-next, .home-slider-control-prev, .carousel-custom-prev-icon, .carousel-custom-next-icon').hover(
        function(){
            $('.carousel-custom-prev-icon').css('display', 'block');
            $('.carousel-custom-next-icon').css('display', 'block');
        },
        function(){
            $('.carousel-custom-prev-icon').css('display', 'none');
            $('.carousel-custom-next-icon').css('display', 'none');
        }
    );
});
