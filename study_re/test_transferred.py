import re


content = '(百度) www.baidu.com'
result = re.match(r'\(.*\).*\..*\..*', content)
print(result)
