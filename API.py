import requests

x = requests.get('https://catfact.ninja/fact')

print(x.text)