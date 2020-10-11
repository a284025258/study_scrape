from pyquery import PyQuery


doc = PyQuery(filename='./movie.html')
print(doc('title'))
