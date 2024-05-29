# Framework Playwright

Este framework esta construido con: 
- **Playwright** para la creación de casos de prueba 
- **Pytest** para la ejecución de los casos de prueba 
- **Allure Reports** para enviar los resultados de prueba.


## Modo de uso

Para utilizar este framework siga estos pasos:
1. Clonar el repositorio o la rama 'dev' en un directorio local. 
2. Crear y activar un entorno virtual en la carpeta Playwright

```
{ruta_elegida}/sap-crm-tests/PlaywrightFramework/venv/Scripts/activate
```

Una vez dentro de la carpeta 'sap-crm-tests', para activar 
el entorno hay que moverse a la carpeta 'venv/Scripts' y 
ejecutar './activate'

```
cd PlaywrightFramework/venv/Scripts
./activate
```

3. Instalar el requirements.txt que se encuentra dentro del proyecto.

```
cd PlaywrightFramework/
pip install -r requirements.txt
```


## <u>Ventajas del nuevo framework</u>

- Permite crear los test a partir de la grabación 
de acciones por UI. 
- Permite ejecuciones paralelas, emuladores mobile y 
pruebas de geolocalización.
- Agiliza el mantenimiento de los test, ya que
en caso de actualizar los xpaths de la pagina, se
puede realizar otra toma y copiar el codigo. 
- Es compatible con la estructura basada en contenedores
propuesta. 
- Las ejecuciones de los test se realizan de manera
efimera, sin malgastar recursos.
- La integración con Allure se realiza a partir de su API,
que se comunica con un contenedor. De esta manera,
ya no es necesario ejecutar un job para visualizar el reporte en construcción.
Sino simplemente ejecutar un script que envia los archivos que se encuentran en la carpeta allure-results.  


## Creación de test

El framework ofrece la bondad de ejecutar una grabadora que
permite interacturar con la UI de la plataforma a probar y luego
obtenemos el codigo del mismo para copiarlo hacia un nuevo test.

Para activar la grabadora se debe ejecutar el comando:
```
playwright codegen <URL>
```

Esto abrirá dos ventanas, una con un navegador que esta grabando
lo sucedido y otra con el código que se va a generando en cada interacción. 

## Ejecución de test

Para ejecutar todos los test creados, simplemente basta con ir a 
la carpeta y ejecutar el siguiente comando:

```
pytest --alluredir=../allure-results
```

Esto ejecutará todos los test y guardará los resultados en la carpeta 
'allure-results' que se encuentra en el directorio padre.

En caso de que solo se quiera ejecutar un test, se puede hacer desde la UI o por consola 
con el siguiente comando: 

```
pytest nombre_test.py --alluredir=../allure-results
```

> Es importante verificar que siempre la ejecución se está realizando desde la siguiente ruta:
> ya que sino la carpeta 'files' se creará fuera de la carpeta de proyecto. 
```
C:\{ruta_elegida}\sap-crm-tests\PlaywrightFramework\projects\{project}\test
``` 

## Estructura de un proyecto

- config
- projects
  - HBPF
    - allure-results
    - files
      - captures
      - videos
    - send_results.ps1
    - test

> **config**: esta carpeta se encarga de contenedor los métodos, 
> necesarios comunes a cualquier proyecto. Por ejemplo, eliminar resultados de la carpeta de allure.

> **IMPORTANTE**: las carpetas ***allure-results***, ***captures***
> y ***videos*** deben estar incluidas en el **.gitignore** 

> **allure-results**: esta carpeta contendrá todos los 
> resultados generados en la ejecución de casos de manera local. 

> **captures**: esta carpeta contendrá todas las imagenes
> capturadas durante la ejecución del test.

> **videos**: esta carpeta contendrá todos los videos 
> generados por los test ejecutados, en caso de dejar activa 
> dicha función durante su ejecución. 

> **send_results**: este script envia los resultados a allure pruebas.
> Captura los resultados desde la carpeta 'allure-results' del proyecto especificado. 

> **config**: esta carpeta se encarga de contenedor los métodos, 
> necesarios comunes a cualquier proyecto. Por ejemplo, eliminar resultados de la carpeta de allure.


## Integración con Allure

En la creación del test a partir de la grabadora no se incluye la integración con allure
y tampoco se encuentra activa la función de screenshots, estos pasos deben ser agregados
manualmente al test. 

Para realizar las capturas se encuentra creado el método 'screen2allure', 
dentro del modulo **stBrowser** que permite sacar las capturas e integrar dicha
imagen a un step de allure.


## Envio de resultados a la instancia de prueba de Allure

Debido a que hay una instancia de prueba de Allure corriendo en un contenedor,
podemos enviar los resultados a partir de su API, para ver como nos queda el reporte. Para eso,
se encuentra el archivo **send_results**, que se puede ejecutar
para enviar los resultados a la instancia de allure de prueba. 


## Eliminar resultados de la carpeta allure-results

Para vaciar los resultados de la carpeta 'allure-results' correspondiente
al proyecto en el que estemos trabajando, solamente hay que pasarle
como parametro al método inicio_test un bool que indique un 'True', si 
se quieren borrar los resultados anteriores. Por defecto, se encuentra
definido en 'False', por lo que si no se realiza dicha modificación quedarán
todos los resultados de nuestras ejecuciónes. 

Por ejemplo: 
```
inicio_test(self, True)
```



# Comandos utiles para Playwright

### Ejecutar grabadora de test
```
playwright codegen <URL>
```

### Ejecutar test abriendo un navegador
```
pytest --headed
```

### Ejecutar test abriendo un navegador con medida especifica
```
playwright codegen --viewport-size=800,600 playwright.dev
```

### Ejecutar test emulando dispositivo
```
playwright codegen --device="iPhone 13" playwright.dev
```

### Ejecutar test de geolocalización
```
playwright codegen --timezone="Europe/Rome" --geolocation="41.890221,12.492348" --lang="it-IT" bing.com/maps
```

### Preservar cookies en repo:
```
playwright codegen github.com/microsoft/playwright --save-storage=auth.json
```

Sirve para guardar las credenciales de login, para futuros casos de uso. 


### Cargar cookies desde repo:  
```
playwright codegen --load-storage=auth.json github.com/microsoft/playwright
```



### Ejecutar pruebas en paralelo
```
pytest --numprocesses 2
```
