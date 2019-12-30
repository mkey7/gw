import sm2

def init():
    len_para = int(sm2.Fp / 4)
    e = sm2.get_random_str(len_para)  #签名消息的hash值
    d = sm2.get_random_str(len_para)
    k = sm2.get_random_str(len_para)
    # e = '656E6372797074696F6E207374616E64617264'
    # d = '3945208F7B2144B13F36E38AC6D39F95889393692860B51A42FB81EF4DF7C5B8'
    # d = '58892B807074F53FBF67288A1DFAA1AC313455FE60355AFD'
    Pa = sm2.kG(int(d, 16), sm2.sm2_G,len_para)
    return e,d,k,Pa,len_para

def num(e,h=0):
    E = bytes(e,encoding='utf-8')
    E = E.hex()
    r = int(E,16)
    r *= 4
    r = hex(r)[2:]
    r = bytes.fromhex(r).decode('utf-8')

    return r

def show(d,k,Pa,len_para,o_pa):
    r = ''
    q = 1
    print('*---------------------------*')
    print('|请输入你的操作选项（数字） |')
    print('|       1.加密信息：        |')
    print('|       2.加密过程：        |')
    print('|       3.签名信息：        |')
    print('|       4.签签过程：        |')
    # print('|       5.盲加密法：        |')
    print('|       0.推出程序：        |')
    print('*---------------------------*')
    a = input()

    if a == '1':
        m = input('请输入要加密的明文：')
        r = sm2.Encrypt(m,o_pa,len_para,0)
        r = a+r
    elif a == '2':
        m = input('请输入要加密的明文：')
        r = sm2.Encrypt(m,o_pa,len_para,0)
        print('加密密文：'+r)
        r = a+r
    elif a == '3':
        m = input('请输入要签名的明文：')
        #r = sm2.Sign(m,d,k,len_para,0)
        r = sm2.Encrypt(m,o_pa,len_para,0)
        r = a+r
    elif a == '4':
        m = input('请输入要签名的明文：')
        #r = sm2.Sign(m,d,k,len_para,0)
        r = sm2.Encrypt(m,o_pa,len_para,0)
        print('加密密文：'+r)
        a = '5'
        r = a+r
    elif a == '5':
        m = input('请输入要签名的明文：')
        r = sm2.Encrypt(num(m,1),o_pa,len_para,0)
        r = a+r
    elif a == '0':
        r = '0.推出程序'
        m = '0'
    q = int(a)
    return q,r,m

def deshow(m,E,d,k,o_pa,len_para):
    if m[0] == '1':
        r = sm2.Decrypt(m[1:],d,len_para)
        r = bytes.fromhex(r)
        r = r.decode()
        r = '解密结果：' +r
        a = '1'
    if m[0] == '2':
        print('接受到的密文:'+m[1:])
        r = sm2.Decrypt(m[1:],d,len_para)
        r = bytes.fromhex(r)
        r = r.decode()
        r = '解密结果：' +r
        a = '2'
    if m[0] =='3':
        #r = sm2.Decrypt(m[1:],d,len_para)
        #r = bytes.fromhex(r)
        #r = r.decode()
        #print('r:'+r)
        r = sm2.Sign(m[1:],d,k,len_para,0)
        r = '4'+r
        a = '3'
    if m[0] == '4':
        #E = E.encode('utf-8')
        #e = E.hex() # 消息转化为16进制字符串
        # e = int(E, 16)
        #print('e:'+e)
        r = sm2.Verify(m[1:],E,o_pa,len_para,0)
        r = '解签结果：' +str(r)
        a = '4'
    if m[0] =='5':
        #r = sm2.Decrypt(m[1:],d,len_para)
        #r = bytes.fromhex(r)
        #r = r.decode()
        print('接受到的密文:'+m[1:])
        r = sm2.Sign(m[1:],d,k,len_para,0)
        print('签名密文：'+r)
        r = '6'+r
        a = '5'
    if m[0] == '6':
        #print('e:'+e)
        r = sm2.Verify(m[1:],E,o_pa,len_para,0)
        r = '解签结果：' +str(r)
        a = '6'
#   if m[0] =='5':
#        r = sm2.Decrypt(m[1:],d,len_para)
#        r = bytes.fromhex(r)
#        r = r.decode()
#        print('r:'+r)
#        r = sm2.Sign(r,d,k,len_para,0)
#        r = '6'+r
#        a = '5'
#    if m[0] == '6':
#        #E = E.encode('utf-8')
#        #e = E.hex() # 消息转化为16进制字符串
#        # e = int(E, 16)
#        #print('e:'+e)
#        r = sm2.Verify(m[1:],num(E),o_pa,len_para,0)
#        r = '解签结果：' +str(r)
#        a = '6''
    if m[0] == '0':
        r = '0.退出程序'
        a = '0'
    return r,a

if __name__ == "__main__":
    e,d,k,Pa,len_para = init()
    q = True
    while q:
        q,r,m = show(d,k,Pa,len_para,Pa)
        print(r)

