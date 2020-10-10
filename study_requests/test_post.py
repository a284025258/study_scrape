import requests

data = {
    'name': 'Jax',
    'age': 18
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
response = requests.post(url='http://httpbin.org/post', headers=headers, data=data)
print(response.json())
