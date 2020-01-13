import socket
import s
# 创建接听
server = socket.socket()
server.bind(("localhost",6881))
server.listen()
e,d,k,Pa,len_para = s.init()
q = 1
while q:
    # 创建连接
    conn,addr = server.accept()
    print("connect by",addr)
    data = conn.recv(1024)
    o_pa = data.decode('utf-8')
    print('连接对象的公钥为：'+o_pa)
    conn.send(Pa.encode('utf-8'))
    m = ''
    while q:
        # 处理接受到的数据
        data = conn.recv(1024)
        r,a = s.deshow(data.decode('utf-8'),m,d,k,o_pa,len_para)
        if a == '3':
            conn.send(r.encode('utf-8'))
        if a == '5':
            conn.send(r.encode('utf-8'))
        if a == '0':
            q = 0
            conn.send(r.encode('utf-8'))
            break
        print(r)
        # 发送操作数据
        q,r,m = s.show(d,k,Pa,len_para,o_pa)
        conn.send(r.encode('utf-8'))
        if q == 3:
            data = conn.recv(1024)
            r,a = s.deshow(data.decode('utf-8'),r[1:],d,k,o_pa,len_para)
            print(r)
        if q == 5:
            data = conn.recv(1024)
            r,a = s.deshow(data.decode('utf-8'),r[1:],d,k,o_pa,len_para)
            print(r)


server.close()


