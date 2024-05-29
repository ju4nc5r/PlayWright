class plConsultaTC(object):
    titulo_esperado = ("//label[contains(@class,'title') and "
                       "contains(text(),'Detalle de tarjeta de cr')]")
    select_tarjeta = "//select[@caption='Tarjeta']"
    tablle_detalle = (
        "//table[@class='table-align_section' and contains(.,'Detalle')]"
    )
    button_adherirDebAuto = "//button[@id= 'actionButton03']"
    span_debAutomatico = ("//span[contains(@caption,'Adhesi') and "
                          "contains(@caption,'bito autom')]")
    span_stopDeb = "//span[@caption='Stop debit']"
    span_limCompra = "//span[contains(@caption,'mite de compra')]"
    span_modif_debito = "//span[contains(@class,'action-button_tertiary_texto')]"

    button_volver = "//button[contains(.,'Volver')]"
    button_bloqueo = "//button[@id='bloqueo']"
    button_reposicion = "//button[@id = 'reposicion']"
    button_pagar = "//button[@id = 'Pago']"
    button_cerrar = "//button[contains(.,'Cerrar')]"
    button_cancelar_bloqueo = "//*[@id='detalle']"
    button_cancelar_adherirDebAuto = "//*[@id='actionButtonBack']"

    tabla_bloqueo = "//table[@class='table_modal-alerta']"
    titulo_reposicion = (
        "//label[contains(@class,'title') and "
        "contains(text(),'Bloqueo/reposici')]"
    )
    titulo_pagar = (
        "//label[contains(@class,'title') and "
        "contains(text(),'Pago de tarjeta de cr')]"
    )
    a_pagosRealizadosPesos = "//a[contains(@id,'Pagos realizados $')]"
    a_pagosRealizadosDolar = "(//a[contains(@id,'Pagos realizados')])[2]"
    table_pagosRealizados = (
        "//table[@class='table_modal' and contains(.,'Pagos realizados')]"
    )

    div_error = "//div[@id='errorPanelCollection']"
    titulo_adicionales = "//*[@id='constantLabel7']"