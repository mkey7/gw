from tkinter import *
import threading
import c_s
import sm2
        
class win():
        def __init__(self):
                self.win = Tk()
                self.win.title('Char Room')
                self.data = ''
                #创建几个frame作为容器
                self.frame_left_top   = Frame(width=380, height=270, bg='white')
                self.frame_left_center  = Frame(width=380, height=100, bg='white')
                self.frame_left_bottom  = Frame(width=380, height=20)
                self.frame_right     = Frame(width=170, height=400, bg='white')
                ##创建需要的几个元素
                self.text_msglist    = Text(self.frame_left_top)
                self.text_msg      = Text(self.frame_left_center);
                self.button_sendmsg   = Button(self.frame_left_bottom, text='发送', command=self.sendmessage)
                #创建一个绿色的tag
                self.text_msglist.tag_config('green', foreground='#008B00')
                #使用grid设置各个容器位置
                self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
                self.frame_left_center.grid(row=1, column=0, padx=2, pady=5)
                self.frame_left_bottom.grid(row=2, column=0)
                #self.frame_right.grid(row=0, column=1, rowspan=3, padx=4, pady=5)
                self.frame_left_top.grid_propagate(0)
                self.frame_left_center.grid_propagate(0)
                self.frame_left_bottom.grid_propagate(0)
                #把元素填充进frame
                self.text_msglist.grid()
                self.text_msg.grid()
                self.button_sendmsg.grid(sticky=E)
                self.e,self.d,self.k,self.Pa,self.len_para = sm2.init()
                self.tc = c_s.TcpClient(self.Pa)
                print('D: '+self.d)
                print('o_pa: '+self.tc.o_pa)
                self.trecv = threading.Thread(target=self.recvmsg)
                self.trecv.start()
                #主事件循环
                self.win.mainloop()

        def sendmessage(self):
                data = self.text_msg.get('0.0', END)
                print(data)
                print(self.sm_2(data,1))
                self.tc.sendmsg(self.sm_2(data,1))
                self.text_msg.delete('0.0', END)

        def recvmsg(self):
        # 接收消息，如果链接一直存在，则持续监听接收消息
                try:
                        while self.tc.client.connect_ex(self.tc.ADDR):
                                data = self.tc.client.recv(self.tc.BUFSIZ).decode('utf8')
                                data = self.sm_2(data,0)
                                print(u'从%s收到信息：%s' % (self.tc.HOST, data))
                                self.text_msglist.insert(END, data)
                except:
                        print('error')

        def sm_2(self, m, t):
                if t:
                        r = sm2.Encrypt(m,self.tc.o_pa,self.len_para,0)
                if not t:
                        r = sm2.Decrypt(m,self.d,self.len_para)
                        r = bytes.fromhex(r)
                        r = r.decode()
                return r
                
                '''
        def sendmessage(self):
                #在聊天内容上方加一行 显示发送人及发送时间
                self.msgcontent = '我:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
                self.text_msglist.insert(END, msgcontent, 'green')
                self.text_msglist.insert(END, text_msg.get('0.0', END))
                self.text_msg.delete('0.0', END)
                '''
w = win()
