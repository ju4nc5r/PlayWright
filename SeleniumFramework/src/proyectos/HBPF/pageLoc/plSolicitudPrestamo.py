class plSolicitudPrestamo(object):
    titulo = (
        "//label[contains(@class,'title') and contains(.,'Solicitud de p')]"
    )
    span_nombre = "//span[@caption='Nombre']"
    span_numeroDocu = "//span[@id='textField122']"
    select_prestamo = (
        "//select[contains(@caption,'Pr') and contains(@caption,'stamo')]"
    )
    button_volver = "//button[contains(.,'Volver')]"
    table_prestamoNoDisponible = (
        "(//table[@id='tableAlignNuevo']//ancestor::table)[1]"
    )
    select_prestamo3 = "//select[contains(@class,'select-field_large_label-large')]/option[contains(.,'{}')]"

    # Pantalla carga de datps
    span_lineaProducto = "//span[contains(@caption,'nea de producto')]"
    span_producto = "//span[@caption='Producto']"
    span_cuenta = "//span[@id='textField0ae']"
    select_prestamo2 = "//select[@id='selectField0']"
    span_moneda = "//span[@caption='Moneda']"
    select_cuotas = "//select[@caption='Cantidad de cuotas']"
    span_montoMaximo = "//span[contains(@caption,'Monto m')]"
    input_montoSolicitado = "//input[@caption='Monto solicitado']"
    select_vencimientoCuotas = (
        "//select[contains(@caption,'vencimiento de cuotas')]"
    )
    select_cuentaAcred = (
        "//select[contains(@caption,'Cuenta de acreditaci')]"
    )
    select_cuentaDeb = "//select[contains(@caption,'Cuenta de d')]"
    select_destinoPrestamo = "//select[contains(@caption,'Destino del pr')]"
    input_checkboxTerminos = "//input[@type='checkbox']"
    button_cancelar = "//button[contains(.,'cancelar')]"
    button_simular = "//button[contains(.,'Simular')]"
    button_composicionCuota = "//button[@id='nextStateComposicion']"
    button_continuar = "//button[contains(.,'Continuar')]"

    label_tituloTablaSimulacion = (
        "//label[contains(@class,'title') and contains(.,'Simulaci')]"
    )
    label_tituloTablaComposicionCuotas = (
        "//label[contains(@class,'title') and contains(.,'Composici')]"
    )
    button_cerrar = "//button[contains(.,'cerrar')]"

    # Pantalla de confirmacion
    input_pin = "//input[@id='textFieldPin']"
    span_prestamo = "//span[@id='textField0sa']"
    span_moneda = "//span[@caption='Moneda']"
    span_cuotas = "//span[@caption='Cantidad de cuotas']"
    span_montoSolicitado = "//span[@caption='Monto solicitado']"
    span_importePrimCuota = "//span[@caption='Importe de la 1er cuota']"
    span_vencimientoPrimCuota = (
        "//span[@caption='Vencimiento de la 1era cuota']"
    )
    span_tasaPrestamo = "//span[contains(@caption,'Tasa del ')]"
    span_gastosImpuestos = "//span[@caption='Gastos de otorgamiento']"
    span_iva = "//span[@caption='IVA sobre gastos:']"
    span_montoAcreditar = "//span[@caption='Monto a acreditar']"
    span_cuentaAcred = "//span[contains(@caption,'Cuenta de acredita')]"
    span_cuentaDeb = "//span[contains(@caption,'Cuenta de d')]"
    span_diaVencimiento = "//span[contains(@caption,'vencimiento de cuotas')]"
    span_destinoPrestamo = "//span[contains(@caption,'Destino del pr')]"
    span_tna = "//span[@caption='TNA']"
    span_tea = "//span[@caption='TEA']"
    span_cftea = "//span[@caption='CFTNA']"
    button_modificar = "//button[contains(@id,'Corregir')]"
    input_tercerCuarto = "//input[contains(@id,'fechaVencimiento')]"
    input_pin = "//input[contains(@id,'textFieldPin')]"
    btn_confirmar = "//button[contains(.,'Confirmar')]"
    img_ticket = "//img[contains(@id,'image')]"
    ipt_a_solicitar = "//input[@id='floatField00']"
    slc_a_pagar = "//select[@caption='a pagar en']"