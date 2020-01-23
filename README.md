# Servidor y Cliente En Python

**Funcion:** Crea un servidor y un usuario que se conecta a traves de un socket en donde se pueden enviar correos, mensajes, archivos, imagenes y documentos, etc.

**Denegacion de Servicio:** Si usted manda datos infinitos como por **ejemplo**

   ```python
while True:
      socket.send(data);
```
Usted **derribara el servidor** para proteger nuestro servidor debemos **limitar** la conexion que hemos acceptada se puede realizar de diferentes maneras.

* Limitar el tamaño del buffer que podemos recibir
* Restrigir las peticiones que podemos acceptar
* Bloquear la conexion por la direccion IP


**Excepcion No Atrapada:** Su servidor puede tener un error de sofware que puede **derribar el servidor** como por ejemplo que suceda una **excepcion** que no es **atrapada** es importante que todos las excepcion sean atrapadas.

**Ejemplo:**
   ```python
int division = 0/0
```
Por realiar esta division su servidor cerrara de manera inesperada y mostrara el siguiente error
   ```python
ZeroDivisionError: division by zero
```

**Inyeccion De Datos:** Esto es cuando el cliente inyecta datos de manera fraudulenta para manipular los datos y recibir datos que estan restingidos.

**Ejemplo:**
   ```python
socket.send(0)
```

Usted manda un ```0``` no recibira datos si usted cambia este valor de este mensaje a un ```1 ``` usted recibira datos restringidos como una ```contraseña``` 




