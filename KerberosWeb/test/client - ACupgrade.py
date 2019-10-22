import json
import urllib.request
from urllib import parse
url = 'http://192.168.50.173:8080/kerberosService/api'
#这种嵌套json的格式需要把嵌套部分先json.dumps一下，服务器才能正确解析数据
file = {
	'folder_name':'vip_group',
	'files':['vip_money','vip_name','vip_data']
}

login_data = {
	'IDo':'bilibili',
    'user':'test',
	'permission':'10',
    'type':'folder',
	'end_time':'1566390556179',
    'data':json.dumps(file)
}


test_data = {
	'type':'ac_set_permission',
	'data':json.dumps(login_data)
}

print(test_data)
data = parse.urlencode(test_data).encode("utf-8")
print(type(data))
response = urllib.request.urlopen(url,data)
content = response.read().decode("utf-8")
result = json.loads(content)
print (result)