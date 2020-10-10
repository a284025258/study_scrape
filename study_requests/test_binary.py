import requests


response = requests.get(url='https://github.com/favicon.ico')
print(response.text)
print(response.content)
with open(file='./favicon.ico', mode='wb') as f:
    f.write(response.content)
