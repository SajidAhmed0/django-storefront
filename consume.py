import requests

response = requests.get('http://127.0.0.1:8000/drinks/1', headers={'Accept': 'application/json'})

print(response.json())