# -*- coding: utf-8 -*-
class pl_ICajaInicio():
    # login
    ipt_usuario = "//input[contains(@formcontrolname,'file')]"           
    ipt_terminal = "//input[contains(@formcontrolname,'terminal')]"
    ipt_clave ="//input[contains(@formcontrolname,'password')]"
    btn_Ingresar = "//span[@class='mat-button-wrapper'][contains(.,'INGRESAR')]"
    btn_aceptar = "//button[contains(.,'Aceptar')]"
    btn_aceptar2 = "//span[contains(.,'ACEPTAR')]"
    msj_error = "//app-error-dialog//div[contains(@class,'header')]"
    btn_salir = "//button[contains(@class,'client-dialog-text')]"
   
    # datos
    lbl_holaUsuario = "//span[contains(.,'Hola, ')]"
    txt_datos_user = "//div[@class='user-info-content'][contains(.,'')]"
    txt_datos_Legajo = "(//span[contains(.,'{}')])[3]"
    txt_datos_Terminal = "(//span[contains(.,'{}')])"
    txt_datos_Sucursal = "//span[contains(.,'{}')]"
    
#   icn_vcard = "//div[@class='menu-button-container'][contains(.,'Hola,')]"
    icn_vcard = "//i[@class='it-icon-vcard']"
    lblDatosOperador = "//div[@class='menu-info-container'][contains(.,'Legajo') and contains(.,'Terminal')]" 
    cdk_overlay_backdrop = "//html[contains(@lang,'en')]"
    txt_usuario = "(//span[contains(.,'{}')])[2]"
    btn_cerrarSesion = "//span[@class='mat-button-wrapper'][contains(.,'CERRAR SESIÓN')]"
    btn_salir = "//button[contains(@class,'client-dialog-text-button')]/span[contains(.,'Salir')]"
    msg_sucursalCerrada = "//span[contains(.,'{}')]"
    msg_errorTerminalUser = "//span[contains(.,'{}')]"
    tle_apertura_forzada = "//span[@class='it-page-title'][contains(.,'Apertura forzada')]"
    checkbox_carga = "(//span[contains(@class,'mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin')])[1]"
    button_cargar = "//button[@type='button'][contains(.,'Cargar')]"
    button_siguiente = "//button[@color='primary'][contains(.,'Siguiente')]"

    