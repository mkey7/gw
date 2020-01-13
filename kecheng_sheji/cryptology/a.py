#英文使用utf-8 转换成16进制hex字符串的方法

newstr = 'asd'
b_str = bytes(newstr,encoding='utf-8')
print(b_str)
hex_str = b_str.hex() #将bytes类型转换成16进制的hex字符串
print(hex_str) #字节码转16进制hex的方法
print(bytes.fromhex(hex_str).decode('utf-8')) #将16进制hex字符串转换成bytes,然后在转换成字符串
print(type('中文'.encode('utf-8')),'中文'.encode('unicode_escape'),'中文123456'.encode('unicode_escape').decode('utf-8'))

#中文转换成Unicode的一种方法之一
u_str = '中文123456'
b_str = bytes(u_str,encoding='unicode_escape')
h_u_s = b_str.hex()
print ("\u4e2d\u6587") #Unicode编码可直接输出
#中文使用Unicode转换成bytes再转换成16进制hex方法 包含英文和数字
u_cn = '中文asd123'
hex_msg = bytes(u_cn,encoding='utf_16_be').hex()
#这是特殊要求下最终的解决方案
#注意在Python3中已经没有了直接将字符串变成bytes或者Unicode的方法了
#也就是说，在Python中 u'中文'已经不再奏效

#bytes转str
b_str = bytes('中文',encoding='utf-8')
print(b_str.decode()) #直接输出为普通字符串
