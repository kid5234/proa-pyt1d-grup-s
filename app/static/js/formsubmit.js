// Document on Form Submit Process

$(function() {
  $('#btnhotel').click(function(e) {
    e.preventDefault()
    $.getJSON('/proseshitung', {
      cat: $("#cat").val(),
      kmrhotel : $("#hotelkamar").val()
    }, function(data) {
      $('#duit').text(data.result)
    });
    return false;
  });
});
