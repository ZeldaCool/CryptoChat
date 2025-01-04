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
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ports = 5050
servers = socket.gethostbyname(socket.gethostname())
adresss = (servers, ports)
ADDR = (SERVER,PORT)
msg = ''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(adresss)
FirstSend = True
FirstRecieve = True
FirstConnect = True
#Function Declarations
def sender():
    global FirstSend
    global send_length
    global message
    global FirstConnect
    inputthing = input(str('Enter the other persons IP here:'))
    while FirstSend & FirstConnect:
        SERVER = inputthing
        ADDR = (SERVER,PORT)
        srvr = inputthing
        addr = (srvr, PORT)
        print('Attempting Connection to Host')
        msg = input(str('Enter Your Message Here:'))
        clientsocket.connect((addr))
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' '*(HEADER - len(send_length))
        FirstSend = False
        FirstConnect = False
        sendhandler()
    while FirstSend:
        msg = input(str('Enter Your Message Here:'))
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        print('Message sending now!')
        clientsocket.send(send_length)
        clientsocket.send(message)
        FirstSend = False
        FirstConnect = False
        sendhandler()
    print('Changing modes now!')
    main()
def sendhandler():
    global send_length
    global message
    global FirstSend
    global msg
    print('Message sending now!')
    clientsocket.send(send_length)
    clientsocket.send(message)
    FirstSend = False
    main()
def socketeer(conn,addr):
    global FirstRecieve
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if FirstRecieve:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)
            print('New Message Recieved!')
            print(str(addr)+': '+str(msg))
            FirstRecieve = False
            main()
            if socket.timeout:
                print('Error! Connection Timeout. Closing Socket Now...')
                clientsocket.shutdown(socket.SHUT_RDWR)
                clientsocket.close()
                sys.exit()
def listen():
    print('Setup Complete! Listening for connections now! Hostname: ' + servers + " Port: 5050")
    client.listen(HEADER)
    conn, addr = client.accept()
    handler = int(input('Connection Received! Press One To Accept Connection, Or Press Two to Deny.'))
    while True:
        if handler == 1:
            threader = threading.Thread(target=socketeer, args=(conn, addr))
            threader.start()
        elif handler == 2:
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            sys.exit()
def main():
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