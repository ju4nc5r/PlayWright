class plCajaSeguridad(object):
    titulo = (
        "//label[contains(@class,'title') and "
        "contains(text(),'caja de seguridad')]"
    )
    span_sucursal = "//table[@id='tableAlign3']//child::span"
    span_tamano = "//table[@id='tableAlign31']//child::span"
    span_vencimiento = "//table[@id='tableAlign32']//child::span"
    span_periodo = "//table[@id='tableAlign34']//child::span"
    span_debito = "//table[@id='tableAlign35']//child::span"
