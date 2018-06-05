import requests

response = requests.get('http://www.baidu.com/')
content = response.content
print(content.decode())
