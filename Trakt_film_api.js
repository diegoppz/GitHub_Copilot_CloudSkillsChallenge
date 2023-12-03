fetch('https://api.trakt.tv/movies/watched/daily', {
    headers: {
        'Content-Type': 'application/json',
        'trakt-api-version': '2',
        'trakt-api-key': '6cc206bf89b66802c80c58d2cc1250e0d805e225fbcdab067c6c96a4da3c4454'
    }
})
.then(response => response.json())
.then(data => {
    // Atualize sua página com os dados aqui
    console.log(data);
})
.catch(error => console.error('Error:', error));
