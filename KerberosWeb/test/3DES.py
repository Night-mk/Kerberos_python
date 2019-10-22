'''
    加密算法3DES
'''
from Crypto.Cipher import DES3
from Crypto import Random
import key_gen
import base64
# from Crypto.Util.Padding import pad, unpad
'''
    明文使用PKCS7填充
    最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    :param text: 待加密内容(明文)
    :return: text+padding
'''
def pkcs7padding(text):
    bs = DES3.block_size  # 16
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

# 加密3DES
def encrypt_3DES(key, content):
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

# 解密3DES
def decrypt_3DES(key, cipertext):
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

def test():
    # key=key_gen.key_generation("123456.")
    key = b'\x87\xe9\x11\xfe\x82\xce\x8dS\x08;9\xd2\xbfx\x03\x95\x15\x99\xc2\x02\x9c\xcb\xaa\xd7G\x16\xd8\xae\x157U\xdb'
    print('============3DES============')
    # 对英文加密
    source_en = 'Hello!'
    encrypt_en = encrypt_3DES(key, source_en)
    print('plaintext: ', source_en)
    print('cipertext: ',encrypt_en)
    # 对英文解密
    decrypt_en = decrypt_3DES(key, encrypt_en)
    print('decrypted plaintext: ', decrypt_en)
    print(source_en == decrypt_en)

    # 中英文混合加密
    source_mixed = 'Hello, 韩- 梅 -梅'
    encrypt_mixed = encrypt_3DES(key, source_mixed)
    print('plaintext: ', source_mixed)
    print('cipertext: ', encrypt_mixed)
    decrypt_mixed = decrypt_3DES(key, encrypt_mixed)
    print('decrypted plaintext: ', decrypt_mixed)
    print(decrypt_mixed == source_mixed)

    # 刚好16字节的情况
    en_16 = 'abcdefgj10124567'
    encrypt_en = encrypt_3DES(key, en_16)
    print('plaintext: ', en_16)
    print('cipertext: ', encrypt_en)
    decrypt_en = decrypt_3DES(key, encrypt_en)
    print('decrypted plaintext: ',decrypt_en)
    print(en_16 == decrypt_en)

    # 混合
    mix_16 = 'abx张三丰12sa'
    encrypt_mixed = encrypt_3DES(key, mix_16)
    print('plaintext: ', mix_16)
    print('cipertext: ', encrypt_mixed)
    decrypt_mixed = decrypt_3DES(key, encrypt_mixed)
    print('decrypted plaintext: ',decrypt_mixed)
    print(decrypt_mixed == mix_16)

test()