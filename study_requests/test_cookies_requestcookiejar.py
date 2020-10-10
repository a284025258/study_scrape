import requests


cookies = 'p_h5_u=D6FE897A-56AB-41B2-BC74-84D788446B0B; _ga=GA1.2.1422460404.1599824325; user_trace_token=20200911193846-8357cabc-0f9f-40db-ac2c-db8d334e04b2; LGUID=20200911193846-c7771dd1-7984-4474-a7e1-5afb082cec59; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1599824325; sensorsdata2015session=%7B%7D; LG_HAS_LOGIN=1; _putrc=1B037A690EDDACA3; login=true; unick=%E7%9F%B3%E9%AB%98%E6%9E%97; index_location_city=%E6%88%90%E9%83%BD; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1600344497; LGRID=20200917200824-e7543659-4bde-484c-9230-fc17fcde24fd; LG_LOGIN_USER_ID=8df3b79f63417095aaa21aa665d8c3015221cf647551e2f2; X_HTTP_TOKEN=b68ef2109dee9a987339222061c3c54877206753ad; JSESSIONID=ABAAABAAAECABEH9203DCF7829DDDE411533A3691B74117; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221750d05e8dd534-0209cafd8f8611-5b472512-2073600-1750d05e8de918%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2285.0.4183.83%22%7D%2C%22%24device_id%22%3A%221747cf5fb2c116-05754346412532-5b472512-2073600-1747cf5fb2d623%22%7D; kw_login_authToken="fkwcMpvfT9p8WYf9xYH02xtCfBuUOojgXoHqdIxxDQAR125yCG8wedm3ZUNQEbivW/VWzoseCHACXVZBpBcnuzRz5P1MBTNnspj3uTZ2lW2qjjRUlFoM3DwVBInxMa+eCLvW5pOJ0giHYlFavHV0WNjcCsOd69HGXKfmUOT2cYZ4rucJXOpldXhUiavxhcCELWDotJ+bmNVwmAvQCptcy5e7czUcjiQC32Lco44BMYXrQ+AIOfEccJKHpj0vJ+ngq/27aqj1hWq8tEPFFjdnxMSfKgAnjbIEAX3F9CIW8BSiMHYmPBt7FDDY0CCVFICHr2dp5gQVGvhfbqg7VzvNsw=="; gate_login_token=6ab82593587f37e8e539e1c6c4abe222948d6bd8094f36dd'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
response = requests.get(url='https://edu.lagou.com', headers=headers, cookies=jar)
print(response.text)
