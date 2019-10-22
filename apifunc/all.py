from mongoengine import *
import pymongo
from bson import json_util
import hashlib
from pbkdf2 import PBKDF2
import os
import hmac
import binascii
import json
import collections
import datetime
import secrets
import socket
import logging
import pickle
import base64
import time
import datetime
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
from Crypto import Random
import urllib.request
from urllib import parse
'''
    ====================================基础加密算法====================================
'''

'''
   =================密钥生成模块=================
'''
def key_generation(seed):
    """密钥生成函数
    Func:
        生成对称密钥，包括用户和服务器之间的密钥，和服务器与服务器之间的共享密钥

    Args:
        seed: 密钥种子

    Returns:
        salt: 密钥生成参数，盐值
        key: 对称密钥
    """
    ori_salt=os.urandom(8)
    salt =str(base64.b64encode(ori_salt))
    salt = salt[2:-1]
    # 64-bit salt
    key = PBKDF2(seed, ori_salt, iterations=1000, macmodule=hmac, digestmodule=hashlib.sha256).read(32) # 256-bit key
    key = str(base64.b64encode(key))
    key = key[2:-1]
    # 输出16进制数据\x..\x.., 转换为16进制可读形式
    # print(binascii.b2a_hex(key))
    # 转换16进制byte为字符串
    return salt,key

'''
    =================RC4加密，解密模块=================
'''
def encrypt_RC4(key = "init_key", message = "init_message"):
    """RC4加密函数
    Func:
        对明文进行RC4加密

    Args:
        key: 密钥
        message: 待加密的明文

    Returns:
        crypt: RC4加密密文
    """
    s_box = rc4_init_sbox_en(key)
    crypt = str(rc4_excrypt_en(message, s_box))
    return  crypt

def rc4_init_sbox_en(key):
    s_box = list(range(256))  # 我这里没管秘钥小于256的情况，小于256不断重复填充即可
    # print("原来的 s 盒：%s" % s_box)
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    #print("混乱后的 s 盒：%s"% s_box)
    return s_box

def rc4_excrypt_en(plain, box):
    # print("调用加密程序成功。")
    res = []
    i = j = 0
    
    for s in plain:
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j]) % 256
        k = box[t]
        a=ord(s) ^ k
        one=int(a/16)
        two=a%16
        if one>9:
            one=one+ord('a')-10
        if one<10:
            one=one+ord('0')
        if two>9:
            two=two+ord('a')-10
        else:
            two=two+ord('0')
        res.append(chr(one))
        res.append(chr(two))
    #print("res用于加密字符串，加密后是：%res" %res)
    cipher = "".join(res)
    # print("加密后的字符串是：%s" %cipher)
    # print("加密后的输出(经过编码):")
    # print(str(base64.b64encode(cipher.encode('utf-8')), 'utf-8'))
    #return (str(base64.b64encode(cipher.encode('utf-8')), 'utf-8'))
# rc4_main("123456sh","123456sh")
    return cipher

def decrypt_RC4(key = "init_key", message = "init_message"):
    """RC4解密函数
    Func:
        对密文进行RC4解密

    Args:
        key: 密钥
        message: 密文

    Returns:
        crypt: RC4解密明文
    """
    s_box = rc4_init_sbox_de(key)
    crypt = rc4_excrypt_de(message, s_box)
    return crypt
def rc4_init_sbox_de(key):
    s_box = list(range(256))  # 我这里没管秘钥小于256的情况，小于256不断重复填充即可
    # print("原来的 s 盒：%s" % s_box)
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
   # print("混乱后的 s 盒：%s"% s_box)
    return s_box
