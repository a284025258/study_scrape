import re


content1 = '2020-10-11 14:48'
content2 = '2021-10-11 14:48'
content3 = '2022-10-11 14:48'
pattern = re.compile(r'\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)
