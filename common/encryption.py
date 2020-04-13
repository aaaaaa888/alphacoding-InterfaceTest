
'''
封装各种加密方汨
hashlib pycryptodome 模块
'''

from hashlib import md5
from hashlib import sha1
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Cipher import DES
import binascii

def my_md5(msg):
    '''
    md5算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    '''
    m = md5()
    m.update(msg.encode('utf-8'))
    return m.hexdigest()

def my_sha1(msg):
    '''
    sha1算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    '''
    m = sha1()
    m.update(msg.encode('utf-8'))
    return m.hexdigest()

def my_sha256(msg):
    '''
    sha256算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    '''
    m = SHA256.new()
    m.update(msg.encode('utf-8'))
    return m.hexdigest()

def my_des(msg,key):
    '''
    DES算法加窑
    :param msg:需加密的字符锅,长变必须为8的倍数，不足添加'='
    :param key: 8个字符
    :return:加密后的字符
    '''
    de = DES.new(key,DES.MODE_ECB)
    mss = msg + (8 - (len(msg) % 8)) * '='
    text = de.encrypt(mss.encode())
    return binascii.b2a_hex(text).decode()

def my_aes_encrypt(msg,key,vi):
    '''
    AES算法加密
    # 密钥（key）, 密斯偏移量（vi） CBC模式加密
    :param msg:需加密的字符串
    :param key:长度必须为16,24,32位
    :param vi:必须为16位
    :return:加密后的字符
    '''
    ae = AES.new(key,AES.MODE_CBC,vi)
    txt = ae.encrypt(msg.encode())
    return binascii.b2a_hex(txt).decode()

def my_aes_decrypt(msg,key,vi):
    '''
    AES算法加密
    :param msg:需加密的字符串，长度需为16,24,32位
    :param key:长度必须为16,24,32位
    :param vi:必须为16位
    :return:解密后的字符
    '''
    mesg = binascii.b2a_hex(msg)
    ae = AES.new(key,AES.MODE_CBC,vi)
    return ae.decrypt(mesg).decode()

# aa = my_aes_encrypt('herish acorn','5c44c819appsapi0','01020304050607089')
# print(aa)
# print(my_aes_decrypt(aa,'5c44c819appsapi0','01020304050607089'))