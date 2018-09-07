$('#id_archivo').change(function(e){
  $in=$('#id_archivo');
  console.log($in.val());
  $('#file-loaded').html($in.val());
});