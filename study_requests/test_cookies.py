import requests


response = requests.get(url='https://www.baidu.com')
print(response.cookies)
for key, value in response.cookies.items():
    print(f'key: {key}, value: {value}')