def rc4_excrypt_de(plain, box):
    # print("调用解密程序成功。")
    #plain = base64.b64decode(plain.encode('utf-8'))
    #plain = bytes.decode(plain)
    res = []
    plainb = ''
    b=0
    sum=0
    for i in plain:
        if b%2==1:
            if(ord(i)>=ord('a')):
                two=ord(i)-ord('a')+10
            if(ord(i)<ord('a')):
                two=ord(i)-ord('0')
            sum+=two
            plainb+=chr(sum)
            b+=1
            sum=0
            continue
        if b%2==0:
            if(ord(i)>=ord('a')):
                one=ord(i)-ord('a')+10
            if(ord(i)<ord('a')):
                one=ord(i)-ord('0')
            sum+=16*one
            b+=1
    i = j = 0
    for s in plainb:
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j]) % 256
        k = box[t]
        res.append(chr(ord(s) ^ k))
    # print("res用于解密字符串，解密后是：%res" %res)
    cipher = "".join(res)
     #print("解密后的字符串是：%s" %cipher)
     #print("解密后的输出(没经过任何编码):")
    return  cipher


'''
    =================3DES加密，解密模块=================
'''
def pkcs7padding(text):
    """PKCS7填充函数
    Func:
        对字符串进行PKCS7填充，用于3DES和AES算法

    Args:
        text: 加密之前的字符串

    Returns:
        text + padding_text: 处理填充之后的字符串
    """
    bs = DES3.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text

def pkcs7unpadding(text):
    """PKCS7去填充函数
    Func:
        对字符串进行PKCS7去填充，用于3DES和AES算法

    Args:
        text: 解密后的字符串

    Returns:
        text[0:length-unpadding]: 处理填充之后的字符串
    """
    length = len(text)
    unpadding = ord(text[length-1])
    return text[0:length-unpadding]

def encrypt_DES3(key, content):
    """3DES加密函数
    Func:
        3DES加密，模式cbc，填充pkcs7

    Args:
        key: 密钥
        content: 加密明文

    Returns:
        result: 3DES加密密文
    """
    key_byte = key[:24]
    iv = key_byte[:DES3.block_size] #DES3.block_size==8
    # print(key_byte)
    cipher_encrypt = DES3.new(key_byte, DES3.MODE_CBC, iv)
    # plaintext = 'sona si latine loqueri  ' #padded with spaces so than len(plaintext) is multiple of 8
    # 填充
    content_padding = pkcs7padding(content)
    # 加密
    encrypt_bytes = cipher_encrypt.encrypt(bytes(content_padding, encoding='utf-8'))
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result


def decrypt_DES3(key, cipertext):
    """3DES解密函数
    Func:
        3DES解密，模式cbc，填充pkcs7

    Args:
        key: 密钥
        cipertext: 密文

    Returns:
        result: 3DES解密明文
    """
    key_byte = key[:24]
    iv = key_byte[:DES3.block_size] #DES3.block_size==8
    cipher_decrypt = DES3.new(key_byte, DES3.MODE_CBC, iv) #you can't reuse an object for encrypting or decrypting other data with the same key.
    # cipher_decrypt.decrypt(cipertext)
     # base64解码
    encrypt_bytes = base64.b64decode(cipertext)
    # 解密
    decrypt_bytes = cipher_decrypt.decrypt(encrypt_bytes)
    # 重新编码
    result = str(decrypt_bytes, encoding='utf-8')
    # 去除填充内容
    result = pkcs7unpadding(result)
    return result

'''
    =================AES加密，解密模块=================
'''
def encrypt_AES(key, content):
    """AES加密函数
    Func:
        AES加密，模式cbc，填充pkcs7，key,iv使用同一个

    Args:
        key: 密钥
        content: 加密明文

    Returns:
        result: AES加密密文
    """
    # key_bytes = bytes(key, encoding='utf-8')
    # iv = key_bytes[:16]
    key_bytes = key
    iv = key_bytes[:AES.block_size]
    # print(iv)
    # iv = Random.new().read(AES.block_size)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # 处理明文
    content_padding = pkcs7padding(content)
    # 加密
    encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    print(base64.b64encode(encrypt_bytes))
    # 重新编码
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result

def decrypt_AES(key, cipertext):
    """AES解密函数
    Func:
        AES解密，模式cbc，填充pkcs7，key,iv使用同一个

    Args:
        key: 密钥
        cipertext: 密文

    Returns:
        result: AES解密明文
    """
    # key_bytes = bytes(key, encoding='utf-8')
    # iv = key_bytes[:16]
    key_bytes = key
    iv = key_bytes[:AES.block_size]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # base64解码
    encrypt_bytes = base64.b64decode(cipertext)
    # 解密
    decrypt_bytes = cipher.decrypt(encrypt_bytes)
    # 重新编码
    result = str(decrypt_bytes, encoding='utf-8')
    # 去除填充内容
    result = pkcs7unpadding(result)
    return result

