class PagoTC():

    title_h1_PagoTC = (
        "//label[contains(@class,'constant-label_title') and "
        "contains(.,'Pago de tarjeta')]"
    )
    list_tc_option = (
    #    "//select[contains(@class,'select-field_large_label-large')]")
        "//*[@id='selectField03']")
    button_saldopesos = ("//button[@id='botUno']")
    button_saldodolares = ("//button[@id='botDos']")
    
    list_ctaDebito = ("//select[@id='selectField3']")
    option_OtroImporte = (
        "descendant::input[contains(@name,'radiobuttonField')][4]")
    input_OtroImporte = "//input[@id='floatFieldOtroImportePesos']"
    option_ImporteTotalDolar = (
        "//*[@id='radioButtonField670_opt_0']")
    cmdContinuar = (
        "//button[@id='actionButton0']"
    )
    cmdConfirmar = (
        "//button[contains(@type,'button') and contains(.,'Confirmar')]")
    spanClass_resultado = "//span[@class='step-process_text-in-icon']"
    cmdButton_descargar = (
        "//label[contains(@id,'downloadLink') and contains(.,'Descargar')]"
    )

    tblTable_CuentaSinTarjetaCredito = (
        "//table[@id='table1' and contains(.,'No ten') and "
        "contains(.,'s productos asociados')]"
    )
    tbl_saldoMayor = "//table[@id='table1']"
    button_CerrarSaldoMayor = (
        "//body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/span[1]/button[1]" 
    )
    tbl_debitoAutomaticoActivo = (
        "//*[@id='table0' and contains(.,'stop debit')]"
    )
    cmdButton_CerrarTable = "//*[@id='nextStateContinuar']"
    pnlErrorPanel = "//*[@id='errorPanel']"
    div_error = "//div[@id='errorPanelCollection']"
    option_ImporteMinimo = "//*[@id='radioButtonPagoMin_opt_0']"
    radio_importeTotalPesos = "//input[@type='radio' and @value='2']"
    radio_importeTotalDolar = "//input[@type='radio' and @value='3']"
    cmdButton_NuevoPago = "//*[@id='1actionButton0x']"
    cmdButton_continuar_Inicio = (
        "//*[@id='1actionButton0']")
    img_ticket = "//img[contains(@id,'image')]"
    lblExitoSinTkt = "//p[contains(.,'xito') and contains(.,'pero no se pudo generar el ticket.')]"
    input_enviarMail = (
        "//input[@type='checkbox' and contains(@caption,'mail a')]"
    )
    txt_PagoPesosHastaFecha = "//*[@id='floatField0']"
    txt_PagoDolaresHastaFecha = "//*[@id='floatField4']"
    button_cerrar = "//button[contains(.,'Cerrar')]"
    btn_continuar = "//button[@id='1actionButton0']"
    
    btn_anularPago = "//a[@id='anularPagoTC']"
