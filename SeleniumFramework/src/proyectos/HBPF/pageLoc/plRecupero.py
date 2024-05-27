class plRecupero():
    # Primera pagina
    lbl_titulo = '//*[@id="constantLabel0"]'
    slc_tipo_doc = '//select[@caption="Tipo de documento"]'
    inp_documento = '//input[@id = "textField0"]'
    btn_continuar = "//button[contains(.,'Continuar')]"

    tbl_error = "//table[@id = 'table0' and contains(.,'Aviso')]"
    tbl_usuario_bloqueado = "//table[contains(.,'Aviso de bloqueo')]"
    lbl_ult_pregunta = (
        "//table[contains(@class, 'table-align_wrap-top-margin') "
        "and contains(.,'la respuesta correcta a la siguiente pregunta')]"
    )
    
    radio_pregSeguridad = "//input[@type='radio' and @value='RIESGONET']"
    radio_infoTarjetaItau = "//input[@type='radio' and @value='MISPRODUCTOS']"


    inp_tarjeta = "//input[contains(@caption,'gitos de la tarjeta de')]"
    inp_fecha = "//input[@caption='Fecha de nacimiento']"
    lbl_preguntas = "//*[@class='text-field_nobox-bold-noheight_nolabel']"
    radio_pregunta_1 = "//*[@id='collectionTable0']/tbody/tr"
    radio_pregunta_2 = "//*[@id='collectionTable1']/tbody/tr"
    radio_pregunta_3 = "//*[@id='collectionTable2']/tbody/tr"
    radio_pregunta_4 = "//*[@id='collectionTable3']/tbody/tr"
    radio_pregunta_5 = (
        "//table[@class='collection-table_noformat-nowidth-nothead']/tbody/tr")

    input_user = "//input[@id = 'textField2']"
    input_user_confirmar = "//input[@id='textField3']"
    input_pass = "//input[@id='textField1']"
    input_pass_confirmar = "//input[@id='textField20']"
    input_mail = "//input[@id='textField4']"
    input_mail_confirmar = "//input[@id='textField5']"
    check_terminos = "//input[@type='checkbox' and contains(@id,'checkFiel')]"
    list_avatares = '//*[@id="avatarList"]'

    div_clave_repe = "//div[@id='errorPanelCollection']"

    # usuarios cartera gral
    input_pin = '//input[@title = "Clave cajero"]'
    
    xpBtnAccederAhora = "//*[@id='nextState']" 
    xpMsgYaPodesAcceder = "//p[contains(.,'Ya pod') and contains(.,'s acceder nuevamente')]"
    
    xpClteNoRegistrado = (
        "//span[contains(.,'Los datos ingresados no son correctos. Para recuperar tu usuario o clave a trav') and contains(.,'s de esta opci') and contains(.,'estar registrado en el nuevo home banking')]"
    )
    
    xpBtnCerrar = "//button[@id='backToWorkflow']"
