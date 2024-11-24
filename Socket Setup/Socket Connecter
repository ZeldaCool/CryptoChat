#Will use socket connections instead of SSH
from ssl import SSLContext

import certifi
import socket
import ssl

packet, reply = "<packet>How are you?</packet>", "Packet Sent!"
HOST, PORT = '127.0.0.5', 443


sock = socket.socket(socket.SOCK_STREAM)
sock.settimeout(10)

# Fix position error
wrappedSocket = SSLContext().wrap_socket(sock, server_side=False, do_handshake_on_connect=True, suppress_ragged_eofs=True, server_hostname=None, session=None)



wrappedSocket.connect((HOST, PORT))
wrappedSocket.send (packet)
print(wrappedSocket.recv(1280))


wrappedSocket.close()