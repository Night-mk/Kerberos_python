import base64
def rc4_main_en(key = "init_key", message = "init_message"):
    # print("RC4加密主函数")
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
def rc4_main_de(key = "init_key", message = "init_message"):
    # print("RC4解密主函数调用成功")
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
#print(rc4_main_en('123456','123456'))
#print(rc4_main_de('123456','31ca4d531105'))
'''import base64
def rc4_main_en(key = "init_key", message = "init_message"):
    # print("RC4加密主函数")
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
    # print("混乱后的 s 盒：%s"% s_box)
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
        res.append(chr(ord(s) ^ k))
    # print("res用于加密字符串，加密后是：%res" %res)
    cipher = "".join(res)
    # print("加密后的字符串是：%s" %cipher)
    # print("加密后的输出(经过编码):")
    # print(str(base64.b64encode(cipher.encode('utf-8')), 'utf-8'))
    return (str(base64.b64encode(cipher.encode('utf-8')), 'utf-8'))
# rc4_main("123456sh","123456sh")
def rc4_main_de(key = "init_key", message = "init_message"):
    # print("RC4解密主函数调用成功")
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
    plain = base64.b64decode(plain.encode('utf-8'))
    plain = bytes.decode(plain)
    res = []
    i = j = 0
    for s in plain:
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j]) % 256
        k = box[t]
        res.append(chr(ord(s) ^ k))
    # print("res用于解密字符串，解密后是：%res" %res)
    cipher = "".join(res)
    # print("解密后的字符串是：%s" %cipher)
    # print("解密后的输出(没经过任何编码):")
    return  cipher
	'''