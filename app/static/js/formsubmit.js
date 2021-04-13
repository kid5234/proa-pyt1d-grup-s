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

});
