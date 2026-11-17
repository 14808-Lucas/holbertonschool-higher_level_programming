const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const list = document.querySelector('#list_movies');
    const movies = data.results;

    for (let i = 0; i < movies.length; i++) {
      const li = document.createElement('li');
      li.textContent = movies[i].title;
      list.appendChild(li);
    }
  });
