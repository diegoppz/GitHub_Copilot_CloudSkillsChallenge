fetch('https://api.trakt.tv/movies/watched/daily', {
    headers: {
        'Content-Type': 'application/json',
        'trakt-api-version': '2',
        'trakt-api-key': 'b6185b6d7a1f52babb0df5c16dd9c65c822590d0a2aee602de80ff5fa7771818'
    }
})
.then(response => response.json())
.then(data => {
    // Atualize sua página com os dados aqui
    console.log(data);
})
.catch(error => console.error('Error:', error));
