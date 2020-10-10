import requests


response = requests.get(url='https://kaiwu.lagou.com/course/courseInfo.htm?courseId=46#/detail/pc?id=1668')
print(requests.codes)
# exit() if not response.status_code == requests.codes.not_found else print('Request Successfully')
