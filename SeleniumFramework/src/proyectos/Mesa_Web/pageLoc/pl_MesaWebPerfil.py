# -*- coding: utf-8 -*-
class pl_MesaWebPerfil():
    
    # Menu perfiles
    btn_otro_perfil = "//a[contains(@title,'Seleccionar otro Perfil')]" 
    
    #Perfiles
    auditoria = "//td[contains(.,'AUDITORIA')]"
    operador_planeamiento = "//label[@for='j_id_38:8'][contains(.,'OperadorIAM')]"
    operador_IAM = "//label[@for='j_id_38:8'][contains(.,'OperadorIAM')]"
    operador_backOffice = "//td[contains(.,'OperadorBackOfficeConf')]"
    operador_bancaPrivada = "//td[contains(.,'OperadorBancaPrivada')]"
    operadorMesaDinero = "//label[@for='j_id_38:9'][contains(.,'OperadorMesaDinero')]"
    operador_banca_privada = "//label[@for='j_id_38:3'][contains(.,'OperadorBancaPrivada')]"
    operador_sucursal = "//label[@for='j_id_38:13'][contains(.,'OperadorSucursal')]"

    #Cambiar Perfil
    btn_cambiar_perfil = "//input[contains(@name,'switchButton')]"
    
    btn_cambiar_perfil_2 = "//input[contains(@value,'Cambiar Perfil')]"

    
    