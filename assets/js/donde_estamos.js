function show(theid) {
    document.getElementById(theid).style.visibility='visible';
    document.getElementById(theid).style.display='block';       
};
function hide(theid) {
    document.getElementById(theid).style.visibility='hidden';
    document.getElementById(theid).style.display='none';    
};

$(document).ready(function(){
    last_dir = $('.direccion:first').data('id');
    first_link = $('.direccion:first').data('link');
    $('#google_map').attr('src', first_link);
    $('#google_link').attr('href', first_link);

    $('.direccion').on('mouseover', function(){
        id = $(this).data('id');
        $('.indicaciones #text-direccion'+last_dir).removeClass('d-block');
        $('.indicaciones #text-direccion'+last_dir).addClass('d-none');

        url = $(this).data('link');
        $('.indicaciones #text-direccion'+id).addClass('d-block');
        $('#google_map').attr('src', url);
        $('#google_link').attr('href', url);

        last_dir = id;
    });
});