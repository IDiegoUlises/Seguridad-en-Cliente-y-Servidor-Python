import socket  
  
s = socket.socket()

#La IP del servidor y el puerto a utilizar
s.bind(("192.168.1.88", 60))

#Clientes permitidos
s.listen(1) 
print "server run"

#Funcion que espera que un cliente se conecte
#para iniciar la conexion
sc, addr = s.accept()  
  
while True:
      #Espera hasta que reciba datos
      recibido = sc.recv(1024)
      
      #Imprime los datos recibidos
      print "received:", recibido
      
      #Para terminar la conexion por peticion del cliente
      if recibido == "quit":  
         break
      
  
#Termina la conexion del servidor  
s.close()

#Termina la conexion del socket con el cliente
sc.close()

print "Conexion terminada"
