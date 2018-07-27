$(function()
{
    var ticker = function()
    {
        setTimeout(function(){
            $('.noticias li:first').animate( {marginTop: '-275px'}, 2000, function()
            {
                $(this).detach().appendTo('.noticias').removeAttr('style'); 
            });
            ticker();
        }, 10000);
    };
    ticker();
});

$(document).ready(function() {
    // nivo slider ------------------------------------------------------ //
    $('#slider').nivoSlider({
        effect:'fade', //Specify sets like: 'fold,fade,sliceDown'
        slices:3,
        animSpeed:500, //Slide transition speed
        pauseTime:5000,
        startSlide:2, //Set starting Slide (0 index)
        directionNav:true, //Next & Prev
        directionNavHide:true, //Only show on hover
        controlNav:true, //1,2,3...
        controlNavThumbs:false, //Use thumbnails for Control Nav
        controlNavThumbsFromRel:false, //Use image rel for thumbs
        controlNavThumbsSearch: '...', //Replace this with...
        keyboardNav:false, //Use left & right arrows
        pauseOnHover:false, //Stop animation while hovering
        manualAdvance: false, //Force manual transitions
        captionOpacity:0.7 //Universal caption opacity
    });

    $('.nivo-prevNav').css('display', 'none');
    $('.nivo-nextNav').css('display', 'none');
        
    $('.nivo-imageLink').hover(
        function(){
            $('.nivo-prevNav').css('display', 'block');
            $('.nivo-nextNav').css('display', 'block');
        },
        function(){
            $('.nivo-prevNav').css('display', 'none');
            $('.nivo-nextNav').css('display', 'none');
        }
    );
    $('.nivo-prevNav, .nivo-nextNav').hover(
        function(){
            $('.nivo-prevNav').css('display', 'block');
            $('.nivo-nextNav').css('display', 'block');
        },
        function(){
            $('.nivo-prevNav').css('display', 'none');
            $('.nivo-nextNav').css('display', 'none');
        }
    );
});
