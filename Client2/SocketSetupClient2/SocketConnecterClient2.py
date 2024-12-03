#Import Statements
#Credit: TechWithTim(Code Adjusted Heavily)
import sys
import threading
import socket
#Variable Declarations
HEADER = 100
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
FORMAT = 'utf-8'
#Function Declarations
def socketeer(conn,addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        print('New Message Recieved!')
        print(str(ADDR)+': '+ msg)
        if socket.timeout:
            print('Error! Connection Timeout. Closing Socket Now...')
            conn.close()
            sys.exit()

def main():
    server.listen()
    while True:
        conn,addr = server.accept()
        handler = input(int('Connection Received! Press One To Accept Connection, Or Press Two to Deny.'))
        if handler == 1:
            threader = threading.Thread(target = socketeer, args =(conn, addr))
            threader.start()
        elif handler == 2:
            conn.close()
            sys.exit()
#Main Area
print('Setup Complete! Listening for connections now! Hostname: '+SERVER+" Port: 5050")
main()