class plSolicitudSeguroTarjeta(object):
    titulo = (
        "//label[contains(@class,'title') and text()='Solicitud de seguros']")
    span_nombre = "//span[@caption='Nombre']"
    span_tipoDoc = "(//span[@unmasked='DNI'])[1]"
    span_numDoc = "(//span[@unmasked='DNI'])[2]"
    span_lineaProducto = "//span[@caption='Linea de producto']"
    span_producto = "//span[@caption='Producto']"
    select_medioDePago = "//select[@caption='Medio de pago']"
    select_cuenta = "//select[@caption='Cuenta']"
    input_terminosYCondicion = "//input[@id='checkField02']"
    button_cancelar = "//button[@id='Cancelar']"
    button_modificar = (
        "//button[contains(.,'Modificar') or contains(.,'modificar')]"
    )
    button_continuar = "//button[contains(@id,'Continuar')]"

    # Pantalla de confirmacion
    subtitulo = "//label[contains(@class,'subtitulo')]"
    span_plan = "//span[@caption='Plan']"
    span_sumaAsegurada = "//span[contains(@caption,'Suma asegurada')]"
    span_costo = "//span[contains(@caption,'Costo')]"
    span_medioDePago = "//span[contains(@caption,'Medio de Pago')]"
