import requests
import json
import socket
import threading
'''server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",6666))
server.listen(3)
def Connection(sock,id):
    code=input("Enter the airport code\n")
    def apiParameters(parameters):
       api=requests.get('http://api.aviationstack.com/v1/flights',parameters)
       jsonValue=json.dumps(api.json(),indent=4)
       with open("GB1_202105138/202106345.jason","w") as k:
          k.write(jsonValue)
    message=server.recv(1024).decode('utf-8')
    print(message)
    st1=server.recv(1024).decode
    jsonFile="GB1_202105138/202106345.jason"
    st1=(str)
    while st1.casefold() !="quit":
       if(st1=="arrived flights".casefold()):
           parameters={
          'access_key': '1d815a01512667373760dd9a41070d0f',
          'arr_icao':code,
          'flight_status':'landed'
}
           with open(jsonFile,'r') as k:
              information=clientSocket.sendall(json.load(k)) 
              
numThreads=[] 
clientSocket,address=server.accept()
t1=threading.Thread(target=Connection,args=(clientSocket,len(numThreads)+1))
numThreads.append(t1)
t1.start()
clientSocket.close()'''

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",6666))
server.listen(3)
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
    message=ClientSocket.recv(1024).decode('utf-8')
    print(message)
    message=ClientSocket.recv(1024).decode('utf-8')
    while True:
         if message=='1':        
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


                     
                  
                     
                     #print(search['arrival']['gate'],"\n")

            break      
                       #ClientSocket.sendall(json.dumps(json.load(k)).encode('utf-8')) 
                     #ClientSocket.close()
              

while True:
    ClientSocket,address=server.accept()
    threading.Thread(target=Clients,args=(ClientSocket,address)).start()

