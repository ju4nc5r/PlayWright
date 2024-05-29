# -*- coding: utf-8 -*-
class pl_MesaWebInicio():
    # login
    ipt_usuario = "//input[contains(@name,'loginForm:inputUser')]" 
    ipt_clave ="//input[contains(@type,'password')]"
    btn_Ingresar = "//input[contains(@name,'loginForm:acceptButton')]"
    btn_aceptar = "//button[contains(.,'Aceptar')]"
    btn_aceptar2 = "//span[contains(.,'ACEPTAR')]"
    msj_error = "//app-error-dialog//div[contains(@class,'header')]"
    btn_salir = "//button[contains(@class,'client-dialog-text')]"
   
    # datos
    lbl_holaUsuario = "//span[contains(.,'Hola ')]"
    txt_datos_user = "//div[@class='user-info-content'][contains(.,'')]"
    txt_datos_Legajo = "(//span[contains(.,'{}')])[3]"
    txt_datos_Terminal = "(//span[contains(.,'{}')])"
    txt_datos_Sucursal = "//span[contains(.,'{}')]"
#   icn_vcard = "//div[@class='menu-button-container'][contains(.,'Hola,')]"
    icn_vcard = "//i[@class='it-icon-vcard']"
    lblDatosOperador = "//div[@class='menu-info-container'][contains(.,'Legajo') and contains(.,'Terminal')]" 
    cdk_overlay_backdrop = "//html[contains(@lang,'en')]"
    txt_usuario = "//div[contains(@class,'user-fullname')]"
    btn_cerrarSesion = "//i[contains(@class,'fa fa-power-off')]"
    btn_salir = "//button[contains(@class,'client-dialog-text-button')]/span[contains(.,'Salir')]"
    msg_sucursalCerrada = "//span[contains(.,'{}')]"
    msg_errorTerminalUser = "//span[contains(.,'{}')]"
    

    