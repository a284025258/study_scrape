from pyquery import PyQuery
import requests


# doc = PyQuery(requests.get('https://www.cuiqingcai.com').text)  # 与下面写法等价
doc = PyQuery(url='https://www.baidu.com', encoding='utf-8')
print(doc('title'))
