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
    'diskotik' : $('#formdiskotik'),
    'nsp' : $('#formnsp'),
    'bank' : $('#formbank'),
    'bioskop' : $('#formbioskop'),
    'pesawat' : $('#formpesawat'),
    'bazaar' : $('#formbazaar'),
    'kereta' : $('#formtransport')
  };

  $('#cat').change(function(){
    $('#cat').find('[value="0"]').attr('hidden','hidden');
    $.each($.selMap, function() { this.hide(); this.trigger('reset') });
    $.selMap[$(this).val()].show();
    $('#duit').text('0');
  });

  $('#cekradio-0').click(function(){
    $('#htm').removeAttr("disabled");
    $('#pengunjung').removeAttr("disabled");
    $('#persen').removeAttr("disabled");
  });

  $('#cekradio-1').click(function(){
    $('#htm').attr("disabled","disabled");
    $('#pengunjung').attr("disabled","disabled");
    $('#persen').attr("disabled","disabled");
    $('#htm').val('0');
    $('#pengunjung').val('0');
    $('#persen').val('0');
  });

  $('#konsercek-0').click(function(){
    $('#bproduksi').attr("disabled","disabled");
    $('#freetiket').removeAttr("disabled");
    $('#grosstiket').removeAttr("disabled");
    $('#bproduksi').val('0');
  });

  $('#konsercek-1').click(function(){
    $('#bproduksi').removeAttr("disabled");
    $('#freetiket').attr("disabled","disabled");
    $('#grosstiket').attr("disabled","disabled");
    $('#freetiket').val('0');
    $('#grosstiket').val('0');
  });

});
