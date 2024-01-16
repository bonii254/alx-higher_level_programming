$(function () {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
        var movies = data.results;
        var list = $('#list_movies');

        $.each(movies, function (index, movie) {
            $('<li>').text(movie.title).appendTo(list);
        });
    });
});