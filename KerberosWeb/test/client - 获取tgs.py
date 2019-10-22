import json
import urllib.request
from urllib import parse
url = 'http://192.168.1.106:8080/kerberosService/api'
#这种嵌套json的格式需要把嵌套部分先json.dumps一下，服务器才能正确解析数据
user1 = {
	'username':'jun',
	'password':'123'
}

'''
login_data = {
	'IDc':json.dumps(user1),
	'IDtgs':'0',
	'TS1':'2019-07-29 08:24:56'
}
'''

login_data = {
	'IDo':'bilibili',
	'IDv':'0',
	'ticket_tgs':'b2f8a4116f729ac443dcbe0063b48f0b9bf014b9a0d6265d28469f3b79b4115bf9da2a18eba94b26055d0e8ca0d0860930dde98af7f50173c54d41330aa5c4544c9c2058e040b815f2c29fc6d157adbb389953f1a95fceb89f96a3906f2b710a41f7c5be373f5d4d39160290614ae13b54fda2a2a57b40529bfdf78f7724fb6273ba634ecb23e9c249ebd538',
	'auth':'820e34322425f2c2f6c24988bf91b8da52246d79bfb014b97515d1bf00030aa3d45341b5e4c7fae9e0c6478aea000ce9c08885214b2db42b394fce24'
}

test_data = {
	'type':'request_tgs',
	'data':json.dumps(login_data)
}

print(test_data)
data = parse.urlencode(test_data).encode("utf-8")
print(data)
response = urllib.request.urlopen(url,data)
content = response.read().decode("utf-8")
result = json.loads(content)
print (result)