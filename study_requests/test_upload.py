import requests


files = {'favicon.ico': open(file='./favicon.ico', mode='rb')}
response = requests.post(url='http://httpbin.org/post', files=files)
print(response.json())
