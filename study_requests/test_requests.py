import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
response = requests.get(url='https://static1.scrape.cuiqingcai.com/', headers=headers)
pattern = re.compile(r'<h2.*?>(.*?)</h2>', re.S)
titles = re.findall(pattern=pattern, string=response.text)
print(titles)
# with open(file='./movie.html',mode='w', encoding='utf-8') as f:
#     f.write(response.text)
