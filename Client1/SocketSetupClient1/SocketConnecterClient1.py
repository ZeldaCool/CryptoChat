#Import Statements
#Credit: TechWithTim(Adjusted Heavily)
import threading
import socket
#Variable Declarations
HEADER = 100
PORT = 5050
FORMAT = 'utf-8'
inputthing = input(str('Enter the other persons IP here:'))
SERVER = inputthing
ADDR = (SERVER,PORT)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Function Declarations
def sender():
    while msg != 'New Mode':
        msg = input(str('Enter your message here: '))
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' '*(HEADER - len(send_length))
        print('Message sending now!')
        clientsocket.send(send_length)
        clientsocket.send(msg)
    print('Changing modes now!')
    main()
def main():
    while True:
        oginput = input(int('Which Mode Are You Using?(One for listening, Two for receiving)'))
        if oginput == 1:
            print('Running Listening Mode Now.')
        elif oginput == 2:
            print('Running send mode now.')
            sender()

#Main Area
clientsocket.connect(ADDR)
print('Attempting connection to Host: '+ SERVER + ' Port: 5050')
msg = input(str('Enter your message here: '))
sender(msg)
