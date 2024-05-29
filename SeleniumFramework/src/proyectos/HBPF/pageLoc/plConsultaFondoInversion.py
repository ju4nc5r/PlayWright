class plConsutalFondoInversion(object):
    titulo = (
        "//label[contains(@class,'title') and "
        "contains(.,'Consulta de fondos comunes')]"
    )
    select_cuentaComitente = "//select[@caption='Cuenta comitente']"
    span_sinFondos = "//span[@id='richText0x']/p"
    button_volver = "//button[contains(.,'Volver')]"
    button_valorCuotaparte = "//button[@id='valorCuotaparte']"
    button_caracteristica = "//label[contains(.,'Caracter')]"
    table_cuotaParte = "//table[@id='table1']"
    button_cerrar = "//button[contains(.,'Cerrar')]"
    tabla_fondos = "//table[@id='collectionTable0']"
