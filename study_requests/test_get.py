import requests


data = {'name': 'germey', 'age': 25}
response = requests.get(url='http://httpbin.org/get', params=data)
print(type(response.text))
print(response.json())
print(type(response.json()))
