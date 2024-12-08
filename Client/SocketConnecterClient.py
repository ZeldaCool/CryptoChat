#Import Statements
#Credit: TechWithTim(Adjusted Heavily)
import threading
import socket
import sys

#Variable Declarations
HEADER = 100
PORT = 7070
FORMAT = 'utf-8'
FirstUse = True
SERVER = ''
ADDR = (SERVER,PORT)
inputthing = input(str('Enter the other persons IP here:'))
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = inputthing
ports = 7070
servers = socket.gethostbyname(socket.gethostname())
adresss = (servers, ports)
ADDR = (SERVER,PORT)
msg = ''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
FirstSend = True
FirstRecieve = True
#Function Declarations
def sender():
    global FirstSend
    msg = input(str('Enter your message here: '))
    while FirstSend:
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' '*(HEADER - len(send_length))
        print('Message sending now!')
        clientsocket.send(send_length)
        clientsocket.send(message)
        FirstSend = False
        sendhandler()
    print('Changing modes now!')
    main()
def sendhandler():
    global send_length
    global message
    global FirstSend
    print('Message sending now!')
    clientsocket.send(send_length)
    clientsocket.send(message)
    FirstSend = False
    sender()
def socketeer(conn,addr):
    global FirstRecieve
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if FirstRecieve:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print('New Message Recieved!')
            print(str(ADDR)+': '+ msg)
            FirstRecieve = False
            main()
            if socket.timeout:
                print('Error! Connection Timeout. Closing Socket Now...')
                clientsocket.shutdown(socket.SHUT_RDWR)
                clientsocket.close()
                sys.exit()
def listen():
    print('Setup Complete! Listening for connections now! Hostname: ' + SERVER + " Port: 5050")
    client.listen(HEADER)
    while True:
        conn,addr = client.accept()
        handler = int(input('Connection Received! Press One To Accept Connection, Or Press Two to Deny.'))
        if handler == 1:
            print('Ready to recieve messages!')
            threader = threading.Thread(target = socketeer, args =(conn, addr))
            threader.start()
        elif handler == 2:
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            sys.exit()
def main():
    global FirstUse
    while FirstUse == True:
        clientsocket.connect((ADDR))
        print('Attempting connection to Host: ' + SERVER + ' Port: 5050')
        FirstUse = False
        main()
    while True:
        global FirstRecieve
        global FirstSend
        oginput = int(input('Which Mode Are  You Using?(One for listening, Two for sending)'))
        if oginput == 1:
            print('Running Listening Mode Now.')
            FirstRecieve = True
            listen()
        elif oginput == 2:
            print('Running send mode now.')
            FirstSend = True
            sender()

#Main Area
main()