'''
    ====================================基础加密算法END====================================
'''


'''
    ====================================接口底层函数====================================
'''

'''
    =================用户身份管理模块=================
'''

def register_create(c,pw):
    """注册信息生成函数
    Func:
        对注册的用户生成密钥，并记录用户信息

    Args:
        c: 用户id
        pw: 用户口令的哈希值

    Returns:
        salt: 生成密钥的盐值 
    """
    disconnect()  
    #断开数据库连接
    connect('IDdata', host='localhost', port=27017) 
    #连接用户信息数据库
    salt,key=key_generation(pw)  
    #生成盐值和密钥，其中盐值和密钥为base64编码
    class cred(Document):
        name=StringField(required=True, max_length=50) 
        pw_hash=StringField(required=True, max_length=80)
        Ekc=StringField(required=True, max_length=80)
        salt=StringField(required=True, max_length=40)
    cred1 = cred(
        name=c,
        pw_hash=pw,
        Ekc=key,
        salt=salt
    )
    cred1.save()
    #数据库添加操作
    return salt
    
def register_judge(c):
    """用户名查询函数
    Func:
        查询用户是否已经注册

    Args:
        c: 用户id

    Returns:
        查询结果,0:用户不存在，1:用户已存在 
    """
    disconnect()
    #断开数据库连接
    connect('IDdata', host='localhost', port=27017)
    class cred(Document):
        name=StringField(required=True, max_length=50)
        pw_hash=StringField(required=True, max_length=80)
        Ekc=StringField(required=True, max_length=80)
        salt=StringField(required=True, max_length=40)
    
    uk_users = cred.objects(name=c)
    #查询用户名，返回数据库信息
    if len(uk_users) == 0:
        return 0
    #若用户名不存在，返回值为0
    else :
        return 1
        
def revise_judge(c,pw):
    """用户确认函数
    Func:
        查询确认用户身份

    Args:
        c: 用户id
        pw: 用户口令的哈希值

    Returns:
        查询结果,0:用户密码错误，1:用户身份确认
    """
    #用户名判断修改，输入值为用户名和加密后的密码
    disconnect()
    #断开数据库连接
    connect('IDdata', host='localhost', port=27017)
    class cred(Document):
        name=StringField(required=True, max_length=50)
        pw_hash=StringField(required=True, max_length=80)
        Ekc=StringField(required=True, max_length=80)
        salt=StringField(required=True, max_length=40)
    uk_users= cred.objects(name=c)
    #查询用户名，返回数据库信息
    for i in uk_users:
        if i.pw_hash==pw:
            return 1
    #如果密码与数据库匹配，返回值为1
        else :
            return 0

def admin_judge(c,pw):
    """管理员登陆信息判断
    Func:
        查询确认管理员身份

    Args:
        c: 管理员id
        pw: 管理员口令的哈希值

    Returns:
        查询结果,0:管理员查询错误，1:管理员身份确认
    """
    #管理员信息判断，输入值为用户名和加密后的密码
    disconnect()
    #断开数据库连接
    connect('admindata', host='localhost', port=27017)
    class cred(Document):
        name=StringField(required=True, max_length=50)
        pw_hash=StringField(required=True, max_length=80)
    uk_users= cred.objects(name=c)
    #查询管理员名称，返回数据库信息
    for i in uk_users:
        if i.pw_hash==pw:
    #如果密码与数据库匹配，返回值为1
            return 1
        else :
            return 0

