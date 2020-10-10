from requests import Session, Request


url = 'http://httpbin.org/post'
data = {'name': 'Jax'}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
s = Session()
req = Request(method='POST', url=url, data=data, headers=headers)
print(type(req))
prepared = s.prepare_request(req)
print(type(prepared))
response = s.send(prepared)
print(response.text)
