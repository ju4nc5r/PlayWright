class plAdhesionDebAuto(object):
    titulo = (
        "//label[contains(@class,'titulo') and contains(.,'Adhesi')]"
    )
    select_tarjeta = "//select[@caption='Tarjeta']"
    span_sinDebAuto = "//span[@id='richText0']/p"
    select_cuentaDebito = "//select[contains(@caption,'Cuenta de d')]"
    radio_pagoMinimo = (
        "//div[@class='radioButtonDiv' and contains(.,'Pago m')]//child::input"
    )
    radio_pagoTotal = (
        "//div[@class='radioButtonDiv' and contains(.,'Pago total')]"
        "//child::input"
    )
    button_continuar = "//button[contains(.,'Continuar')]"
    button_cancelar = "//button[contains(.,'Cancelar')]"
    div_error = "//div[@id='errorPanel']"

    # Pantalla de confirmacion
    span_tarjeta = "//span[@caption='Tarjeta']"
    span_cuentaDebito = "//span[contains(@caption,'Cuenta de d')]"
    span_importeDebitar = "//span[@caption='Importe a debitar']"
