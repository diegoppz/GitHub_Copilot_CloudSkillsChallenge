import requests
import json

def check_github_status():
    response = requests.get('https://kctbh9vrtdwd.statuspage.io/api/v2/status.json')
    data = response.json()
    return data['status']['description']

print(check_github_status())

