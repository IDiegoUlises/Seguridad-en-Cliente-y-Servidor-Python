# Servidor y Cliente En Python

**Funcion:** Crea un servidor y un usuario que se conecta a traves de un socket en donde se pueden enviar correos, mensajes, archivos, imagenes y documentos, etc.

**Denegacion de Servicio:** Si usted manda datos infinitos como por **ejemplo**

   ```python
while True:
      socket.send(data)
```
Usted **derribara el servidor** para proteger nuestro servidor debemos **limitar** la conexion que hemos acceptada se puede realizar de diferentes maneras.

* Limitar el tamaño del buffer que podemos recibir
* Restrigir las peticiones que podemos acceptar
* Bloquear la conexion por la direccion IP


**Excepcion no Atrapada:** Su servidor puede tener un error de sofware que puede **derribar el servidor** como por ejemplo que suceda una **excepcion** que no es **atrapada** es importante que todos las excepciones sean atrapadas.

**Ejemplo:**
   ```python
  int division = 0/0
```
Por realizar esta division su servidor cerrara de manera inesperada y mostrara el siguiente error
   ```python
ZeroDivisionError: division by zero
```

**Inyeccion de Datos:** Esto es cuando el cliente inyecta datos de manera fraudulenta para recibir datos que estan restingidos como **contraseñas**.

**Ejemplo:**
   ```python
socket.send(0)
```

Usted manda un ```0``` no recibira ningun dato si usted cambia este valor de este mensaje a un ```1 ``` usted recibira datos restringidos como una ```contraseña``` 

**Actividad Sospechosa:** Debemos tener un algoritmo que detecte la actividad sospechosa para impedir cualquier accion maliciosa por parte de personas malitencionadas.

**Pasos**
* Documentar la actividad del usuario
* Almacenar el documento en una base de datos
* Analizar la actividad del usuario

Con estos datos podemos diseñar nuestro **cortafuegos** para impedir las actividades maliciosas.

**Ejemplo:**
 ```python
socket.send(0x52)
```
Al verificar el mensaje que el usuario nos ha enviado podemos señalar que es diferente al que tendriamos que recibir esto es porque es una conexion malitencionada al documentar estas acciones podemos crear un algoritmo de **cortafuegos**.

**Recuperacion de Cuenta:** Una persona puede obtener nuestras credenciales como **usuario** y **contraseña** por diversor maneras intentara bloquear al propetario de la cuenta para no permitirle el ingreso para impedir esto podemos usar.

* **Verificacion por SMS:** Para que este proceso de recuperacion sea seguro debemos darle proridad a los numeros telefonicos mas antiguos registrados.

* **Verificacion por Ubicacion:** Podemos utilizar la ubicacion del usuario para poder comprobar el legitimo dueño del propietario de la cuenta.

* **Pregunta Secreta:** Este metodo puede ser subestimado y en muchos casos lo pueden considerar anticuado pero no deben olvidar que este metodo en uso resulta ser uno de los mas confiable y de los mas seguros.

**No Permitir la Entrada de Robots:** Un robot humano como **Sophia** de **Microsoft** puede entrar a nuestro servidor o un programa informatico como un **bot** puede hacer **spam** en nuestro sitio para evitar esto podemos utilizar.

* **Captcha:** Es una prueba de la capacidad de una máquina para exhibir un comportamiento inteligente similar al de un ser humano puede ser por sonido o por imagen.

* **Conducta Perfecta:** Una persona se equivoca en determinadas acciones cuando realizan peticiones perfectas puede ser considerado un robot.

* **Duracion de una Sesion:** Una persona para ```escribir``` ese texto se demora aproximamente ```5 segundos``` y para enviarlo  en total se demora ```8 segundos``` aproximadamente cuando las peticiones se manda un tiempo que un **humano** no puede lograr es porque es un robot.

# Imagen en Funcionamiento
![alt text](https://github.com/IDiegoUlises/Servidor-y-Cliente-En-Python/blob/master/images/servidor-y-cliente-python-funcionando.png)








