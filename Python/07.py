import urllib.request

url = "http://www.doubam.com/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
data = response.read()
data.decode()
print(data)
print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())
