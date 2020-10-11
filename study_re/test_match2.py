import re


content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search(r'Hello.*', content)
print(result)
