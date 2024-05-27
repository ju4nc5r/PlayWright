# Automation Framework For Selenium
# Indice

1. [Objetivo](##Objetivo)
2. [Estructura](##Estructura)
3. [Usabilidad](##Usabilidad)
4. [Implementación](##Implementación)
5. [Comandos de utilidad](##Comandos de utilidad)


## Objetivo

Este es un framework diseñado para controlar el driver de Selenium Web Driver,
agregando funciones nuevas utilizando Python. Cada acción que se realiza
en el browser, queda registrado en un log.

También, se agrega el manejo de los plugin de allure.

## Estructura

La estructura de este framework está compuesta por una clase llamada
**sub.py**, donde hereda las funciones de otras clases.

Las subclases son:
- ***allure_driver***: en esta clase, se encuentran los métodos para manejar el
allure, como la generación de pasos y la adjunción de las capturas de pantallas.
- ***browser***: en esta clase se encuentra el manejo de los diferentes browser y las
funciones que tengan que ver con el mismo. Por ejemplo, la apertura de chrome, 
maximizar los navegadores, apertura en modo mobile, manejo de pestañas, etc.
- ***error_management***: En esta clase se generaron funciones relacionadas a pytest
como los mensajes fallados, skipeados y los test fallados.
- ***image***: En esta clases tenemos los metodos relacionados a la captura de 
imágenes y guardarlos en la carpeta de evidencias.
- ***js***: Se encuentran los métodos creados con JavaScript que no están integrados
en selenium web driver, tales como, scrolear hasta que el elemento sea visible,
resaltar un elemento, crear una nueva pestaña, etc.
- ***keyboard***: Se encuentran los metodos para escribir/borrar un texto de un
elemento.
- ***log***: Se encuentra la generacion del log y la carpeta de evidencias.
- ***mouse***: En esta clase se encuentran los métodos relacionados al mouse, tales 
como el click sobre un elemento, dobleclick, mover el cursor sobre un elemento,
etc.
- ***search***: En esta clase, se encuentran los metodos relacionado a la búsqueda de
un elemento en el browser; para la funcion de visibility, se utiliza el tiempo
de espera implicito, por lo que se le deberá pasar por parametro, el tiempo de
espera. Se utiliza los xpath para identificar los elementos.
- ***select_element***: Los elementos select de html, se manejan con esta clase. Se 
pueden seleccionar las opciones de los select según indice, valor, texto y texto
parcial. También tiene una funcion para elegir la opción de manera aleatoria.
- ***sub***: Clase principal que hereda las funciones de las subclases.
- ***webelement***: Clase para obtener el atributo o el texto de un elemento.

Para completar esta estructura, se crea un archivo settings y las constantes
que se utilizan para los mensajes del log.

### Settings.py
> C:\{ubicacion_elegida}\sap-crm-tests\SeleniumFramework\src\utils\settings.py

Archivo donde se definen variables que se utilizan en los test.
- Carpeta de evidencias, que se genera en: **C:/ITAU_Tools/evidencias/homologacion/\*/screenshots'** <br> 
> en donde * es el
> nombre del proyecto en el cual se esta ejecutando (o se reemplaza por 'sin
> proyecto')
- Path para la lectura de los excel que se utilizan
- URL de las aplicaciones
- Path para ejecutar el desbloqueador de usuarios
- Usuario y contraseña del mail
- Usuario y contraseña para la aplicación de CCA

En esta ubicación, se puede crear un archivo local_settings, en donde se pueden
agregar variables con valores locales, ya que este archivo se encuenta ignorado
del repositorio.

### Constants.py
Estos archivos, que se encuentran en: 
> C:\{ubicacion_elegida}\sap-crm-tests\SeleniumFramework\src\constants

Sirven para almacenar las
constantes que se utilizan en el framework.
- constants.py: Se encuentran las constantes que se utilizan en las clases
del framework
- english_message.py: Se encuentran los mensajes en inglés para el log
- spanish_message.py: Se encuentran los mensajes en español para el log

## Estructura de los test
La estructura de los test está diseñada en forma de Page Object, en donde
se crea una clase st(steps) y pl(pagelocator).<br>
En la clase st, se encuentran las acciones que se pueden llevar a cabo en la
pagina; en cambio, en el pl, se encuentran los xpath de los elementos de la 
pagina.

## Instalación
Para la instalación de este framework, en la carpeta requirements se encuentran
las librerias de python que se necesitan instalar. Se puede utilizar el comando
> pip install -r requirements.txt

Luego, hay que definir la variable de entorno PYTHONPATH con el valor de 
donde se encuentra instalado el framework, para asi, pueda reconocer
las importaciones que debe realizar. Por defecto agregar el path
> C:\ITAU_Tools\QA_Automation\workspace\Fram27\src

Una vez finalizada la instalacion, para utilizar este framework basta con 
importar el sub.
> from SeleniumFramework.sub import sub

## Herramientas

### common_functions
En este archivo se encuentran unas funciones comunes, que no utiliza ninguna 
funcion de selenium web driver, pero se puede utilizar en los diferentes 
proyectos. Como la obtención de una fecha segun el plazo, obtención del 
excel para los proyectos, el desbloqueo de un cliente de hb, etc.

### excel_file
Esta clase se crea para menejar un excel con la libreria openpyxl. Se crea 
una clase excel_file, que se encarga de manejar los excel; y una clase usuario,
con metodos definidos para leer un excel de una manera especifica.

La clase usuarios, es utilizado para leer las filas de los casos, obteniendo
los datos por el encabezado. Primero se lee la fila que le corresponde al caso;
segundo, con el usuario que le corresponde al caso, obtiene los datos del
usuario; luego se crea un diccionario de acuerdo al encabezado, y finalmente se
combina el diccionario de la fila del test con el diccionario de la fila de los
datos del usuario. Todo este proceso se realiza con el metodo 
*obtener_datos_usuarios*

### set_xml

Ejecucion para setear el entorno de ejecucion para el allure. Se ingresan los
valores relacionados al nombre del proyecto en jenkins, el ambiente en el que
se está ejecutando, el nodo donde se corrió los test y el navegador que se
está ejecutando. 

Para utilizar este seteo de entorno, se tiene que ejecutar desde el jenkins,
ya que obtiene en nombre y el nodo en el cual se ejecuta el proyecto. En caso
que se ejecute localmente, se muestra un mensaje de error.

El proceso para realizar esta ejecucion, se encuentra en common_functions. <br>

Primero se obtiene el nombre del proyecto y el nodo donde se está ejecutando.
Luego, obtiene el xml enviroment_template, en donde esta el formato de los
entornos que se quiere mostrar; creando un archivo enviroment con los datos
del proyecto. Estos archivos se generan en la carpeta **C:\ITAU_Tools\QA_Automation\workspace\Fram27\src\utils**.
Finalmente, crea la carpeta allure-results, donde se irá guardando los
resultados de las ejecuciones del proyecto y se copia el archivo enviroment
que se genero.

Ejemplo de ejecucion:

![Ejemplo de ejecucion](../img/enviroment.png)

Ejemplo de setting de variables:

![Ejemplo de seteo de ejecucion](../img/enviroment_xml.png)