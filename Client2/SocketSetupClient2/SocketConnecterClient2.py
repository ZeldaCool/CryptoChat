from ssl import SSLContext

import certifi
import socket
import ssl

hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST,PORT))
data,addr= s.recvfrom(1024)
data = data.decode('utf-8')
print("Message from: " + str(addr))
print(data)
data = input('INPUT:')
data = data.encode('utf-8')
print("Sending: " + data)
s.sendto(data.encode('utf-8'), addr)