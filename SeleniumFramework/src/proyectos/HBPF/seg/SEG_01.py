import requests
import random
import string

# URL de la página de inicio de sesión
login_url = 'https://internethomo.sis.ad.bia.itau/internet/sso'


# Generar un nombre de usuario y contraseña aleatorios
random_username = generate_username()
random_password = generate_password()
print("Usuario:", random_username)
print("Contraseña:", random_password)
# Datos de inicio de sesión aleatorios
payload = {
    'username': random_username,
    'password': random_password
}

# Realizar la solicitud POST para iniciar sesión
response = requests.post(login_url, data=payload, verify=False)

# Verificar si el inicio de sesión fue exitoso
if response.status_code == 200:
    print("Inicio de sesión exitoso.")
    print("Usuario:", random_username)
    print("Contraseña:", random_password)
    # Aquí puedes continuar navegando por la página autenticada
else:
    print("Error al iniciar sesión. Código de estado:", response.status_code)



### SCRIPT PARA CONOCER TODOS LOS XPATHS DE UNA WEB ###

from selenium import webdriver

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir la página web
driver.get("https://www.ejemplo.com")

# Obtener todos los elementos de la página
elements = driver.find_elements_by_xpath("//*")

# Imprimir los xpaths de todos los elementos
for element in elements:
    print("Xpath:", element.get_attribute("xpath"))

# Cerrar el navegador
driver.quit()
