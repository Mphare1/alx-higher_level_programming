$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (body) {
  $('DIV#character').text(body['name']);
});
