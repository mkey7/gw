# -*- encoding:utf-8 -*-
# socket.getaddrinfo(host,  port, family=0, socktype=0, proto=0, flags=0)
# 根据给定的参数host/port，相应的转换成一个包含用于创建socket对象的五元组，
# 参数host为域名，以字符串形式给出代表一个IPV4/IPV6地址或者None.
# 参数port如果字符串形式就代表一个服务名，比如“http”"ftp""email"等，或者为数字，或者为None
# 参数family为地主族，可以为AF_INET  ，AF_INET6 ，AF_UNIX.
# 参数socktype可以为SOCK_STREAM(TCP)或者SOCK_DGRAM(UDP)
# 参数proto通常为0可以直接忽略
# 参数flags为AI_*的组合，比如AI_NUMERICHOST，它会影响函数的返回值
# 附注：给参数host,port传递None时建立在C基础，通过传递NULL。
# 该函数返回一个五元组(family, socktype, proto, canonname, sockaddr)，同时第五个参数sockaddr也是一个二元组(address, port)
# 更多的方法及链接请访问
# Echo server program

#socket - tcp - server.py（服务端）:
from socket import *
import sys
import threading
from time import ctime
from time import localtime
import traceback
import time
import subprocess
import sm2

# reload(sys)
# sys.setdefaultencoding("utf8")

HOST = '127.0.0.1'
PORT = 8555  # 设置侦听端口
BUFSIZ = 1024

class TcpServer():
    def __init__(self):
        self.ADDR = (HOST, PORT)
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            print('%d is open' % PORT)

            self.sock.bind(self.ADDR)
            self.sock.listen(5)
            # 设置退出条件
            self.STOP_CHAT = False

            # 所有监听的客户端
            self.clients = {}
            self.thrs = {}
            self.stops = []
            self.sm2 = {}
            self.e,self.d,self.k,self.Pa,self.len_para = sm2.init()

        except:
            print('%d is down' % PORT)
            return False

    def IsOpen(ip, port):

        s = socket(AF_INET, SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            # s.shutdown(2)
            # 利用shutdown()函数使socket双向数据传输变为单向数据传输。shutdown()需要一个单独的参数，
            # 该参数表示s了如何关闭socket。具体为：0表示禁止将来读；1表示禁止将来写；2表示禁止将来读和写。
            print('%d is open' % port)
            return True
        except:
            print('%d is down' % port)
            return False

    def listen_client(self):
        while not self.STOP_CHAT:
            print(u'等待接入，侦听端口:%d' % (PORT))
            self.tcpClientSock, self.addr = self.sock.accept()
            print(u'接受连接，客户端地址：', self.addr)
            address = self.addr
            # 将建立的client socket链接放到列表self.clients中
            self.clients[address] = self.tcpClientSock
            # 密钥交换
            self.sm2[address] = self.clients[address].recv(BUFSIZ).decode('utf8')
            self.clients[address].send(self.Pa.encode('utf8'))
            print(str(address)+self.sm2[address])
            # 分别将每个建立的链接放入进程中，接收且分发消息
            self.thrs[address] = threading.Thread(target=self.readmsg, args=[address])
            self.thrs[address].start()
            time.sleep(0.5)

    def readmsg(self, address):
        # 如果地址不存在，则返回False
        if address not in self.clients:
            return False
        # 得到发送消息的client socket
        client = self.clients[address]
        while True:
            try:
                # 获取到消息内容data
                data = client.recv(BUFSIZ).decode('utf8')
            except:
                print('error')
                self.close_client(address)
                break
            if not data:
                break

            data = self.sm_2(data,0,self.sm2[address])
            # python3使用bytes，所以要进行编码
            # s='%s发送给我的信息是:[%s] %s' %(addr[0],ctime(), data.decode('utf8'))
            # 对日期进行一下格式化
            ISOTIMEFORMAT = '%Y-%m-%d %X'
            stime = time.strftime(ISOTIMEFORMAT, localtime())
            s = u'%s发送给我的信息是:%s' % (str(address), data)
            # 将获得的消息分发给链接中的client socket
            for k in self.clients:
                data1 = self.sm_2(s,1,self.sm2[k])
                self.clients[k].send(data1.encode('utf8'))
                #self.clients[k].sendall(u'sendall:' + s.encode('utf8'))
                print(str(k))
            print([stime], ':', data)
            # 如果输入quit(忽略大小写),则程序退出
            STOP_CHAT = (data.upper() == "QUIT")
            if STOP_CHAT:
                print("quit")
                self.close_client(address)
                print("already quit")
                break

    def close_client(self, address):
        try:
            client = self.clients.pop(address)
            self.stops.append(address)
            client.close()
            for k in self.clients:
                self.clients[k].send(str(address) + u"已经离开了")
        except:
            pass
        print(str(address) + u'已经退出')

    def sm_2(self, m, t, o_pa,):
        if t:
            r = sm2.Encrypt(m,o_pa,self.len_para,0)
        if not t:
            r = sm2.Decrypt(m,self.d,self.len_para)
            r = bytes.fromhex(r)
            r = r.decode()
        return r


if __name__ == '__main__':
    tserver = TcpServer()
    tserver.listen_client()
