import socket
import time
from inputimeout import inputimeout 
loop_control=True
exceptTest=False
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
while True:
  message=client.recv(1024).decode('utf-8')
  client.send(input(message).encode())
  message=client.recv(1024).decode('utf-8')
  client.send(input(message).encode())
  message=client.recv(1024).decode('utf-8')
  print(message)
  if message.casefold()=="login successful!":
    break
name=inputimeout(prompt="Enter your name:", timeout=240)
client.send(name.encode('utf-8'))
option=input("press Enter to start\n")
while option!='0':
  print("1. print All Arrived flights")
  print("2. print All delayed flights")
  print("3. print All flights from a specific airport using the airport ICAO code  ")
  print("4. print Details of a particular flight ")
  print("5. Quit")
  option=inputimeout(prompt="Enter option number:\n",timeout=240)
  client.send(option.encode('utf-8')) 
  if option=='1':
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(80*"-")
    print()
  if option=='2':
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(80*"-")
    print()
  if option=='3':
    message=input("Enter deparure airport:")
    client.send(message.encode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(80*"-")
    print()
  if option=='4':
    message=input("Enter the flight iata:")
    client.send(message.encode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(80*"-")
    print()
  if option=='5':
    break
   
client.close()