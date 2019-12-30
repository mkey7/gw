import socket
import s
    # 创建连接
client = socket.socket()
client.connect(("localhost",6881))
e,d,k,Pa,len_para = s.init()
st = str(Pa)
client.send(st.encode("utf-8"))
data = client.recv(1024)
o_pa = data.decode('utf-8')
print('连接对象的公钥为：'+o_pa)
q = 1
while q:
        # 发送操作数据
    q,r,m = s.show(d,k,Pa,len_para,o_pa)
    client.send(r.encode("utf-8"))
    if q == 3:
        data = client.recv(1024)
        r,a = s.deshow(data.decode('utf-8'),r[1:],d,k,o_pa,len_para)
        print(r)
    if q == 5:
        data = client.recv(1024)
        r,a = s.deshow(data.decode('utf-8'),r[1:],d,k,o_pa,len_para)
        print(r)

        # 处理接受到的数据
    data = client.recv(1024)
    r,a = s.deshow(data.decode('utf-8'),m,d,k,o_pa,len_para)
    if a == '3':
        client.send(r.encode('utf-8'))
    if a == '5':
        client.send(r.encode('utf-8'))
    if a == '0':
        q = 0
    print(r)

client.close()
