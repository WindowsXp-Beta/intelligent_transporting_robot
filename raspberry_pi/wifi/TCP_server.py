import socket 
from time import ctime 

Host = '' #主机号为空白表示可以使用任何可用的地址
Port = 21566
BUFSIZ = 1024 #接受数据缓冲大小
ADDR = (Host,Port)
tcpsersocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsersocket.bind(ADDR)
tcpsersocket.listen(5) #开始监听
while True:
    tcpClisocket,addr = tcpsersocket.accept()
    print('accept successfully and the address is{}'.format(addr))
    while True:
        data = tcpClisocket.recv(BUFSIZ)
        if not data:  #如果数据空白，则表示客户端退出，所以退出接收	
            break	
        else:
            print('The data received is {}'.format(data))
            msg = input('please input the message you want to send\n')
            tcpClisocket.send(bytes('[{}] {}'.format(ctime(), msg),'utf-8'))
            #这里解释下`byte(str,'utf-8')`的意思，Python3中文本总是Unicode，由str类型表示，二进制数据则由bytes类型表示
            #socket send只能发送二进制数据，所以要讲str转换为b'str'，b'xxx'与xxx的区别在于前者是str，后者虽然内容显得和前
            #者一样，但bytes的每个字符都只占用一个字节，encode是编码，而decode是解码，Python3中str已经是unicode了，因此不需要
            #解码，而str可以使用str.encode('utf-8')变成b'str'，发送信息只能使用bytes，因此需要通过bytes(str,encoding='utf-8')转换
    tcpClisocket.close()
    break
tcpsersocket.close()