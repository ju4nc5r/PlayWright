# -*- coding: utf-8 -*-
class plAdminInicio():
    # login
    ipt_usuario = "//input[@formcontrolname='loginLegajo']"
    ipt_terminal = "//input[@formcontrolname='loginTerminal']"
    ipt_clave = "//input[@formcontrolname='loginPassword']"
    btn_aceptar = "//span[contains(.,'Ingresar')]"
    msj_error = "//app-error-dialog//div[contains(@class,'header')]"
#     btn_salir = "//span[@class='mat-button-wrapper'][contains(.,'Salir')]"
    btn_salir = "//button[contains(@class,'client-dialog-text')]"
  
    # datos
    txt_name_cajero = "//span[contains(.,'{}')]"
    txt_datos_user = "//span[contains(.,'{}')]"
    

    # buttons menu
    btn_consultas = "//button[contains(.,'Consultas')]"

#     btn_consulta_operadores = "//button[contains(@class,'btnMenuItem') and contains(.,'Operadores registrados')]"
    btn_consulta_operadores = "//button[contains(.,'Operadores Registrados')]"
#     btn_consulta_terminales_regis = "//button[contains(@class,'btnMenuItem') and contains(.,'Terminales registradas')]"
    btn_consulta_terminales_regis = "//button[contains(.,'Terminales Registradas')]"
    
    btn_consulta_terminales = "//button[contains(@class,'btnMenuItem') and contains(.,'Terminales registrados')]"
#     btn_consulta_saldos = "//button[contains(@class,'btnMenuItem') and contains(.,'Saldos de caja')]"
    btn_consulta_saldos = "//button [contains(.,'Saldos de Caja')]"
#     btn_consulta_MovDeCajas = "//button[contains(@class,'btnMenuItem') and contains(.,'Movimientos de caja')]"
    btn_consulta_MovDeCajas = "//button[contains(.,'Movimientos de Caja')]"
#     btn_consulta_TotalesIngresos = "//button[contains(@class,'btnMenuItem') and contains(.,'Totales ingresos')]"
    btn_consulta_TotalesIngresos = "//button[contains(.,'Totales Ingresos')]"  
#     btn_consulta_ListadoMultiples = "//button[contains(@class,'btnMenuItem') and contains(.,'Listados M')]"
    btn_consulta_ListadoMultiples = "//button[contains(.,'Listados M')]"
#     btn_consulta_ListadoTickets = "//button[contains(@class,'btnMenuItem') and contains(.,'Listado de Tickets')]"
    btn_consulta_ListadoTickets = "//button[contains(.,'Listados de Tickets')]"
    
    btn_terminales = "//button[contains(.,'Terminales')]"
    btn_terminales_baja = "(//button[contains(.,'Baja')])[1]"

    btn_parametria = "//button[contains(@class,'btnMenu') and contains(.,'Parametr')]"
    
    btn_limites_maxmin = "//button[contains(.,'Límites Máximos y Mínimos')]"

#     btn_limites_maxmin = "//button[contains(@class,'btnMenuItem') and contains(.,'ximos y m')]"

    btn_sucursales = "//button[contains(.,'Sucursales')]"
    btn_apertura = "//button[contains(.,'Apertura')]"
    msjSucursalYaEstaAbierta = "//div[@class='mat-dialog-content'][contains(.,'No se puede aperturar la sucursal,ya se encuentra abierta')]"
    btn_salir = "//button[contains(@class,'btnMenu mat-button')]/span[contains(.,'Salir')]"
    
    cell_saldoCajero = "//td[contains(@class,'{}')]"
    cell_preba = "(//td[contains(@class,'{}')])"
    cell_operador = "(//td[contains(@class,'{}')])"
    cell_saldoSupervisor = "(//td[contains(@class,'{}')])[3]"
    msj_error_terminal = "//div[@class='mat-dialog-content'][contains(.,'Error: Ocurrio un error al intentar obtener la terminal del usuario')]"
    btn_aceptar_2 = "//button[contains(.,'Aceptar')]" 