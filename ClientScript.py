import socket
import time 
from inputimeout import inputimeout
x=True
exceptTest=False
while x:
  try:
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("127.0.0.1",6666))
  except:
    print("Failed to connect to server will try again in 8 seconds")
    time.sleep(8)
    exceptTest=True
  if not exceptTest:
    x=False
name=inputimeout(prompt="Enter your name:",timeout=60)
client.send(name.encode('utf-8'))
option=inputimeout(prompt="press Enter to start\n",timeout=60)
while option!='0':
  print("1. print All Arrived flights")
  print("2. print All delayed flights")
  print("3. print All flights from a specific airport using the airport ICAO code  ")
  print("4. print Details of a particular flight ")
  print("5. Quit")
  option=inputimeout(prompt="Enter option number:\n",timeout=60)
  client.send(option.encode('utf-8')) 
  if option=='1':
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))

  if option=='2':
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
  if option=='3':
    message=input("Enter airport ICAO code:")
    client.send(message.encode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
  if option=='4':
    message=input("Enter the flight number:")
    client.send(message.encode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
  if option=='5':
    break
   
client.close()
  
