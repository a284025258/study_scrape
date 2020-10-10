import re


content = 'http://weibo.com/comment/kEraCN'
result1 = re.match(r'http.*?comment/(.*?)', content)
result2 = re.match(r'http.*?comment/(.*)', content)
print(f'result1: {result1.group(1)}')
print(f'result2: {result2.group(1)}')
