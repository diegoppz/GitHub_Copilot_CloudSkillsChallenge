fetch('https://api.trakt.tv/movies/watched/daily', {
    headers: {
        'Content-Type': 'application/json',
        'trakt-api-version': '2',
        'trakt-api-key': 'https://staging.trakt.tv/oauth/applications/2006'
    }
})
.then(response => response.json())
.then(data => {
    // Atualize sua página com os dados aqui
    console.log(data);
})
.catch(error => console.error('Error:', error));
