# HTTP Basic Access Authentication
import requests


response = requests.get(url='https://static3.scrape.cuiqingcai.com/', auth=('admin', 'admin'))
print(response.status_code)