def revise(c,new_pw):
    """密码修改函数
    Func:
        对注册的用户的密码进行更改，生成新密钥，并更新用户信息

    Args:
        c: 用户id
        pw: 用户新口令的哈希值

    Returns:
        salt: 新生成密钥的盐值
    """
    #密码修改函数，用户名判断修改，输入值为用户名和加密后的新密码
    disconnect()
    #断开数据库连接
    connect('IDdata', host='localhost', port=27017)
    class cred(Document):
        name=StringField(required=True, max_length=50)
        pw_hash=StringField(required=True, max_length=80)
        Ekc=StringField(required=True, max_length=80)
        salt=StringField(required=True, max_length=40)
    salt,key=key_generation(new_pw)
    #生成盐值和密钥，其中盐值和密钥为base64编码
    uk_users = cred.objects(name=c)
    #查询用户名，返回数据库信息
    for i in uk_users:
        i.pw_hash=new_pw
        i.Ekc=key
        i.salt=salt
        i.save()
        #数据库更新
    return salt

'''
    =================用户身份管理模块END=================
'''

'''
    =================TGT,TGS票据模块=================
'''
def tgt_create(username):
    """TGT票据生成函数
    Func:
        生成TGT

    Args:
        username: 用户id

    Returns:
        TGT: 加密后的TGT票据
    """
    #tgt生成函数，输入为用户名
    t = time.time()
    now=int(round(t * 1000))
    #获取当前时刻毫秒数
    Lifetime=0
    
    CRYPTO_TYPE=''
    
    disconnect()
    #断开数据库连接
    connect('admindata', host='localhost', port=27017)
    #连接管理员信息数据库
    class set_1(Document):
        Lifetime=StringField(required=True, max_length=80)
        CRYPTO_TYPE=StringField(required=True, max_length=10)
    set_users = set_1.objects()
    for u in set_users:
        Lifetime=int(u.Lifetime)
        CRYPTO_TYPE=u.CRYPTO_TYPE
    #获取tgt有效期Lifetime和加密方式CRYPTO_TYPE
    disconnect()
    #断开数据库连接
    connect('IDdata', host='localhost', port=27017)
    #连接用户信息数据库
    class cred(Document):
        name=StringField(required=True, max_length=50)
        pw_hash=StringField(required=True, max_length=80)
        Ekc=StringField(required=True, max_length=80)
        salt=StringField(required=True, max_length=40)
    uk_users = cred.objects(name=username)
    #查询用户名，返回数据库信息
    for i in uk_users:
        kdc_req_body = {}
        
        kdc_req_body['username'] = username
        
        kdc_req_body['TS2'] = now
        #TS2为当前时间
        hash=hashlib.sha256()
        hash.update(bytes(str(secrets.randbits(31)),encoding='utf-8'))
        #生成31bit随机数
        kdc_req_body['Kc2tgs'] = hash.hexdigest()
        #转化为hash值，存入tgt中的Kc2tgs
        kdc_req_body['lefttime2'] = Lifetime
        
        Ticket_tgs_file=json.dumps(kdc_req_body)
        #使用json的dumps函数进行json格式处理
        if (CRYPTO_TYPE=='RC4'):
        #判断加密方式，后续可进行封装
            Ticket_tgs=encrypt_RC4('Ektgs',Ticket_tgs_file)
        
        elif (CRYPTO_TYPE=='3DES'):
            
            Ticket_tgs=encrypt_DES3('Ektgs',Ticket_tgs_file)
        
        elif (CRYPTO_TYPE=='AES'):
            
            Ticket_tgs=encrypt_AES('Ektgs',Ticket_tgs_file)
        #生成加密后的Ticket
        first_TGT={}
        TGT={}
        
        first_TGT['Kc2tgs']=kdc_req_body['Kc2tgs']
        
        first_TGT['TS2']=kdc_req_body['TS2']
        
        first_TGT['lefttime2']=kdc_req_body['lefttime2']
        
        first_TGT['Ticket_tgs']=Ticket_tgs

        first_TGT_file=json.dumps(first_TGT)
        #json格式处理
        if (CRYPTO_TYPE=='RC4'):
            TGT=encrypt_RC4(i.Ekc,first_TGT_file)
        elif (CRYPTO_TYPE=='3DES'):
            TGT=encrypt_DES3(i.Ekc,first_TGT_file)
        elif (CRYPTO_TYPE=='AES'):
            TGT=encrypt_AES(i.Ekc,first_TGT_file)
    #生成加密后的TGT
    return TGT

