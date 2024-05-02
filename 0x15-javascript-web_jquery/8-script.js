// 8-script.js
$(document).ready(function() {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    success: function(response) {
      $.each(response.results, function(index, movie) {
        $('<li>').text(movie.title).appendTo('#list_movies');
      });
    }
  });
});

