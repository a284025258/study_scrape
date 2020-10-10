import requests


response = requests.get('https://static2.scrape.cuiqingcai.com/', cert=('/path/server.crt', '/path/server.key'))
print(response.status_code)
