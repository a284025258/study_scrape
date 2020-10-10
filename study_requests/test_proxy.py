import requests


proxies = {
    'http': 'http://10.10.10.10:1080',
    'https': 'https://10.10.10.10:1080'
}
requests.get(url='https://httpbin.org/get', proxies=proxies)