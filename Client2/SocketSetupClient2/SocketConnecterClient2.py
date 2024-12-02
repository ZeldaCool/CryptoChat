from ssl import SSLContext

import certifi
import socket
import ssl
import time

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
            try:
                s.sendto(data.encode('utf-8'), addr)
            except socket.timeout:
                print("Error, timeout")
                s.close()
        elif not firstTime :
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((HOST, PORT))
            s.settimeout(5)
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8')
            print("Message from: " + str(addr))