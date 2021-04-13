// document ready
$(document).ready(function() {
  $.selMap = {
    'rekreasi' : $('#formrekreasi'),
    'konser' : $('#formkonser'),
    'karaoke' : $('#formkaraoke'),
    'maldsb' : $('#formmall'),
    'hotel' :  $('#formhotel'),
    'restokafe' :  $('#formrestokafe'),
    'pubbar' : $('#formpubbar'),
    'diskotik' : $('#formdiskotik')
  };

  $('#cat').change(function(){
    $.each($.selMap, function() { this.hide(); this.trigger('reset') });
    $.selMap[$(this).val()].show();
  });

  $('#tiketya').click(function(){
    $('#htm').removeAttr("disabled");
    $('#pengunjung').removeAttr("disabled");
    $('#persen').removeAttr("disabled");
  });

  $('#tiketga').click(function(){
    $('#htm').attr("disabled","disabled");
    $('#pengunjung').attr("disabled","disabled");
    $('#persen').attr("disabled","disabled");
    $('#htm').val('0');
    $('#pengunjung').val('0');
    $('#persen').val('0');
  });

  $('#konserya').click(function(){
    $('#bproduksi').attr("disabled","disabled");
    $('#freetiket').removeAttr("disabled");
    $('#grosstiket').removeAttr("disabled");
    $('#bproduksi').val('0');
  });

  $('#konserga').click(function(){
    $('#bproduksi').removeAttr("disabled");
    $('#freetiket').attr("disabled","disabled");
    $('#grosstiket').attr("disabled","disabled");
    $('#freetiket').val('0');
    $('#grosstiket').val('0');
  });

});