def creat_Authenticator_c(username,IDo,Kc2tgs,TS3= None):
    """用户身份认证信息生成函数（authenticator）
    Func:
        生成用户身份认证信息

    Args:
        username: 用户id
        IDo: 版权方名称
        Kc2tgs: 从TGT中获取的用于通信的密钥Kc2tgs
        TS3: 时间戳

    Returns:
        Authenticator_c: 用户身份认证信息
        Authenticator_c_body['TS3']: 时间戳
    """
    #该函数为用户身份验证生成函数，输入为用户名，版权方名称，从TGT中获取的用于通信的密钥Kc2tgs
    #返回值作为下一步TGS请求的输入值，该操作在前端实现，在Kerberos端仅作为测试使用
    t = time.time()
    now=int(round(t * 1000))
    #获取当前时刻毫秒数
    Authenticator_c_body={}
    
    Authenticator_c_body['username']=username
    
    Authenticator_c_body['IDo']=IDo
    
    Authenticator_c_body['TS3']=now
    
    Authenticator_c_body_file=json.dumps(Authenticator_c_body)
    #使用json的dumps函数进行json格式处理
    Authenticator_c=encrypt_RC4(Kc2tgs,Authenticator_c_body_file)
    #对dict进行加密，生成加密后的用户身份验证信息
    #此处为RC4加密方式，测试时可根据实际情况选取加密函数
    return Authenticator_c,Authenticator_c_body['TS3']
    #返回用户身份验证信息与生成时刻毫秒数

