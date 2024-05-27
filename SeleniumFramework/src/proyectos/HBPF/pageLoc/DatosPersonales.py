class DatosPersonales():
    # Datos personales
    # Encontrado en el menu de perfil
    lbl_Titulo_Datos_Personales_xp = ("//*[@id='constantLabel0' and " 
                                      "text()='Datos personales']")

    # Pagina de datos personales
    txt_DirParticular = "(//span[contains(@caption,'Direcci')])[1]"

    #Modificacion de celular / e-mail (cm)
    btn_Modificar_CelMail_xp = "//*[@id='CelMail']"
    txt_CambioCm_Tel_CodInterurbano = "//*[@id='textField0']"
    txt_CambioCm_Tel_Telefono = "//*[@id='textField088']"
    sel_CambioCm_Tel_Empresa = "//*[@id='selectField001']"
    txt_CambioCm_Mail = "//*[@id='textField12']"
    txt_CambioCm_MailAlt = "//*[@id='textField133']"

    # Modificacion de domicilio particular o laboral (dpl)
    btn_Modificar_DomParticular_xp = "//*[@id='DomicilioParticular_P1']"
    btn_Modificar_DomLaboral_xp = "//*[@id='DomicilioLaboral_P1']"
    txt_CambioDpl_Dom_Calle_xp = "//*[@id='textField101']"
    inp_CambioDpl_Dom_NumCalle_xp = "//input[contains(@caption,'mero')]"
    txt_CambioDpl_Dom_Piso_xp = "//*[@id='textField81']"
    txt_CambioDpl_Dom_CodPostal_xp = "//*[@id='textField311']"
    txt_CambioDpl_Dom_Departamento_xp = "//*[@id='textField211']"
    sel_CambioDpl_Dom_LocalidadProvincia_xp = "//*[@id='selectField0110']"
    txt_CambioDpl_Tel_CodInterurbano_xp = "//*[@id='textField018']"
    txt_CambioDpl_Tel_Telefono_xp = "//*[@id='textField191']"
    txt_CambioDpl_TelAlt_CodInterurbano_xp = "//*[@id='textField023']"
    txt_CambioDpl_TelAlt_Telefono_xp = "//*[@id='textField241']"

    # Botones comunes en la modificacion
    btn_Cambio_Cancelar_xp = "//*[@id='Salir']"
    btn_Cambio_Volver_xp = "//*[@id='actionButton1']"
    # btn_Cambio_Continuar_xp = "//*[@id='actionButton9']"
    btn_Cambio_Continuar_xp = ("//button[contains(.,'Continuar') or " 
                               "contains(.,'continuar')]")
    btn_Confirmar_xp = "//button[contains(@id,'Confirmar')]"

    # Carteles de error
    pnl_Error_xp = "//*[@id='errorPanelCollection' or @id='errorPanel']"

    # Paso actual
    div_paso_actual = ("//div[contains(@class,'step-process_active') " 
                       "and contains(.,'confirmaci')]")

    # Pagina confirmacion
    lbl_celular_direc = (
        "//label[contains(@class,'constant-label_label-small')]")
    inp_clave_itau = "//input[@caption='Clave']"

    # Pagina resultado
    img_comprobante = "//img[contains(@id,'imageComponent0')]"
