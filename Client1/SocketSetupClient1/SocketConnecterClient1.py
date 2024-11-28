#Will use socket connections instead of SSH
from ssl import SSLContext


import certifi
import socket
import ssl
import serversocket

hostname = socket.gethostname()
PORT = 400
host = socket.gethostbyname(hostname)

data = input('Message:')
data = host + ": " + data
def sender():
    erver = (serversocket.HOST, 4000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,PORT))
    wrappedSocket = SSLContext().wrap_socket(s, server_side=False, do_handshake_on_connect=True, suppress_ragged_eofs=True, server_hostname=None, session=None)
    wrappedSocket.sendto(data.encode('utf-8'), erver)
    print(wrappedSocket.recv(1024))
    wrappedSocket.close()
sender()