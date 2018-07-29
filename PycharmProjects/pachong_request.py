# requests库的使用

# get请求
import requests
url = 'http://httpbin.org/get'
data = {'key':'value'}
response = requests.get(url,data)
# 字典类型的data不用额外处理，返回数据也不用管编码问题
print(response.text)

# post请求
import requests
url = 'http://httpbin.org/post'
data = {'key':'value'}
response = requests.post(url, data)
# 返回类型为json类型
print(response.json())