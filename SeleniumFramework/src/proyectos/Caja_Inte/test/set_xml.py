import argparse
from SeleniumFramework.common_functions import test_Modificar_XML_Enviroments


def set_Values(carpeta):
    test_Modificar_XML_Enviroments(carpeta)


def test_obtener_parser():
    parser = argparse.ArgumentParser(
        description='generacion de la carpeta de allure-results'
    )
    parser.add_argument('carpeta', help='path de la carpeta')
    arg = parser.parse_args()
    carpeta = arg.carpeta
    if carpeta[len(carpeta) - 1] != '/':
        carpeta += '/'
    carpeta = carpeta.replace('/', '\\')
    return carpeta


if __name__ == "__main__":
    carpeta = test_obtener_parser()
    set_Values(carpeta)
