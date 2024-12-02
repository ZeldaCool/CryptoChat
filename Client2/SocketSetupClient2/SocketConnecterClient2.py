from ssl import SSLContext

import certifi
import socket
import ssl

data = input('INPUT:')
hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 4000
firstTime = True
def mainloopy ():
    while data != 'quit':
        if not firstTime == True:
            print("Sending: " + data)
            data = data.encode('utf-8')
            s.sendto(data.encode('utf-8'), addr)
        elif not firstTime :
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((HOST, PORT))
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8')
            print("Message from: " + str(addr))