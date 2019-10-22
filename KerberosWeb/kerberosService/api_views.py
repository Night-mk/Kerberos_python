# from django.shortcuts import render
# from models import *
# Create your views here.
from apifunc.socket import *
# import sys
# sys.path.append('D:\\python\\FZUKerberosweb\\FZUKerberos')
CRYPTO_TYPE='RC4'

'''
    注册接口: register
    {user, password}
'''
def register(data):
    print('test')
    username = data["user"]
    password = data['password']
    print('service: username[',username,'],[',password,']')

    result = {}
    rep=register_judge(username)
    if rep==0:
        salt=register_create(username,password)
        result={"status": "success", "salt":salt, "crypto_type": CRYPTO_TYPE}
    # 检查用户名是否在数据库中
    # try:
    #     u = User.objects.get(username = username)
    # 数据库没有此用户名，创建共享密钥
    else :
        result={"status": "false", "reason": "0"}
    
    '''
    if username!="guojun":
        # 生成共享密钥
        key = "flkaj932pj2230920923"
        # 数据库添加用户(name, pw_hash, Ekc)

        # 返回数据
        result={"status": "success", "key": key, "crypto_type": CRYPTO_TYPE}
    # 用户已存在
    if username=='guojun':
        result={"status": "false", "reason": "0"}
    '''
    
    return result

'''
    修改密码接口: figure_password
    {user, ori_password, new_password}
'''
def figure_password(data):
    username = data["user"]
    ori_password = data['ori_password']
    new_password = data['new_password']
    result={}
    if(register_judge(username)==1):
        if(revise_judge(username,ori_password)==1):
            salt=revise(username,new_password)
            result={"status": "success", "salt":salt, "crypto_type": CRYPTO_TYPE}
        else :
            result={"status": "false","reason": "1"}
    else :
        result={"status": "false","reason": "0"}
    # 检查用户和密码是否对应数据的数据
    
    # 是, 修改成新密码, 返回新共享密钥

    # 否, 返回错误

    return result

'''
    申请TGT票据接口: request_tgt
    {IDc, IDtgs, TS1}
'''
def request_tgt(data):
    IDc = data['IDc']
    IDtgs = data['IDtgs']
    TS1 = data['TS1']
    # username = json.loads(IDc)['username']
    username = IDc['username']
    # password = json.loads(IDc)['password']
    password = IDc['password']
    result={}
    if(register_judge(username)==1):
        if(revise_judge(username,password)==1):
            encrypt=tgt_create(username)
            result={"status": "success","encrypt":encrypt,"crypto_type": CRYPTO_TYPE}
        else:
            result={"status": "false","reason": "1"}
    else:
        result={"status": "false","reason": "0"}
    return result

'''
    用户-TGS票据服务器接口: request_tgs
    {IDo, IDv,ticket_tgs,auth}
'''
def request_tgs(data):
    print(data)
    result={}
    IDo = data['IDo']
    IDv = data['IDv']
    ticket_tgs = data['ticket_tgs']
    auth = data['auth']
    ticket_tgs_text=decrypt_RC4('Ektgs',ticket_tgs)
    print(ticket_tgs_text)
    auth_text=decrypt_RC4(json.loads(ticket_tgs_text)['Kc2tgs'],auth)
    print(auth_text)
    print(json.loads(ticket_tgs_text)['Kc2tgs'])
    print(json.loads(auth_text)['IDc'],json.loads(ticket_tgs_text)['username'])
    if(json.loads(auth_text)['IDc']==json.loads(ticket_tgs_text)['username']):
        username=json.loads(auth_text)['IDc']
        encrypt=tgs_create(username,IDo,IDv,ticket_tgs,auth)
        if encrypt==0:
            result={"status": "false","reason": "1"}
        else :
            result={"status": "success","encrypt":encrypt,"crypto_type": CRYPTO_TYPE}
    else:
        result={"status": "false","reason": "0"}
    return result

'''
    设置票据有效期接口: figure_lifetime
    {user,password,lifetime}
'''
def figure_lifetime(data):
    result={}
    user = data['user']
    password = data['password']
    lifetime = data['lifetime']
    if(admin_judge(user,password)==1):
        set_lifetime(lifetime)
        result={"status": "success"}
    else :
        result={"status": "false","reason": "0"}
'''
    设置票据有效期接口: figure_crypto
    {user,password,crypto_type}
'''
def figure_crypto(data):
    result={}
    user = data['user']
    password = data['password']
    crypto_type = data['crypto_type']
    if(admin_judge(user,password)==1):
        set_crypto_type(crypto_type)
        result={"status": "success"}
    else :
        result={"status": "false","reason": "0"}

'''
    AC添加数据到访问控制数据库接口: ac_add
'''
def ac_add(data):
    result={}
    ido = data['IDo']
    folder_name = data['data']['folder_name']
    files = data['data']['files']

    # 添加到数据库
    ac_add_database(ido,folder_name,files)
    print("complete add AC")


'''
    AC设置用户权限，修改用户在数据库中的权限接口: ac_set_permission
'''
def ac_set_permission(data):
    result={}
    ido = data['IDo']
    idc = data['IDc']
    permission = data["permission"]
    type1 = data["type"]
    valid_time = data["end_time"]
    folder_name = data['data']['folder_name']
    files = data['data']['files']
    
    ac_set_permission_database(ido,idc,permission,type1,valid_time,folder_name,files)
    
    print("complete set permission")


