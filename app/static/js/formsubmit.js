//function process
function setDuit(data) {
  $('#duit').text(data.result)
  $('#boxDuit').addClass('alert-success')
}
$(function(){
  $('#btnrekreasi').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      htm : $("#htm").val(),
      pengunjung : $("#pengunjung").val(),
      persentase : $("#persen").val()
    }, function(data) {
      setDuit(data);
    });
    return false;
  });

  $('#btnhotel').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      kmrhotel : $("#hotelkamar").val()
    }, function(data) {
      setDuit(data);
    });
    return false;
  });

  $('#btnresto').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      jmlkur : $("#jmlkursi").val()
    }, function(data) {
      setDuit(data);
    });
    return false;
  });

  $('#btnmall').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      lmall : $("#luasruang").val()
    }, function(data) {
      setDuit(data);
    });
    return false;
  });

  $('#btnpub').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      lpub : $("#pubbarluas").val()
    }, function(data) {
      setDuit(data);
    });
    return false;
  });

  $('#btndiskotik').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      ldisk : $("#diskotikluas").val()
    }, function(data) {
      setDuit(data);
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
      setDuit(data);
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
      setDuit(data);
    });
    return false;
  });

  $('#btnnsp').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      sambung : $("#nsp").val()
    }, function(data) {
      setDuit(data);
    });
    return false;
  });

  $('#btnbank').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      luasbank : $("#luasbankktr").val()
    }, function(data) {
      setDuit(data);
    });
    return false;
  });

  $('#btnbioskop').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      jlayar : $("#jmllayar").val()
    }, function(data) {
      setDuit(data);
    });
    return false;
  });

  $('#btnbazaar').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      haribazaar : $("#hariAcara").val()
    }, function(data) {
      setDuit(data);
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
      setDuit(data);
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
      setDuit(data);
    });
    return false;
  });

  $('#btnradio').click(function() {
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      thnRadio : $("#tahunRadio").val(),
      iklanRadio : $("#auditRadio").val()
    }, function(data) {
      setDuit(data);
    });
    return false;
  });

});
