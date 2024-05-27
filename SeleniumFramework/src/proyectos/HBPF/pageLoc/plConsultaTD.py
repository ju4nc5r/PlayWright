class plConsultaTD(object):
    titulo_consultaTD = (
        "//label[contains(@class,'title') and "
        "contains(.,'Detalle de tarjeta de d')]"
    )
    span_numTarjeta = "//span[contains(@caption,'mero de tarjeta')]"
    span_nomApellido = "//span[@caption='Nombre y apellido']"
    span_limDiario = "//span[contains(@caption,'mite diario')]"
    span_seguroContraRobo = "//span[@caption='Seguro contra robo en cajero']"

    button_volver = "//button[contains(.,'Volver')]"
    button_bloqueo = "//button[@id='bloqueo']"
    button_reposicion = "//button[@id='reposicion']"
    button_cuentaExterior = "//button[contains(.,'cuenta op. en el exterior')]"
    button_solicitarSeguro = (
        "//button[@class='action-button_link' and "
        "contains(.,'Solicitar seguro')]"
    )