def tgs_create(username,IDO, IDV, Ticket_tgs,Authenticator_c):
    """TGS票据生成函数
    Func:
        为用户生成TGS票据

    Args:
        username: 用户id
        IDo: 版权方名称
        IDV: 云平台id
        Ticket_tgs: TGT中获取的Ticket_tgs
        Authenticator_c: 用户认证信息

    Returns:
        TGS: 生成的TGS票据
    """
    #该函数为tgs生成函数，输入为用户名username，版权方名称IDO，云平台号IDV，从TGT中获取的Ticket_tgs,用户验证信息Authenticator_c
    t = time.time()
    now=int(round(t * 1000))
    #获取当前时刻毫秒数
    Lifetime=0
    CRYPTO_TYPE=''
    
    disconnect()
    #断开数据库连接
    connect('admindata', host='localhost', port=27017)
    #连接管理员信息数据库
    class set_1(Document):
        Lifetime=StringField(required=True, max_length=80)
        CRYPTO_TYPE=StringField(required=True, max_length=10)
    set_users = set_1.objects()
    
    for u in set_users:
        Lifetime=int(u.Lifetime)
        CRYPTO_TYPE=u.CRYPTO_TYPE
    #获取tgt有效期Lifetime和加密方式CRYPTO_TYPE
    disconnect()
    #断开数据库连接
    connect('IDdata', host='localhost', port=27017)
    #连接用户信息数据库
    class cred(Document):
        name=StringField(required=True, max_length=50)
        pw_hash=StringField(required=True, max_length=80)
        Ekc=StringField(required=True, max_length=80)
        salt=StringField(required=True, max_length=40)
    
    uk_users = cred.objects(name=username)
    #查询用户名，返回数据库信息
    for i in uk_users:
        Ticket_tgs_body=Ticket_tgs
        #该值为加密状态下的Ticket
        if (CRYPTO_TYPE=='RC4'):
            TGT=decrypt_RC4(i.Ekc,Ticket_tgs_body)
        
        elif (CRYPTO_TYPE=='3DES'):
            TGT=decrypt_DES3(i.Ekc,Ticket_tgs_body)
        
        elif (CRYPTO_TYPE=='AES'):
            TGT=decrypt_AES(i.Ekc,Ticket_tgs_body)
        #进行解密，获取Ticket中的信息
        kdc_req_body = {}#IDO,IDV,Ticket_tgs,Authenticator_c
        kdc_req_body['IDo'] = IDO 
        kdc_req_body['IDv'] = IDV
        kdc_req_body['Ticket_tgs'] = Ticket_tgs
        kdc_req_body['Authenticator_c'] = Authenticator_c
        
        Ticket_tgs_body_file={}
        
        if (CRYPTO_TYPE=='RC4'):
            Ticket_tgs_body_file=decrypt_RC4('Ektgs',Ticket_tgs)
        elif (CRYPTO_TYPE=='3DES'):
            Ticket_tgs_body_file=decrypt_DES3('Ektgs',Ticket_tgs)
        elif (CRYPTO_TYPE=='AES'):
            Ticket_tgs_body_file=decrypt_AES('Ektgs',Ticket_tgs)
        
        Ticket_tgs_body={}#IDC,TS2,Kc2tgs,lefttime2
        
        Ticket_tgs_body=json.loads(Ticket_tgs_body_file)
        #使用loads函数进行json格式处理
        if now > (Ticket_tgs_body['TS2'] + Lifetime):
            return 0
        #若超时，返回0
        Authenticator_c_body_file={}
        Authenticator_c_body={}#IDC,IDO,TS3
        
        if (CRYPTO_TYPE=='RC4'):
            Authenticator_c_body_file=decrypt_RC4(Ticket_tgs_body['Kc2tgs'],kdc_req_body['Authenticator_c'])
        elif (CRYPTO_TYPE=='3DES'):
            Authenticator_c_body_file=decrypt_DES3(Ticket_tgs_body['Kc2tgs'],kdc_req_body['Authenticator_c'])
        elif (CRYPTO_TYPE=='AES'):
            Authenticator_c_body_file=decrypt_AES(Ticket_tgs_body['Kc2tgs'],kdc_req_body['Authenticator_c'])
        #根据Ticket中获取的Kc2tgs，对用户验证信息Authenticator_c进行解密
        Authenticator_c_body=json.loads(Authenticator_c_body_file)
        #使用loads函数进行json格式处理
        Ticket_v_body={}#Kcv,IDC,IDO,IDV,TS4,lifetime4,ACc
        
        hash=hashlib.sha256()
        hash.update(bytes(str(secrets.randbits(31)),encoding='utf-8'))
        #生成31bit随机数
        Ticket_v_body['Kcv']=hash.hexdigest()
        #转化为hash值，存入Ticket_v中的Kcv
        Ticket_v_body['username']=Ticket_tgs_body['username']
        Ticket_v_body['IDo']=Authenticator_c_body['IDo']
        Ticket_v_body['IDv']=kdc_req_body['IDv']
        Ticket_v_body['TS4']=now
        Ticket_v_body['lifetime4']=Lifetime
        Ticket_v_body['ACc']=''
        Ticket_v_file=json.dumps(Ticket_v_body)
        #Ticket_v赋值，使用dumps函数进行json格式处理
        if (CRYPTO_TYPE=='RC4'):
            Ticket_v=encrypt_RC4('3',Ticket_v_file)
        
        elif (CRYPTO_TYPE=='3DES'):
            Ticket_v=encrypt_DES3('3',Ticket_v_file)
        
        elif (CRYPTO_TYPE=='AES'):
            Ticket_v=encrypt_AES('3',Ticket_v_file)
        
        TGS_body={}#Kcv,IDO,IDV,TS4,Ticket_v
        TGS_body['Kcv']=Ticket_v_body['Kcv']
        TGS_body['IDo']=Ticket_v_body['IDo']
        TGS_body['IDv']=Ticket_v_body['IDv']
        TGS_body['TS4']=Ticket_v_body['TS4']
        TGS_body['Ticket_v']=Ticket_v
        TGS_body_file=json.dumps(TGS_body)
        #TGS赋值，使用dumps函数进行json格式处理
        if (CRYPTO_TYPE=='RC4'):
            TGS=encrypt_RC4(Ticket_tgs_body['Kc2tgs'],TGS_body_file)
        
        elif (CRYPTO_TYPE=='3DES'):
            TGS=encrypt_DES3(Ticket_tgs_body['Kc2tgs'],TGS_body_file)
        
        elif (CRYPTO_TYPE=='AES'):
            TGS=encrypt_AES(Ticket_tgs_body['Kc2tgs'],TGS_body_file)
        #区块链上链
        #将用户申请信息发送到区块链端
        url = 'http://192.168.1.130:8090/kerberosService/api'
        block_key ={
            'IDc':username,
            'IDo':IDO
        }
        
        block_value ={
            'IDo':IDO,
            'encrypted_value':TGS,
            'applytime':Ticket_v_body['TS4'],
            'lifetime':Lifetime
        }
        
        block_send={
            'key':json.dumps(block_key),
            'value':json.dumps(block_value)
        }
        
        data = parse.urlencode(block_send).encode("utf-8")
        #response = urllib.request.urlopen(url,data)
        urllib.request.urlopen(url,data)
        #print("BC res: ",response)
        
    return TGS

