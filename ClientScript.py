import socket
import time
from inputimeout import inputimeout 
loop_control=True
exceptTest=False
#keep trying to connect each 8 seconds if server is offline
while loop_control:
   try:
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("127.0.0.1",6666))
    if client.getpeername():
      print("Connected")
      break
   except:
     print("Failed to connect to server will try again in 8 seconds")
     time.sleep(8)
     exceptTest=True
   if not exceptTest:
     loop_control=False
while True:#login credintials exchange with the server
  message=client.recv(1024).decode('utf-8')
  client.send(input(message).encode())
  message=client.recv(1024).decode('utf-8')
  client.send(input(message).encode())
  message=client.recv(1024).decode('utf-8')
  print(message)
  if message.casefold()=="login successful!":
    break
name=inputimeout(prompt="Enter your name:", timeout=240) #inputimeout instead of regular input to help with user being inactive
client.send(name.encode('utf-8'))
option=input("press Enter to start\n")
try:
 while option!='0':
  print("1. print All Arrived flights")
  print("2. print All delayed flights")
  print("3. print All flights from a specific airport using the airport ICAO code  ")
  print("4. print Details of a particular flight ")
  print("5. Quit")
  option=inputimeout(prompt="Enter option number:\n",timeout=240)
  client.send(option.encode('utf-8')) 
  if option=='1':
    dataRecieved=True
    while dataRecieved:
     data = client.recv(2048).decode('utf-8')
     print(data)
     if len(data) < 2048:
       print(80 * "-")
       print()
       break
  if option=='2':
    dataRecieved=True
    while dataRecieved:
     data = client.recv(2048).decode('utf-8')
     print(data)
     if len(data) < 2048:
       print(80 * "-")
       print()
       break
  if option=='3':
    message=input("Enter deparure airport:")
    client.send(message.encode('utf-8'))
    dataRecieved=True
    while dataRecieved:
     data = client.recv(2048).decode('utf-8')
     print(data)
     if len(data) < 2048:
       print(80 * "-")
       print()
       break
  if option=='4':
    message=input("Enter the flight iata:")
    client.send(message.encode('utf-8'))
    dataRecieved=True
    while dataRecieved:
     data = client.recv(2048).decode('utf-8')
     print(data)
     if len(data) < 2048:
       print(80 * "-")
       print()
       break
  if option=='5':
    break
except ConnectionResetError: #handle client crash 
 print("Client  was forcibly closed or crashed. Closing the connection..." ) 
except KeyboardInterrupt:
 client.send("cntrl+c".encode('utf-8'))
 print("Closing connection...")
finally:
  client.close()  
