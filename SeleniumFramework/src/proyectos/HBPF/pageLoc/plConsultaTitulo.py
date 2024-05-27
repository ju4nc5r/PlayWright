class plConsultaTitulo(object):
    titulo = (
        "//label[contains(@class,'title') and "
        "contains(text(),'Consulta de t')]"
    )
    sapn_sinProductos = "//span[@id='richcuentaszz']/p"
    button_volver = "//button[contains(.,'Volver')]"
    table_cuenta = "//div[@id='Inversiones']"
    option_cuentaTitulo = (
        "(//span[contains(.,'{cuenta}')]//"
        "ancestor::table[contains(@id,'Inversiones')])[1]//"
        "child::td[contains(@class,'collection') and "
        "contains(.,'{opcion}')]"
    )
    span_cuentaComitente = "//span[@id='textField1']"
    span_especie = "//span[@id='textField2']"
    span_codEspecie = "//span[@id='textField2as']"
    span_cupon = "//span[@id='textField20']"
    span_saldoValorizado = "//span[@id='floatField0']"
    span_tasaAmortizacion = "//span[@id='floatField1']"
    span_valorNominal = "//span[@id='floatField2']"
    span_valorResidual = "//span[@id='floatField3']"
    span_fechaUltCotizacion = "//span[@id='dateField0']"
    span_ultimaCotizacion = "//span[@id='floatField4']"
