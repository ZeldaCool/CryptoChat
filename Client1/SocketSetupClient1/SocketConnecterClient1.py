#Import Statements
#Credit: TechWithTim(Adjusted Heavily)
import threading
import socket
#Variable Declarations
HEADER = 100
PORT = 5050
inputthing = input(str('Enter the other persons IP here:'))
SERVER = inputthing
ADDR = (SERVER,PORT)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Function Declarations
#Main Area
clientsocket.connect(ADDR)
print('Attempting connection to Host: '+ SERVER + ' Port: 5050')
