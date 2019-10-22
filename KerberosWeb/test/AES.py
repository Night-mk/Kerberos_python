'''
    加密算法AES
'''
import base64
from Crypto.Cipher import AES
import key_gen
from Crypto import Random

'''
    明文使用PKCS7填充
    最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    :param text: 待加密内容(明文)
    :return: text+padding
'''
def pkcs7padding(text):
    bs = AES.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text

'''
    处理使用PKCS7填充过的数据
    :param text: 解密后的字符串
    :return: 处理填充之后的字符串
'''
def pkcs7unpadding(text):
    length = len(text)
    unpadding = ord(text[length-1])
    return text[0:length-unpadding]


# 加密AES
'''
    AES加密
    key,iv使用同一个
    key的长度
    模式cbc
    填充pkcs7
    :param key: 密钥
    :param content: 加密内容
    :return:
'''
def encrypt_AES(key, content):
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

# 解密AES
'''
    AES解密
     key,iv使用同一个
    模式cbc
    去填充pkcs7
    :param key:
    :param cipertext:
    :return:
'''
def decrypt_AES(key, cipertext):
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

def test():
    # key=key_gen.key_generation("123456.")
    key=b'\x87\xe9\x11\xfe\x82\xce\x8dS\x08;9\xd2\xbfx\x03\x95\x15\x99\xc2\x02\x9c\xcb\xaa\xd7G\x16\xd8\xae\x157U\xdb'
    # key=b'1234567890qwertyuiopasdfghjklzxc'
    print('============AES============')
    # 对英文加密
    source_en = 'Hello!'
    encrypt_en = encrypt_AES(key, source_en)
    print('plaintext: ', source_en)
    print('cipertext: ',encrypt_en)
    # 对英文解密
    decrypt_en = decrypt_AES(key, encrypt_en)
    print('decrypted plaintext: ', decrypt_en)
    print(source_en == decrypt_en)

    # 中英文混合加密
    source_mixed = 'Hello, 韩- 梅 -梅'
    encrypt_mixed = encrypt_AES(key, source_mixed)
    print('plaintext: ', source_mixed)
    print('cipertext: ', encrypt_mixed)
    decrypt_mixed = decrypt_AES(key, encrypt_mixed)
    print('decrypted plaintext: ', decrypt_mixed)
    print(decrypt_mixed == source_mixed)

    # 刚好16字节的情况
    en_16 = 'abcdefgj10124567'
    encrypt_en = encrypt_AES(key, en_16)
    print('plaintext: ', en_16)
    print('cipertext: ', encrypt_en)
    decrypt_en = decrypt_AES(key, encrypt_en)
    print('decrypted plaintext: ',decrypt_en)
    print(en_16 == decrypt_en)

    # 混合
    mix_16 = 'abx张三丰12sa'
    encrypt_mixed = encrypt_AES(key, mix_16)
    print('plaintext: ', mix_16)
    print('cipertext: ', encrypt_mixed)
    decrypt_mixed = decrypt_AES(key, encrypt_mixed)
    print('decrypted plaintext: ',decrypt_mixed)
    print(decrypt_mixed == mix_16)

test()
