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
    $('.carousel-item, .carousel-control-prev, .carousel-control-next, .carousel-control-prev-icon, .carousel-control-next-icon').hover(
        function(){
            $('.carousel-control-prev-icon').css('display', 'block');
            $('.carousel-control-next-icon').css('display', 'block');
        },
        function(){
            $('.carousel-control-prev-icon').css('display', 'none');
            $('.carousel-control-next-icon').css('display', 'none');
        }
    );
});
