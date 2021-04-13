//function process
$(function(){
  $('#btnrekreasi').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      htm : $("#htm").val(),
      pengunjung : $("#pengunjung").val(),
      persentase : $("#persen").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btnhotel').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      kmrhotel : $("#hotelkamar").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btnresto').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      jmlkur : $("#jmlkursi").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btnmall').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      lmall : $("#luasruang").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btnpub').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      lpub : $("#pubbarluas").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btndiskotik').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      ldisk : $("#diskotikluas").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btnkaraoke').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      raula : $("#karaokeaula").val(),
      rklg : $("#karaokefamili").val(),
      rex : $("#karaokeeksekutif").val(),
      rkubus : $("#karaokebooth").val(),
      hkerja : $("#harikerja").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btnkonser').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      tiketkotor : $("#grosstiket").val(),
      tiketgratis : $("#freetiket").val(),
      biayaprod : $("#bproduksi").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btnnsp').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      sambung : $("#nsp").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btnbank').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      luasbank : $("#luasbankktr").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btnbioskop').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      jlayar : $("#jmllayar").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btnbazaar').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      haribazaar : $("#hariAcara").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btntransport').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      jpnumpang : $("#jmlpenumpang").val(),
      hrgtiket : $("#hrgtikettransport").val(),
      durasi : $("#durasimsk").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });

  $('#btnpesawat').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      jpnumpangpswt : $("#jmlpenumpangpswt").val(),
      hrgtiketpswt : $("#hrgtiketpswt").val(),
      durasipswt : $("#durasimskpswt").val(),
      durasipswtog : $("#durasimskpswtog").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });
});
