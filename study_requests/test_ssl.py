import requests
import logging


logging.captureWarnings(True)
response = requests.get(url='https://static2.scrape.cuiqingcai.com/', verify=False, timeout=(5, 10))
print(response.status_code)
