import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",6666))
name=input("Enter your name:")
client.send(name.encode('utf-8'))
option=input("press Enter to start\n")
while option!=0:
       print("1. print Arrived flights")
       print("2. Gender and Experience")
       print("3. Position Title and Position # ")
       print("4. employee names and their Position #")
       print("5. Quit")
       option=input("Enter the Flight option(not number)\n")
       client.sendto(option.encode('utf-8'),("127.0.0.1",9999)) 
       if option=='1':
         print(client.recv(2048).decode('utf-8'))
         print(client.recv(2048).decode('utf-8'))
         print(client.recv(2048).decode('utf-8'))
         print(client.recv(2048).decode('utf-8'))
         print(client.recv(2048).decode('utf-8'))
         
         

       if option=='5':
           client.close()
