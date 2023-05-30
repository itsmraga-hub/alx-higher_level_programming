// script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) => {
    if (textStatus === 'success') {
      const films = data.results;
      films.forEach(film => {
        $('#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  });
});
