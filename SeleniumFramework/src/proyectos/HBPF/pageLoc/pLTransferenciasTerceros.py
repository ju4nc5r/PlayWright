# -*- coding: utf-8 -*-
class plTransferenciasTerceros():

    title_transferencia_terceros = (
        "//span[contains(@class,'title-span') and "
        "contains(.,'Transferencia')]"
    )
    title_transferencia_terceros_itau = (
        "//span[contains(@class,'title-span') and "
        "contains(.,'Transferencia a terceros')]"
    ) 
    list_cta_debito = "//select[@id = 'selectField1']"
    opt_cuenta = "//select[@id = 'selectField1']//option[contains(.,'{}')]"
    
    input_cta_acreditacion = (
        "//input[contains(@caption,'Alias/CBU/CVU')]"
    )
    cmd_agenda = '//button[@id = "actionButton0"]'
    table_destino = '//table[@id = "collectionTable0"]'
    option_primera_cuenta = (
        '//table[@id = "collectionTable0"]/tbody/tr[1]/td/input'
    )
    option_segunda_cuenta = (
        '//table[@id = "collectionTable0"]/tbody/tr[2]/td/input'
    )
    option_cuenta_variable = "//table[contains(@id,'collectionTable0')]//td[contains(.,'{}')]"
    radio_button_cuenta = "//preceding-sibling::td[1]"

    cmd_continuar = '//button[@id = "nextStateCont"]'
    input_descCtaAcredit = '//input[@id = "textField04"]'
    check_agregar_destinatario = '//table[@id = "tableAlign0"]/tbody/tr/td'
    list_concepto = "//select[@id='TELECTFIELD']"
    opt_concepto = "//select[@id='TELECTFIELD']//option[contains(.,'{}')]"
    opt_concepto2 = "(//select[@id='TELECTFIELD']//option[contains(.,'Op. inmobiliarias')])[2]"
    inputDescConcepto = "//input[contains(@caption,'n concepto')]"
    inputImporte = "//input[contains(@caption,'Importe')]"
    list_moneda = '//select[@id="selectFiel"]'
    checkEnviarAviso = (
        "descendant::input[@caption='Enviar aviso al destinatario'][1]"
    )
    inputEmail = '//input[@id="t7ujiu"]'
    inputComentario = '//textarea[@id="textArea0"]'
    checkProgramar = "descendant::input[@caption='Programar transferencia'][1]"
    declaJurada = "descendant::input[@caption='Agendar destinatario'][2]"
    list_periodicidad = "//select[@id = 'nextStatePerioricidad']"
    input_dia = '//input[contains(@class,"date-field_medium_label-medium")]'
    list_repeticiones = (
        '//select[contains(@class, "option-field_medium_label-medium")]'
    )
    cmdCancelar = "descendant::button[contains(.,'Cancelar')][1]"
    cmdLimitesDiarios = "//button[contains(.,'mites diarios')]"
    cmdContinuar = "//button[contains(.,'Continuar')]"
    cmdCotizaciones = "//button[contains(.,'Cotizaciones')]"
    cmdCerrar = "//button[contains(.,'Cerrar')]"
    table_tabla = "//label[@id = 'constantLabel0']"
    check_concepto = '//*[@id="conceptsCodeCheckField2"]'
    # #################### Segunda pagina #########################
    label_coordenadas = (
        "//span[@class='text-field_nobox_nolabel_padding-right-10']"
    )
    input_coordenada1 = "//input[@id='intFiedlCor1']"
    input_coordenada2 = "//input[@id='intFiedlCor2']"

    fechaVenc = "//*[@id='fechaVencimiento']"
    
    input_clave = "//input[@id = 'textFieldPin']"

    input_fecha = "//*[contains(@title,'DD/MM/YYYY')]"

    cmd_confirmar = "//button[contains(.,'Confirmar')]"
    # ############################ Tercera pagina ############################
    table_comprobante = "//table[@id='tableAlign07']"
    check_enviar_mail = '//table[@id="tableAlign0ee"]/tbody/tr/td'
    input_enviar_mail = "//input[@id='texto']"
    textarea_comentario = "//textarea[@id='textArea079']"
    cmd_nueva_transferencia = "//button[contains(.,'Nueva transferencia')]"
    cmd_descargar = "//label[contains(.,'Descargar')]"

    table_Cuentas = '//*[@id="tableAlign065432"]'

    # verificacion

    validacion_error_cuenta = "//li[contains(.,'Cuenta de acreditac')]"

    enviar_aviso = "//table[@id='tableAlign098']/tbody/tr/td"
    input_aviso_email = "//input[@title='E-mail']"

    input_aviso_comentario = "//textarea[@title='Comentario']"

    validacion_email = "//li[contains(.,'E-mail debe ser v')]"

    validacion_error_dia = "//ul[contains(@class,'error-panel_list')]/li[contains(.,'El d')]"

    validacion_fecha_mayor = "//ul[contains(@class,'error-panel_list')]/li[contains(.,'debe ser una fecha mayor a')]"