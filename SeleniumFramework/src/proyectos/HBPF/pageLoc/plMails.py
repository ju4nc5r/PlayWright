class plMails():
    input_usermail = "//input[@id='username']"
    input_password = "//input[@id='password']"
#     btn_inicio_ses = "//input[@type = 'submit']"
    btn_inicio_ses = "descendant::span[contains(@class,'signinTxt')][1]"
    
#     btn_bandeja_entrada = "//span[contains(.,'Bandeja de entrada')]"
    btn_bandeja_entrada = "descendant::span[contains(.,'Bandeja de entrada')][1]"
#     label_cambio_clave = (
#         "//div[(contains(.,'Recupero de Usuario') or "
#         "contains(.,'para completar tu registro')) and @id='divSubject']"
#     )
    label_cambio_clave = (
        "descendant::span[contains(.,'digo de activaci') and contains(.,'n para completar tu registro a los canales digitales de banco Ita')][1]"
    )
    
    xpAsuntoMailCodActivRecupero = (
        "descendant::span[contains(.,'Recupero de Usuario y Clave digital de Ita')][1]"
    )
#     label_clave_activacion = (
#         "//div[contains(.,'digo de activac') and "
#         "@style = 'margin-top:14pt;margin-bottom:14pt;'][2]"
#     )    
    label_clave_activacion = (
        "//span[contains(.,'Tu c') and contains(.,'digo de activac')]/following-sibling::span[1]"
    )
    
    xpIcnUsuario = ("//button[contains(@aria-label,'Usuario de Servicio para Homologaci')]")
    xpBtnCerrar = ("//span[contains(.,'Cerrar sesi')]")
    