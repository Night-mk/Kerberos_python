import json
import urllib.request
from urllib import parse
url = 'http://localhost:8080/kerberosService/api'
#这种嵌套json的格式需要把嵌套部分先json.dumps一下，服务器才能正确解析数据

login_data = {
	'user':'admin',
	'password':'8a7cb6a4bd37cb8da4f1aa5a9d9e24482c1fe61c5b55734ccc07bf5645b268fe',
	'crypto_type':'RC4'
}



test_data = {
	'type':'figure_crypto',
	'data':json.dumps(login_data)
}

print(test_data)
data = parse.urlencode(test_data).encode("utf-8")
print(data)
response = urllib.request.urlopen(url,data)
content = response.read().decode("utf-8")
result = json.loads(content)
print (result)