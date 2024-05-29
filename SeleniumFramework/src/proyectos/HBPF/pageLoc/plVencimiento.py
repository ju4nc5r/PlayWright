class plVencimiento(object):
    btn_ItauTarjetas = "//*[@id='tab3']"
    table_tarjetas = "//table[contains(.,'tarjeta') and @id='tableAlign2']"
    first_card = "//option[contains(.,'0004695-301/5')]"

    btn_ItauPrestamos = "//*[@id='nextState_Prestamos']"
    table_prestamos = "//table[@id='collectionTable02']"
    span_sinPrestamos = "//span[@id='prestamos']/p"

    btn_ItauDebitoAutomatico = "//*[@id='nextState_sig']"
    span_sinDebitoAutomatico = "//span[@id='richText033']/p"

    btn_PagoMisCuentas = "//*[@id='nextState_Pagomiscuentas']"
    span_sinPagoMisCuentas = "//span[@id='richText0xx0']/p"

    btn_ServiciosVisa = "//*[@id='irPagoVisa']"
    span_sinServicioVisa = "//span[@id='noCuentas']/p"

    btn_Volver = "//*[@id='actionButton2']"
    btn_AdherirServicio = "//*[@id='actionButton1']"
    txt_sinVencimientos = "//*[@id='richText033']/p"
