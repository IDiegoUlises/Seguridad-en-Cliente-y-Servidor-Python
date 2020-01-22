import socket  

#Crea un socket
s = socket.socket()

#Se conecta al servidor y elige el puerto a utilizar
s.connect(("192.168.1.88", 60))  
  
while True:
      #Escribe el mensaje para enviar  
      mensaje = raw_input("> ")
      
      #Envia el mensaje
      s.send(mensaje)  
      
      #Cierraa la conexion por peticion
      if mensaje == "quit":  
         break  

#Cierra el socket
s.close()

print "conexion terminada"
