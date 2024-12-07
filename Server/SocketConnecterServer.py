#Import Statements
#Credit: TechWithTim(Code Adjusted Heavily)
import sys
import threading
import socket
#Variable Declarations
HEADER = 100
PORT = 7070
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
FORMAT = 'utf-8'
FirstUse = True
inputthing = ''
#Function Declarations
def socketeer(conn,addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print('New Message Recieved!')
            print(str(addr)+': '+ msg)
            main()
            if socket.timeout:
                print('Error! Connection Timeout. Closing Socket Now...')
                server.shutdown(socket.SHUT_RDWR)
                server.close()
                sys.exit()

def listen():
    print('Setup Complete! Listening for connections now! Hostname: ' + SERVER + " Port: 5050")
    server.listen()
    while True:
        conn,addr = server.accept()
        handler = int(input('Connection Received! Press One To Accept Connection, Or Press Two to Deny.'))
        if handler == 1:
            threader = threading.Thread(target = socketeer, args =(conn, addr))
            threader.start()
        elif handler == 2:
            server.shutdown(socket.SHUT_RDWR)
            server.close()
            sys.exit()
def sender():
    inputthing = input(str('Enter the other persons IP here:'))
    while inputthing != 'New Mode':
        SERVER = inputthing
        PORT = 7070
        ADDR = (SERVER,PORT)
        server.connect((SERVER,7070))
        print('Attempting connection to Host')
        msg = input(str('Enter your message here: '))
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' '*(HEADER - len(send_length))
        print('Message sending now!')
        server.send(send_length)
        server.send(message)
    print('Changing modes now!')
    main()
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER,PORT)
def main():
    global FirstUse
    while FirstUse == True:
        listen()
        FirstUse = False
    while True:
        oginput = int(input('Which Mode Are You Using?(One for listening, Two for sending)'))
        if oginput == 1:
            print('Running Listening Mode Now.')
            listen()
        elif oginput == 2:
            print('Running send mode now.')
            sender()
#Main Area
main()