'''
    =================TGT,TGS票据模块END=================
'''


'''
    =================系统设置模块=================
'''

def set_lifetime(lifetime):
    """设置票据有效期函数
    Func:
        设置票据有效期

    Args:
        lifetime: 有效期时间(单位毫秒)

    Returns:
        0: 设置成功
    """
    #票据有效期设置，输入值为时间值(单位毫秒)
    disconnect()
    #断开数据库连接
    connect('admindata', host='localhost', port=27017)
    #连接管理员数据库
    class set_1(Document):
        Lifetime=StringField(required=True, max_length=80)
        CRYPTO_TYPE=StringField(required=True, max_length=10)
    set_users = set_1.objects()
    #获取当前数据库信息
    for u in set_users:
        u.Lifetime = lifetime
        u.save()
    #更新数据库信息
    return 0
    
def set_crypto_type(crypto_type):
    """设置票据有效期函数
    Func:
        设置票据有效期

    Args:
        lifetime: 有效期时间(单位毫秒)

    Returns:
        0: 设置成功
    """
    #加密方式设置，输入值为加密方式(字符串)
    disconnect()
    #断开数据库连接
    connect('admindata', host='localhost', port=27017)
    #连接管理员数据库
    class set_1(Document):
        Lifetime=StringField(required=True, max_length=80)
        CRYPTO_TYPE=StringField(required=True, max_length=10)
    set_users = set_1.objects()
    #获取当前数据库信息
    for u in set_users:
        u.CRYPTO_TYPE = crypto_type
        u.save()
    #更新数据库信息
    return 0

'''
    =================系统设置模块END=================
'''


'''
    =================访问控制矩阵处理模块=================
'''

def ac_add_database(ido,folder_name,files):
    """版权文件权限添加函数
    Func:
        为版权文件添加权限，并添加到数据库
        权限参数说明: 
        folder_permission: "1"表示全部权限都一致，"0"表示有差异
        permission: [1,1,1]表示全部权限
        valid_time: null表示没有时间限制

    Args:
        ido: 版权方
        folder_name: 版权文件所在文件夹名称
        files: 需要设置权限的版权文件名称

    Returns:
        0: 版权添加成功
    """
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    # 数据库名称
    mydb = myclient['ACdata']
    # ido_folder 表名称
    folder_table = mydb["ido_folder"]
    '''
        ido_folder数据库添加数据
    '''
    ido_folder_data = {
        "IDc": ido,
        "IDo": ido,
        "file_folder": folder_name,
        "folder_permission": "1"
    }
    # 判断数据是否存在
    if folder_table.count_documents(ido_folder_data) == 0:
        # 数据不存在再插入
        folder_table.insert_one(ido_folder_data)


    '''
        file_table数据库添加数据
    '''
    file_table =  mydb[folder_name+"_table"]
    idc_file_data = []
    for file in files: 
        data = {
            "IDc": ido,
            "file_name": file,
            "permission": [1,1,1],
            "valid_time": "null"
        }
        idc_file_data.append(data)
    # 插入数据
    file_table.insert_many(idc_file_data)

    return 0


