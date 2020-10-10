import requests


session = requests.Session()
session.get(url='http://httpbin.org/cookies/set/number/123456789')
response = session.get(url='http://httpbin.org/cookies')
print(response.json())
