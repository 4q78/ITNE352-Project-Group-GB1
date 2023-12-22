import requests
import json
import socket
import threading
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",6666))
server.listen(3)
def Connection():
    code=input("Enter the airport code\n")
    def apiParameters(parameters):
       api=requests.get('https://api.aviationstack.com/v1/flights',parameters)
       with open("GB1_202105138/202106345.jason","w") as k:
        json.dumps(api.json(),indent=4)
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
clientSocket,address=server.accept()
t1=threading.Thread(target=Connection)
t1.start()



