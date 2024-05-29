import logging
from SeleniumFramework.src.utils.constants.Log_constants import (
    FORMATTER, FATAL, CRITICAL, ERROR, WARNING, DEBUG, INFO, NO_VALID
)


class Log:
    def __init__(self, path=None, console=True, level=INFO):
        """
        Metodo para iniciar el logger.
        :param path: String. Path donde se quiere generar el log
        :param console: Boolean. Valor para si es que se quiere mostrar
                        por consola
        :param level: String. Nivel del loger
        """
        self.__logger = logging.getLogger(__name__)
        self.__formatter = logging.Formatter(FORMATTER)
        self.__logger.setLevel(logging.INFO)
        if path is not None:
            self.__logger_file(path, level)
        if console:
            self.__logger_console(level)

    def get_logger(self):
        """ Metodo para obtener el logger """
        return self.__logger

    def __logger_console(self, level):
        """ Metodo para que el loger se muestre por consola"""
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(self.__formatter)
        consoleHandler.setLevel(self.__get_level(level))
        self.__logger.addHandler(consoleHandler)

    def __logger_file(self, path, level):
        """ Metodo para que el loger se genere el archivo log"""
        handler_info = logging.FileHandler(path)
        handler_info.setLevel(self.__get_level(level))
        handler_info.setFormatter(self.__formatter)
        self.__logger.addHandler(handler_info)

    def __get_level(self, level):
        """ Metodo para obtener lo diferentes niveles que tiene el loger"""
        niveles = {
            ERROR: logging.ERROR,
            CRITICAL: logging.CRITICAL,
            WARNING: logging.WARNING,
            FATAL: logging.FATAL,
            DEBUG: logging.DEBUG,
            INFO: logging.INFO
        }
        valor = niveles.get(level)
        if valor is None:
            print(NO_VALID)
        return valor
