import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",6666))
name=input("Enter your name:")
client.send(name.encode('utf-8'))
option=input("press Enter to start\n")
while option!='0':
  print("1. print All Arrived flights")
  print("2. print All delayed flights")
  print("3. print All flights from a specific airport using the airport ICAO code  ")
  print("4. print Details of a particular flight ")
  print("5. Quit")
  option=input("Enter option number:\n")
  client.send(option.encode('utf-8')) 
  if option=='1':
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print(client.recv(2048).decode('utf-8'))
    print("Am here")
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
  
