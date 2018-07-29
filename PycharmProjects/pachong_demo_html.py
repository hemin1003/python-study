import requests
import re

content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text

print(content)

# <div class ="grid-item work-thumbnail" >
# <a href = "http://www.cnu.cc/works/290746" class ="thumbnail" target="_blank" >
# <div class ="title" >花魁< / div >
# <div class ="author" >口< / div >

pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
print(results)

print('final result: ')
for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))