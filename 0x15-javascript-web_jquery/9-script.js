// 9-script.js
$(document).ready(function() {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    success: function(response) {
      $('#hello').text(response.hello);
    }
  });
});

