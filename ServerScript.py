import requests
import json
import socket
import threading
import time
import sqlite3
import hashlib
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",6666))
server.listen()
print("Wating for connection....")
timeoutSec=240
code=input("Enter the airport code(arr_icao)\n")
params = {
    'access_key': '1d815a01512667373760dd9a41070d0f',
    'arr_icao': code,
    'limit': 100
}
# function returns api information and store it in .json file
def apiParameters(params): 
       api=requests.get('http://api.aviationstack.com/v1/flights',params=params)
       data=api.json()
       with open("GB1.json","w") as file:
         json.dump(data,file,indent=4)
         print("File saved")
apiParameters(params=params)
# function that will deal with all clients and will take clientsocket and address as parameter to seperate between each client(deal with all requests after checking credintials)
def Clients(ClientSocket,address):
    print(f'connected to {address}')
    ClientSocket.settimeout(timeoutSec)
    try:
       check_client_login(ClientSocket)
       Namemessage=ClientSocket.recv(1024).decode('utf-8')
       print(Namemessage)
       message=ClientSocket.recv(1024).decode('utf-8')
       if message=="cntrl+c":
        raise KeyboardInterrupt
       if not message or not Namemessage:
          raise socket.timeout
       loop_control=True
       while loop_control:
         if message=='1':  
            print(f'name:{Namemessage} |type of request: All arrived flights (return flight IATA code, departure airport name,\n arrival time, arrival terminal number, and arrival gate).')    
            print(80*"-")
            print()  
            with open('GB1.json','r') as file:
               reader=json.load(file)
               iata=[]
               airport=[]
               actual=[]
               terminal=[]
               gate=[]

               for search in reader['data']:
                  if search['flight_status']=='landed':
                     iata.append(search['flight']['iata'])
                     airport.append(search['departure']['airport'])
                     actual.append(search['arrival']['actual'])
                     terminal.append(search['arrival']['terminal'])
                     gate.append(search['arrival']['gate'])
            Dictiata={'iata':iata}
            Dictairport={'airport':airport}
            Dictactual={'arrival':actual}
            DictTerminal={'terminal':terminal}
            Dictgate={'gate':gate}
            data_to_send = [Dictiata,Dictairport,Dictactual,DictTerminal,Dictgate]
            ClientSocket.sendall(json.dumps(data_to_send, indent=4).encode('utf-8'))
         if message=='2':
            print(f'name:{Namemessage} |type of request: All delayed flights (return flight IATA code, departure airport,\n original departure time, the estimated time of arrival), arrival terminal, delay, and arrival gate.')
            print(80*"-")
            print()
            with open('GB1.json','r') as file:
               reader=json.load(file)
               iata=[]
               airport=[]
               Dactual=[]
               estimated=[]
               arrivalTerminal=[]
               arrivalDelay=[]
               gate=[]

               for search in reader['data']:
                  if search['arrival']['delay']!='null':
                     iata.append(search['flight']['iata'])
                     airport.append(search['departure']['airport'])
                     Dactual.append(search['departure']['actual'])
                     estimated.append(search['arrival']['estimated'])
                     arrivalTerminal.append(search['arrival']['terminal'])
                     arrivalDelay.append(search['arrival']['delay'])
                     gate.append(search['arrival']['gate'])
            Dictiata={'iata':iata}
            Dictairport={'airport':airport}
            DictDactual={'departure':Dactual}
            Dictestimated={'estimated':estimated}
            DictATerminal={'termianl':arrivalTerminal}
            DictADelay={'delay':arrivalDelay}
            Dictgate={'gate':gate}
            data_to_send = [Dictiata,Dictairport,DictDactual,Dictestimated,DictATerminal,DictADelay,Dictgate]
            ClientSocket.sendall(json.dumps(data_to_send, indent=4).encode('utf-8'))
         if message=='3':
            print(f'name:{Namemessage} | type of request: All flights from a specific airport using the airport ICAO code (return flight IATA code, \n departure airport, original departure time, estimated arrival time, departure gate, arrival gate, and status).')
            print(80*"-")
            print()
            message=ClientSocket.recv(1024).decode('utf-8')
            with open('GB1.json','r') as file:
               reader=json.load(file)
               iata=[]
               airport=[]
               Dactual=[]
               estimated=[]
               DepGate=[]
               arrivalGate=[]
               status=[]
               

               for search in reader['data']:
                  if search['departure']['airport']==message:
                     iata.append(search['flight']['iata'])
                     airport.append(search['departure']['airport'])
                     Dactual.append(search['departure']['actual'])
                     estimated.append(search['arrival']['estimated'])
                     DepGate.append(search['departure']['gate'])
                     arrivalGate.append(search['arrival']['gate'])
                     status.append(search['flight_status'])
                     
                     
            Dictiata={'iata':iata}
            Dictairport={'airport':airport}
            DictDactual={'departure':Dactual}
            Dictestimated={'estimated':estimated}
            DictDg={'gate':DepGate}
            DictAg={'gate':arrivalGate}
            Dictstatus={'status':status}
            data_to_send = [Dictiata,Dictairport,DictDactual,Dictestimated,DictDg,DictAg,Dictstatus]
            ClientSocket.sendall(json.dumps(data_to_send, indent=4).encode('utf-8'))
         if message=='4':
            print(f'name:{Namemessage} |type of request: Details of a particular flight (return flight IATA code; \n departure airport,gate, and terminal; arrival airport, gate, and terminal; \n status; scheduled departure time; and scheduled arrival time).')
            print(80*"-")
            print()
            message=ClientSocket.recv(1024).decode('utf-8')
            with open('GB1.json','r') as file:
               reader=json.load(file)
               iata=[]
               airport=[]
               DepGate=[]
               DipT=[]
               arrivalAirport=[]
               arrivalGate=[]
               arrivalTerminal=[]
               status=[]
               scheduledDTime=[]
               scheduledATime=[]
               

               for search in reader['data']:
                  if search['flight']['iata']==message:
                     iata.append(search['flight']['iata'])
                     airport.append(search['departure']['airport'])
                     DepGate.append(search['departure']['gate'])
                     DipT.append(search['departure']['terminal'])
                     arrivalAirport.append(search['arrival']['airport'])
                     arrivalGate.append(search['arrival']['gate'])
                     arrivalTerminal.append(search['arrival']['terminal'])
                     status.append(search['flight_status'])
                     scheduledDTime.append(search['departure']['scheduled'])
                     scheduledATime.append(search['arrival']['scheduled'])

                     
                     
            Dictiata={'iata':iata}
            Dictairport={'airport':airport}
            DictDg={'gate':DepGate}
            DictDterminal={'terminal':DipT}
            DictAairport={'airport':arrivalAirport}
            DictAg={'gate':arrivalGate}
            DictAt={'terminal':arrivalTerminal}
            Dictstatus={'status':status}
            DictSDT={'scheduled':scheduledDTime}
            DictSAT={'scheduled':scheduledATime}
            data_to_send = [Dictiata,Dictairport,DictDg,DictDterminal,DictAairport,DictAg,DictAt,Dictstatus,DictSDT,DictSAT]
            ClientSocket.sendall(json.dumps(data_to_send, indent=4).encode('utf-8'))
         if message=='5':
            print(f"Client {Namemessage} has disconnected")
            loop_control=False
         message=ClientSocket.recv(1024).decode('utf-8')
         if message=="cntrl+c":
            raise KeyboardInterrupt
         if not message or not Namemessage:
          return 
       else:
        ClientSocket.close()
    except socket.timeout: #handle client being inactive
            print(f"Client {address} timed out. Closing the connection...")
            print() 
            return
    except ConnectionResetError: #handle client crash 
            print(f"Client {address} was forcibly closed or crashed. Closing the connection..." )
    except KeyboardInterrupt:#handle keyboard interrupt(cntrl+c)
        print(f"Ctrl+C pressed by client {address}. Closing the connection...")
    finally: # whether we went through exception or not at last close the connection
       ClientSocket.close()
# function to check clients credintials before accessing the server and it will be called at the beggining of the clients function that deal with the requests
def check_client_login(ClientSocket):
   while True:
    ClientSocket.send("username: ".encode('utf-8'))
    username=ClientSocket.recv(1024).decode('utf-8')
    ClientSocket.send("password: ".encode('utf-8'))
    password=ClientSocket.recv(1024)
    password=hashlib.sha256(password).hexdigest()
    Dbconnect=sqlite3.connect("userdata.db")
    cur=Dbconnect.cursor()
    cur.execute("SELECT * FROM userdata WHERE username =? AND password=?",(username,password))
    if cur.fetchall():
       ClientSocket.send("login successful!".encode('utf-8'))
       break
    else:
       ClientSocket.send("login failed!".encode('utf-8'))
# a loop that will wait for clients and each client that is connected will have his own running thread to run multiple clients simultaneously
while True:
    ClientSocket,address=server.accept()
    threading.Thread(target=Clients,args=(ClientSocket,address)).start()        
                   
            


         

                     
                  
                     
                     

                 
                       
              



