class PlazoFijo(object):
    title_h3_constitucionPlazoFijo = (
        "//h3[contains(text(),'Plazo Fijo')]"
    )
    title_h1_constitucionPlazoFijo = "//label[@id='constantLabel0']"
    select_cuenta = "//select[@id='selectField0']"
    tipo_plazoFijo = "//select[@id='selectField20']"
    tipo_plazoFijoFlexible = "//option[contains(text(),'PF SELECTA FLEXIBLE')]"
    tipo_UVACancelable = "//option[contains(text(),'UVA - LEY 25.827 - PRECANCELABLE')]"
    tipo_plazoFijoClasico = "//option[contains(text(),'CLASICO SELECTA')]"
    tipo_plazoFijoUVA = "//option[contains(text(),'UVA - LEY 25.827 - NO PRECANCELABLE')]"

    span_moneda = "//span[@caption='Moneda']"
    input_plazo = "//input[@caption='Plazo']"
    input_vencimiento = "//input[@caption='Fecha de vencimiento']"
    input_montoInicial = "//input[@caption='Monto inicial']"
    button_simular = "//button[@id='nextStateSimular']"
    button_constituir = "//button[@id='nextStateConstNA']"
    button_confirmar = "//button[contains(.,'Confirmar')]"
    span_mensajeExito = "//span[contains(@class,'success')]"
    msgAltaOK = "//font[contains(.,'El plazo fijo fue dado de alta')]" 
    button_tasas = "//button[@id='nextStateTasas1']"
    div_error = "//div[contains(@id,'errorPanel')]"
    table_tasas = "//table[@id='table0' and @class='table_modal']"
    button_cerrar = "//button[contains(.,'Cerrar')]"
    button_nuevoPlazoFijo = "//*[@id='nextStateNuevoPF']"

    # Pantalla simulacion
    span_diaNoHabil = "//span[@id='richText0xx']/p"
    span_tna = "//span[@caption='TNA']"
    span_tea = "//span[@caption='TEA']"
    table_intereses = (
        "//td[contains(.,'Intereses a devengar') and "
        "@class='dataArea']//"
        "following-sibling::td/table"
    )
    # table_intereses = "//table[@id='tableAlign0010']"
    table_montoVencimiento = (
        "//td[contains(.,'Monto al vencimiento') and "
        "@class='dataArea']//"
        "following-sibling::td/table"
    )
    # table_montoVencimiento = "tableAlign126"
    # Pantalla simulacion con UVA
    span_montoInicial = "//span[contains(@caption,'Monto inicial')]"
    span_montoInicialUVA = (
        "//span[contains(@caption,'Monto inicial') and "
        "contains(@caption,'UVA')]"
    )
    span_valorUVA = "//span[contains(@caption,'Valor UVA')]"
    span_intereses2 = "//span[contains(@caption,'Intereses')]"
    span_montoVencimiento2 = (
        "//span[contains(@caption,'Monto al vencimiento')]")
    span_IIGG = "//span[contains(@caption,'IIGG')]"
    span_impuestoSello = "//span[@id='floatField64']"

    #Pantalla confirmacion
    span_tipoPlazoFijo = "//span[contains(@caption,'Tipo de plazo fijo')]"
    span_fechaConstitucion = "//span[contains(@caption,'Fecha de constituci')]"
    span_fechaVencimiento = "//span[contains(@caption,'Fecha de vencimiento')]"
    span_plazoInicial = "//span[contains(@caption,'Plazo inicial')]"
    span_cuentaDebito = "//span[contains(@caption,'Cuenta de d')]"
    span_cuentaAcreditacion = "//span[contains(@caption,'Cuenta de acredita')]"
    div_error_confirmacion = "//div[@id='errorPanelCollection']"
    span_impuestoSelloConfirmacion = (
        "//span[contains(@caption,'Impuesto de sellos')]"
    )
