import requests

def check_github_status():
    response = requests.get('https://kctbh9vrtdwd.statuspage.io/api/v2/status.json')
    status = response.json()['status']['description']
    print(f'O status atual do GitHub é: {status}')

check_github_status()
