import requests

headers = {
    'cookie': '_ga=GA1.2.1422460404.1599824325; user_trace_token=20200911193846-8357cabc-0f9f-40db-ac2c-db8d334e04b2; LGUID=20200911193846-c7771dd1-7984-4474-a7e1-5afb082cec59; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1599824325; sensorsdata2015session=%7B%7D; LG_HAS_LOGIN=1; _putrc=1B037A690EDDACA3; login=true; unick=%E7%9F%B3%E9%AB%98%E6%9E%97; index_location_city=%E6%88%90%E9%83%BD; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1600344497; LGRID=20200917200824-e7543659-4bde-484c-9230-fc17fcde24fd; LG_LOGIN_USER_ID=8df3b79f63417095aaa21aa665d8c3015221cf647551e2f2; X_HTTP_TOKEN=b68ef2109dee9a981611122061c3c54877206753ad; JSESSIONID=ABAAABAAAECABEHDAF6C3FBC3CD3F9E19833D38E1C36BB8; kw_login_authToken="ivgH0aod1i5gVQQ+mNALyqbVsLhlASf1sLII1lSNEhdjc0Ctzfe/Sx7FCl9kyZXzpWcSqzlHQnw1LrKFjIBdyZjIsmYtiBc2irph2doS/ciVHQ2GEo0IB9dY9CJIqzMWGlfPEvdx0F0DdeHhvOBwribKXJRqdqHCGcWiNjJugGd4rucJXOpldXhUiavxhcCELWDotJ+bmNVwmAvQCptcy5e7czUcjiQC32Lco44BMYXrQ+AIOfEccJKHpj0vJ+ngq/27aqj1hWq8tEPFFjdnxMSfKgAnjbIEAX3F9CIW8BSiMHYmPBt7FDDY0CCVFICHr2dp5gQVGvhfbqg7VzvNsw=="; gate_login_token=6ab82593587f37e8e539e1c6c4abe222948d6bd8094f36dd; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%228502478%22%2C%22first_id%22%3A%221750b3a4f763a2-05e508a994669a-5b472512-2073600-1750b3a4f779f6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2285.0.4183.83%22%7D%2C%22%24device_id%22%3A%221747cf5fb2c116-05754346412532-5b472512-2073600-1747cf5fb2d623%22%7D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
response = requests.get(url='https://edu.lagou.com', headers=headers)
print(response.text)
with open(file='lagou.html', mode='w', encoding='utf-8') as f:
    f.write(response.text)
