# -*- coding: utf-8 -*-
class plAdminInicio():
    # login
    ipt_usuario = "//input[@formcontrolname='loginLegajo']"
    ipt_terminal = "//input[@formcontrolname='loginTerminal']"
    ipt_clave = "//input[@formcontrolname='loginPassword']"
    btn_aceptar = "//button[contains(.,'Aceptar')]"
    msj_error = "//app-error-dialog//div[contains(@class,'header')]"
    btn_salir = "//button[contains(@class,'client-dialog-text')]"
    txt_name_cajero = "//span[contains(.,'{}')]"

    # datos
    txt_datos_user = "//div[contains(@class,'client-dialog-text')][2]//span[contains(.,'{}')]"
    txt_usuario = "(//span[@class='value'])[2]"
    

    # buttons menu
    btn_consultas = "//button[contains(@class,'btnMenu') and contains(.,'Consultas')]"

    btn_consulta_operadores = "//button[contains(@class,'btnMenuItem') and contains(.,'Operadores registrados')]"
    btn_consulta_terminales_regis = "//button[contains(@class,'btnMenuItem') and contains(.,'Terminales registradas')]"
    btn_consulta_terminales = "//button[contains(@class,'btnMenuItem') and contains(.,'Terminales registrados')]"
    btn_consulta_saldos = "//button[contains(@class,'btnMenuItem') and contains(.,'Saldos de caja')]"
    btn_consulta_MovDeCajas = "//button[contains(@class,'btnMenuItem') and contains(.,'Movimientos de caja')]"
    btn_consulta_TotalesIngresos = "//button[contains(@class,'btnMenuItem') and contains(.,'Totales ingresos')]"
    btn_consulta_ListadoMultiples = "//button[contains(@class,'btnMenuItem') and contains(.,'Listados M')]"
    btn_consulta_ListadoTickets = "//button[contains(@class,'btnMenuItem') and contains(.,'Listado de Tickets')]"
       
    btn_terminales = "//button[contains(@class,'btnMenu') and contains(.,'Terminales')]"
    btn_terminales_baja = "//button[contains(@class,'btnMenuItem') and contains(.,'Baja')]"

    btn_parametria = "//button[contains(@class,'btnMenu') and contains(.,'Parametr')]"
    btn_limites_maxmin = "//button[contains(@class,'btnMenuItem') and contains(.,'ximos y m')]"

    btn_sucursales = "//button[contains(@class,'btnMenu') and contains(.,'Sucursales')]"
    btn_apertura = "//button[contains(@class,'btnMenuItem') and contains(.,'Apertura')]"


    btn_salir = "//button[contains(@class,'client-dialog-text-button')]/span[contains(.,'Salir')]"