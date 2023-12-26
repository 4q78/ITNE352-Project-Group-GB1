import requests
import json
import socket
import threading
import time
import sqlite3
import hashlib
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",6666))
server.listen(3)
print("Wating for connection....")
timeoutSec=60
'''code=input("Enter the airport code\n")
params = {
    'access_key': '1d815a01512667373760dd9a41070d0f',
    'arr_icao': code,
    'limit': 100
}
def apiParameters(params): 
       api=requests.get('http://api.aviationstack.com/v1/flights',params=params)
       data=api.json()
       with open("GB1.json","w") as k:
         json.dump(data,k,indent=4)
         print("File saved")
apiParameters(params=params)'''
def Clients(ClientSocket,address):
    print(f'connected to {address}')
    ClientSocket.settimeout(timeoutSec)
    check_client_login(ClientSocket)
    try:
       Namemessage=ClientSocket.recv(1024).decode('utf-8')
       print(Namemessage)
       message=ClientSocket.recv(1024).decode('utf-8')
       if not message or not Namemessage:
          raise socket.timeout
       x=True
       while x:
         if message=='1':  
            print(f'name:{Namemessage} |type of request: All arrived flights (return flight IATA code, departure airport name,\n arrival time, arrival terminal number, and arrival gate).')    
            print(80*"-")
            print()  
            with open('GB1.json','r') as k:
               reader=json.load(k)
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
            ClientSocket.send(json.dumps(Dictiata,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(Dictairport,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(Dictactual,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictTerminal,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(Dictgate,indent=4).encode('utf-8'))
         if message=='2':
            print(f'name:{Namemessage} |type of request: All delayed flights (return flight IATA code, departure airport,\n original departure time, the estimated time of arrival), arrival terminal, delay, and arrival gate.')
            print(80*"-")
            print()
            with open('GB1.json','r') as k:
               reader=json.load(k)
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
            ClientSocket.send(json.dumps(Dictiata,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(Dictairport,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictDactual,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(Dictestimated,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictATerminal,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictADelay,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(Dictgate,indent=4).encode('utf-8'))
         if message=='3':
            print(f'name:{Namemessage} | type of request: All flights from a specific airport using the airport ICAO code (return flight IATA code, \n departure airport, original departure time, estimated arrival time, departure gate, arrival gate, and status).')
            print(80*"-")
            print()
            message=ClientSocket.recv(1024).decode('utf-8')
            with open('GB1.json','r') as k:
               reader=json.load(k)
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
            ClientSocket.send(json.dumps(Dictiata,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(Dictairport,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictDactual,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(Dictestimated,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictDg,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictAg,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(Dictstatus,indent=4).encode('utf-8'))
         if message=='4':
            print(f'name:{Namemessage} |type of request: Details of a particular flight (return flight IATA code; \n departure airport,gate, and terminal; arrival airport, gate, and terminal; \n status; scheduled departure time; and scheduled arrival time).')
            print(80*"-")
            print()
            message=ClientSocket.recv(1024).decode('utf-8')
            with open('GB1.json','r') as k:
               reader=json.load(k)
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
            ClientSocket.send(json.dumps(Dictiata,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(Dictairport,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictDg,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictDterminal,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictAairport,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictAg,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictAt,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(Dictstatus,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictSDT,indent=4).encode('utf-8'))
            ClientSocket.send(json.dumps(DictSAT,indent=4).encode('utf-8'))
         if message=='5':
            print(f"Client {Namemessage} has disconnected")
            x=False
         message=ClientSocket.recv(1024).decode('utf-8')
         if not message or not Namemessage:
          return 
       else:
        ClientSocket.close()
    except socket.timeout:
            print(f"Client {address} timed out. Closing the connection.")
            print() 
            return  
    finally:
       ClientSocket.close()
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

while True:
    ClientSocket,address=server.accept()
    threading.Thread(target=Clients,args=(ClientSocket,address)).start()        
            

         

                     
                  
                     
                     

                 
                       
              



