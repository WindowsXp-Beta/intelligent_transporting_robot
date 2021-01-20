from socket import *
from time import sleep
import threading

def recvData():
    udpRecvSocket = socket(AF_INET,SOCK_DGRAM)
    myRecvPort = 48969
    bindAddr = ('',myRecvPort)
    try:
        udpRecvSocket.bind(bindAddr)
    except OSError:
        myRecvPort = int(input("input a port:"))
        bindAddr = ('',myRecvPort)
        udpRecvSocket.bind(bindAddr)
    myIpAddr = gethostbyname(getfqdn(gethostname()))#gethostname()得到主机名 gethostbyname()得到主机IP
    print("local ip:[{}],local port [{}]".format(myIpAddr,myRecvPort))
    while True:
        try:
            recvData = udpRecvSocket.recvfrom(1024)
            print("receive data is :{}".format(recvData))
        except error as e:
            print(e)

def sendData():
    sleep(10)
    udpSendSocket = socket(AF_INET,SOCK_DGRAM)
    sendIpAddr = input("target ip:")
    sendPort = int(input("target port:"))
    sendAddr = (sendIpAddr,sendPort)
    while True:
        sendData = input("please input the data to sended")
        udpSendSocket.sendto(sendData.encode(),sendAddr)

def main():
    t1 = threading.Thread(target = recvData)
    t2 = threading.Thread(target = sendData)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
