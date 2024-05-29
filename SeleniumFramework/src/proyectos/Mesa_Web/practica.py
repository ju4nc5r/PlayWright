
from cryptography.fernet import Fernet

# Generar una clave aleatoria
clave = Fernet.generate_key()

# Crear un objeto Fernet con la clave generada
cipher_suite = Fernet(clave)

# Texto sin encriptar
texto_sin_encriptar = "Mi clave secreta"

# Convertir el texto en bytes
texto_bytes = texto_sin_encriptar.encode()

# Encriptar el texto
texto_encriptado = cipher_suite.encrypt(texto_bytes)

# Imprimir el texto encriptado
print("Texto encriptado:", texto_encriptado)


def obteneter_user():    
    import getpass
    user = getpass.getuser()
    return (user.lower())
    
def obtener_decimales_aleatorios(de,hasta):
    import random
    numero_aleatorio = random.randint(de, hasta)
    return(numero_aleatorio)

print(obteneter_user())

