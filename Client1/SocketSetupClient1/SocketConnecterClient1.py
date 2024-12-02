#Will use socket connections instead of SSH
from ssl import SSLContext


import certifi
import socket
import ssl
import serversocket

hostname = socket.gethostname()
PORT = 400
host = socket.gethostbyname(hostname)

ata = input('Message:')
ata = host + ": " + ata
def sender():
    erver = (serversocket.HOST, 4000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,PORT))
    s.sendto(ata.encode('utf-8'),erver)
    print(s.recv(1024))
    s.close()
sender()