import requests
import json

# Incluir chave de API https://staging.trakt.tv/oauth/applications/2006
headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': '6cc206bf89b66802c80c58d2cc1250e0d805e225fbcdab067c6c96a4da3c4454'
}

# Obter os filmes mais assistidos no dia anterior
response = requests.get('https://api.trakt.tv/movies/watched/daily', headers=headers)
daily_movies = response.json()

# Obter os filmes mais assistidos no último ano
response = requests.get('https://api.trakt.tv/movies/watched/yearly', headers=headers)
yearly_movies = response.json()

# Imprimir os resultados
for movie in daily_movies[:5]:
    print(f"Title: {movie['movie']['title']}")
    print(f"Year: {movie['movie']['year']}")
    print(f"Watches: {movie['watcher_count']}")
    print()

for movie in yearly_movies[:5]:
    print(f"Title: {movie['movie']['title']}")
    print(f"Year: {movie['movie']['year']}")
    print(f"Watches: {movie['watcher_count']}")
    print()
