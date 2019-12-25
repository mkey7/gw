import sm2

if __name__ == "__main__":
    len_para = int(sm2.Fp / 4)
    print(len_para)
    e = sm2.get_random_str(len_para)
    d = sm2.get_random_str(len_para)
    k = sm2.get_random_str(len_para)
    # e = '656E6372797074696F6E207374616E64617264'
    d = '3945208F7B2144B13F36E38AC6D39F95889393692860B51A42FB81EF4DF7C5B8'
    # d = '58892B807074F53FBF67288A1DFAA1AC313455FE60355AFD'
    Pa = sm2.kG(int(d, 16), sm2.sm2_G,len_para)
    Sig = sm2.Sign(e,d,k,len_para,1)
    print(sm2.Verify(Sig,e,Pa,len_para))
    print(Pa)
    e = "世界考虑一个需求：Alice需要Bob对消息MSG做数字签名，但是Alice又不想让Bob知道MSG，怎么做到？这就是盲签名（Blind signature）要解决的问题。具体的操作流程：、Alice引入一个盲化因子factor对MSG进行盲化，得到BMSG。我的理解，盲化就是一种特殊的对称加密操作，盲化因子factor就是对称密钥，BMSG就是MSG的秘文，通过BMSG无法推导出MSG；"
    print('M = %s' % e)
    C = sm2.Encrypt(e,Pa,len_para,0)
    print('C = %s' % C)
    print('Decrypt')
    m = sm2.Decrypt(C,d,len_para)
    M = bytes.fromhex(m)
    print(M.decode())


