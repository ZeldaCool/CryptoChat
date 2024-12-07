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
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(ADDR)
FORMAT = 'utf-8'
FirstUse = True
inputthing = ''
FirstRecieve = True
FirstSend = True
#Function Declarations
def socketeer(conn,addr):
    global FirstRecieve
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if FirstRecieve:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print('New Message Recieved!')
            print(str(addr)+': '+ msg)
            FirstRecieve = False
            main()
            if socket.timeout:
                print('Error! Connection Timeout. Closing Socket Now...')
                server.shutdown(socket.SHUT_RDWR)
                server.close()
                sys.exit()

def listen():
    print('Setup Complete! Listening for connections now! Hostname: ' + SERVER + " Port: 5050")
    serversocket.listen(HEADER)
    conn, addr = serversocket.accept()
    handler = int(input('Connection Received! Press One To Accept Connection, Or Press Two to Deny.'))
    while True:
        if handler == 1:
            threader = threading.Thread(target = socketeer, args =(conn, addr))
            threader.start()
        elif handler == 2:
            serversocket.shutdown(socket.SHUT_RDWR)
            serversocket.close()
            sys.exit()
def sender():
    global FirstSend
    inputthing = input(str('Enter the other persons IP here:'))
    while FirstSend:
        serv = inputthing
        port = 7070
        address = (serv,port)
        server.connect((address))
        print('Attempting connection to Host')
        msg = input(str('Enter your message here: '))
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' '*(HEADER - len(send_length))
        FirstSend = False
        sendhandler()
    print('Changing modes now!')
    main()
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER,PORT)
def main():
    global FirstUse
    global FirstSend
    while FirstUse == True:
        FirstUse = False
        main()
    while True:
        oginput = int(input('Which Mode Are You Using?(One for listening, Two for sending)'))
        if oginput == 1:
            print('Running Listening Mode Now.')
            listen()
        elif oginput == 2:
            print('Running send mode now.')
            FirstSend = True
            sender()
def sendhandler():
    global send_length
    global message
    global FirstSend
    print('Message sending now!')
    server.send(send_length)
    server.send(message)
    FirstSend = False
    main()
#Main Area
main()