class plRegistro():
    # Primera pagina
    lbl_titulo = '//*[@id="constantLabel0"]'
    slc_tipo_doc = '//select[@caption="Tipo de documento"]'
    inp_documento = '//input[@id = "textField0"]'
    btn_continuar = "//button[contains(.,'Continuar')]"
    tbl_error = ("//table[@id = 'table0' and (contains(.,'en Internet') or "
                 "contains(.,'Importante'))]")

    radio_pregSeguridad = "//input[@type='radio' and @value='RIESGONET']"
    radio_infoTarjetaItau = "//input[@type='radio' and @value='MISPRODUCTOS']"

    inp_tarjeta = "//input[contains(@caption,'gitos de la tarjeta de')]"
    inp_fecha = "//input[@caption='Fecha de nacimiento']"
    lbl_preguntas = "//*[@class='text-field_nobox-bold-noheight_nolabel']"
    radio_pregunta_1 = "//*[@id='collectionTable0']/tbody/tr"
    radio_pregunta_2 = "//*[@id='collectionTable1']/tbody/tr"
    radio_pregunta_3 = "//*[@id='collectionTable2']/tbody/tr"
    radio_pregunta_4 = "//*[@id='collectionTable3']/tbody/tr"

    input_user = "//input[@id = 'textField2']"
    input_user_confirmar = "//input[@id='textField3']"
    input_pass = "//input[@id='textField1']"
    input_pass_confirmar = "//input[@id='textField20']"
    input_mail = "//input[@id='textField4']"
    input_mail_confirmar = "//input[@id='textField5']"
    check_terminos = "//input[@type='checkbox' and contains(@id,'checkFiel')]"
    list_avatares = '//*[@id="avatarList"]'

    # usuarios cartera gral
    input_pin = '//input[@title = "Clave cajero"]'

    input_codActivacion = "//input[contains(@caption,'digo de activaci')]"
    button_continuarCodAct = "//button[@id='continuar']"
    span_registrado = "//span[contains(.,'Felicitaciones')]"
    span_registrado2 = "//p[contains(.,'Ahora pod') and contains(.,'s hacer todo todas tus operaciones sin ir al banco') and contains(.,'con tu ')]"
    button_Ingresar = "//button[@id='nextState']"
    
    #xpMsgErrNoPodProcOperac = "//*[@class='error-panel_title' and contains (.,'En estos momentos no podemos procesar la operaci')]"
    
    xpMsgErrNoPodProcOperac = "//*[@id ='richText0' and contains (.,'La operaci') and contains (.,'no pudo ser realizada en este momento')]"
    
    # xpMsgYaAdherido = "//*[@class='error-panel_title' and contains (.,'Ya est') and contains (.,'registrado en uno de los canales digitales de Ita')]"
    
    xpMsgYaAdherido = "//*[@id ='richText0' and contains (.,'Ya est') and contains (.,'registrado en uno de los canales digitales de Ita')]"
    
    #xpBtnCancelar = "//button[@id='cancelar']"
    
    xpBtnCancelar = "//*[@id='tableAlign15']"
    
    inp_Rnp = "//input[contains(@id,'textField00')]"
    
    radio_doc_viejo = "//input[contains(@id,'radio2')]"