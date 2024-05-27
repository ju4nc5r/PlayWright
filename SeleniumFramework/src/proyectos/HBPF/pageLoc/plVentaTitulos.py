class plVentaTitulos(object):
    tabla_tipoCliente = "//table[contains(@class,'centered')]"
    button_noCalificado = (
        "//button[@id = 'nextState' and contains(.,'No calificado')]"
    )
    button_calificado = (
        "//button[@id='nextState1' and contains(.,'Calificado')]"
    )
    button_domicilioExt = (
        "//button[@id = 'nextState9' and "
        "contains(.,'Domiciliado en el Extranjero')]"
    )
    button_cerrar = "//button[contains(.,'Cerrar')]"
    titulo = "//span[contains(@class,'title') and contains(.,'Venta de t')]"
    span_sinTitulos = "//span[@id='richText55']/p"
    select_cuentaAcreditacion = (
        "//select[contains(@caption,'Cuenta de acredita')]"
    )

    span_cantNominales = "//span[@id='floatField033w']"
    span_precioVenta = "//span[@id='wfloatField010' or @id='floatField01ww']"
    span_montoEstimado = "//span[@id='oculto']"
    span_cuentaAcreditacion = "//span[@id='selectField2']"
    table_acciones = "(//table[@class='collection-table_default'])[2]"
    option_accion = (
        "//td[contains(.,'{accion}') and contains(@class,'column')]"
        "//parent::tr//child::input"
    )
