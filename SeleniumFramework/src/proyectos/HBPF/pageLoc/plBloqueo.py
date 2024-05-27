class plBloqueo(object):
    titulo = (
        "//label[contains(@class,'title') and "
        "contains(text(),'Bloqueo/reposici')]"
    )
    select_motivo = "//select[contains(@caption,'Motivo')]"
    select_tipoTarjeta = "//select[contains(@caption,'tipo de tarjeta')]"
    select_cuenta = "//select[contains(@caption,'Cuenta')]"
    span_nombre = "//span[contains(@caption,'Nombre en la tarjeta')]"
    span_domicilio = "//span[contains(@caption,'Domicilio')]"
    button_continuar = "//button[contains(.,'Continuar')]"
    button_cancelar = "//button[contains(.,'Cancelar')]"

    # Pantalla de confirmacion
    span_cuenta = "//span[contains(@caption,'Paquete')]"
    span_titular = "//span[contains(@caption,'Titular')]"
    span_operacion = "//span[contains(@caption,'Operacion')]"
    button_modificar = "//button[contains(.,'Modificar')]"
