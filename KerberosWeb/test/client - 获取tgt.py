import json
import urllib.request
from urllib import parse
url = 'http://192.168.1.106:8080/kerberosService/api'
#这种嵌套json的格式需要把嵌套部分先json.dumps一下，服务器才能正确解析数据
user1 = {
	'username':'jun',
	'password':'123'
}

login_data = {
	'IDc':json.dumps(user1),
	'IDtgs':'0',
	'TS1':'2019-07-29 08:24:56'
}



test_data = {
	'type':'request_tgt',
	'data':json.dumps(login_data)
}

print(test_data)
data = parse.urlencode(test_data).encode("utf-8")
print(data)
response = urllib.request.urlopen(url,data)
content = response.read().decode("utf-8")
result = json.loads(content)
print (result)