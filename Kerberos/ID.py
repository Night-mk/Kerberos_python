from mongoengine import *
import json
import pymongo
from bson import json_util
import hashlib
def id_decide(data1,data2):
	connect('IDdata', host='localhost', port=27017)
	c=data1
	pw=data2
	hash=hashlib.md5()
	hash.update(bytes(pw,encoding='utf-8'))
	
	class cred(Document):
		name=StringField(required=True, max_length=50)
		pw_hash=StringField(required=True, max_length=40)


	uk_users = cred.objects(name=c)

	for i in uk_users:
		if i.pw_hash==hash.hexdigest():
			return 1
		else :
			return 0