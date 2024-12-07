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
msg = ''
#Function Declarations
def sender():
    msg = input(str('Enter your message here: '))
    while msg != 'New Mode':
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' '*(HEADER - len(send_length))
        print('Message sending now!')
        clientsocket.send(send_length)
        clientsocket.send(message)
    print('Changing modes now!')
    main()
def socketeer(conn,addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print('New Message Recieved!')
            print(str(ADDR)+': '+ msg)
            main()
            if socket.timeout:
                print('Error! Connection Timeout. Closing Socket Now...')
                clientsocket.shutdown(socket.SHUT_RDWR)
                clientsocket.close()
                sys.exit()
def listen():
    print('Setup Complete! Listen ing for connections now! Hostname: ' + SERVER + " Port: 5050")
    clientsocket.listen()
    while True:
        conn,addr = clientsocket.accept()
        handler = int(input('Connection Received! Press One To Accept Connection, Or Press Two to Deny.'))
        if handler == 1:
            threader = threading.Thread(target = socketeer, args =(conn, addr))
            threader.start()
        elif handler == 2:
            conn.close()
            sys.exit()
def main():
    global FirstUse
    while FirstUse == True:
        clientsocket.connect((ADDR))
        print('Attempting connection to Host: ' + SERVER + ' Port: 5050')
        FirstUse = False
        main()
    while True:
        oginput = int(input('Which Mode Are You Using?(One for listening, Two for sending)'))
        if oginput == 1:
            print('Running Listening Mode Now.')
        elif oginput == 2:
            print('Running send mode now.')
            sender()

#Main Area
main()