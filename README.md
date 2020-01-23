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
