import socket 
from time import ctime 

Host = '' #主机号为空白表示可以使用任何可用的地址
Port = 21567
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
            tcpClisocket.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))
    tcpClisocket.close()
tcpsersocket.close()