def ac_set_permission_database(ido,idc,permission,type1,valid_time,folder_name,files):
    """版权文件权限设置函数
    Func:
        为版权文件设置权限，设置用户对于文件夹和文件的权限，并对数据库进行处理
        权限参数说明：
        file_permission: 文件权限
        {
            [0,0,0]: 无权限
            [0,0,1]: 读权限
            [0,1,0]: 写权限
            [0,1,1]: 读写权限
            [1,1,1]: 所有权限（版权方所有）
        }

    Args:
        ido: 版权方id
        idc: 用户id
        permission: 权限
        type1: 设置权限的种类,folder:设置文件夹权限，others:设置文件权限
        valid_time: 版权有效时间
        folder_name: 版权文件夹名称
        files: 版权文件名称

    Returns:
        0: 版权设置成功
    """
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    # 数据库名称
    mydb = myclient['ACdata']
    
    '''
        ido_folder设置权限
    '''
    # ido_folder 表名称
    folder_table = mydb["ido_folder"]
    # 设置文件夹权限
    folder_permission = "0"
    if type1=="folder":
        folder_permission="1"
    
    ido_folder_data = {
        "IDc": idc,
        "IDo": ido,
        "file_folder": folder_name,
        "folder_permission": folder_permission
    }
    # 判断数据是否存在
    if folder_table.count_documents({"IDc": idc,"IDo": ido,"file_folder": folder_name}) == 0:
        # 数据不存在再插入
        folder_table.insert_one(ido_folder_data)
    else: 
        # 更新文件夹
        myquery = {"IDc": idc,"IDo": ido,"file_folder": folder_name}
        newvalues = { "$set": { "folder_permission": folder_permission } }
        folder_table.update_one(myquery, newvalues)

    '''
        file_table设置权限
        每个数据分开处理
    '''
    file_table =  mydb[folder_name+"_table"]
    file_permission = [0,0,0]
    if permission=="01": #read
        file_permission = [0,0,1]
    elif permission=="10": # download
        file_permission = [0,1,0]
    elif permission=="11": # read&&download
        file_permission = [0,1,1]
    
    for file in files: 
        data = {
            "IDc": idc,
            "file_name": file,
            "permission": file_permission,
            "valid_time": valid_time
        }
        
        if file_table.count_documents({"IDc": idc,"file_name": file}) == 0:
            # 插入数据
            file_table.insert_one(data)
        else: 
            # 更新权限
            myquery = {"IDc": idc,"file_name": file}
            newvalues = { "$set": { "permission": file_permission, "valid_time": valid_time } }
            file_table.update_one(myquery, newvalues)
    
    print("complete set")
    return 0


def ac_get_permission(idc,ido):
    """版权文件权限获取函数
    Func:
        获取用户对于特定版权方的访问控制矩阵，获取权限

    Args:
        idc: 用户id
        ido: 版权方id

    Returns:
        ac_permission: 用户对某个版权方的访问控制矩阵
    """
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    # 数据库名称
    mydb = myclient['ACdata']
    
    folder_table = mydb["ido_folder"]

    ac_permission = dict()
    ac_permission["IDc"]=idc
    ac_permission["permission"]={}
    # ac_permission = {
    #     "IDc": idc
    # }

    # 根据idc,ido查询idc控制的所有文件夹名称
    controlled_folder = folder_table.find({"IDc": idc,"IDo": ido,})

    for folder in controlled_folder:
        folder_name = folder["file_folder"]
        file_table =  mydb[folder_name+"_table"]
        folder_permission = folder["folder_permission"]
        ac_permission["permission"][folder_name]={}

        #  权限相同的情况
        if folder_permission == "1":
            perm = file_table.find({"IDc": idc}).limit(1)[0]["permission"]
            # print(type(perm))
            perm.append(1)
            # 添加时间检查

            ac_permission["permission"][folder_name][folder_name]=perm
        # 权限不同的情况, 列出对每个文件的权限
        else: 
            files = file_table.find({"IDc": idc})
            ac_permission["permission"][folder_name][folder_name]=[0,0,0,0]
            # 循环添加每个文件的权限
            # 添加时间检查
            for file in files:
                perm = file["permission"]
                ac_permission["permission"][folder_name][file["file_name"]]=perm

    # 将字典转为json
    # ac_permission_json = json.dump(ac_permission)
    print(ac_permission)
    
    return ac_permission

'''
    =================访问控制矩阵处理模块END=================
'''

'''
    ====================================接口底层函数END====================================
'''