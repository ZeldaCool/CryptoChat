#Will use socket connections instead of SSH
from ssl import SSLContext


import certifi
import socket
import ssl
import SocketConnecterClient2

hostname = socket.gethostname()
PORT = 400
host = socket.gethostbyname(hostname)

data = input('Message:')
data = host + ": " + data
def sender():
    erver = (serversocket.HOST, 4000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,PORT))
    s.sendto(data.encode('utf-8'),erver)
    print(s.recv(1024))
    s.close()
sender()