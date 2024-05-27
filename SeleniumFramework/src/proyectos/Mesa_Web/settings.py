import os
import sys
import platform

# Mediante este archivo se establecen las urls y otros valores como directorios

# #######################   URLs   ########################################

url_MesaWeb = "https://waslibhomo.sis.ad.bia.itau/tradingNS/pages/mesa/bandejaOrdenes.xhtml"   #  20/05/2022

# Metodo para obtener datos del excel
def get_user_mesaWeb_homo(nombre_caso):
    from SeleniumFramework.src.utils.excel_file import usuarios
    from SeleniumFramework.src.utils.settings import mesaWeb_user_excel, mesaWeb_user_sheet_homo

    excel = usuarios(mesaWeb_user_excel, mesaWeb_user_sheet_homo)
    return excel.obtener_datos_usuarios(nombre_caso, 'mesaWeb')
