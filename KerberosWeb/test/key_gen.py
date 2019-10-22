'''
    密钥生成算法PBKDF2
'''
from pbkdf2 import PBKDF2
import os
import hmac
import hashlib
import binascii
# Crypto

# 密钥生成算法pbkdf2
seed
def key_generation(seed):
    salt = os.urandom(8)    # 64-bit salt
    print(salt)
    salt = b'\xa2\x9e\xa8\xd3\x9f\n\xe7\t'
    salt='h+kR/oLOjVMIOznSv3gDlRWZwgKcy6rXRxbYrhU3Vds='
    key = PBKDF2(seed, salt, iterations=1000, macmodule=hmac, digestmodule=hashlib.sha256).read(32) # 256-bit key
    # 输出16进制数据\x..\x.., 转换为16进制可读形式
    # print(binascii.b2a_hex(key))
    # 转换16进制byte为字符串
    print (str(binascii.b2a_hex(key), encoding = "utf-8"))
    print ('KEY: ', key)
    return key

# key_generation("kerberos_hadoop@401")
key_generation("AS_TGS@401")
