class plConsultaMovimientos(object):
    # Pantalla consulta movimientos
    titulo = "//label[text()='Consulta de movimientos']"
    label_cuenta = "//label[text()='Cuenta']"
    select_cuenta = "//select[@caption='Cuenta']"
    label_movimiento = "//label[text()='Movimiento']"
    select_movimiento = "//select[@caption='Movimiento']"
    button_volver = "//button[contains(.,'Volver')]"

    # # Si los movimientos no son los ultimos 20 movimientos
    input_importeDesde = "//input[@caption='Importe desde']"
    input_importeHasta = "//input[@caption='Importe hasta']"
    input_fechaDesde = "//input[@caption='Fecha desde']"
    input_fechaHasta = "//input[@caption='Fecha hasta']"
    button_buscar = "//button[contains(.,'BUSCAR')]"
    p_sinResultado = (
        "//p[@class='error-panel_title' and contains(.,'No hay info')]"
    )
    div_error = "//div[@id='errorPanel']"

    table_movimientos = "//table[contains(@class,'collection-table')]"
    img_visualizarMovimiento = (
        "//table[contains(@class,'table_default-top')]"
        "/tbody/tr[{}]//child::img"
    )
    
    # cuenta CA
    segunda_cuenta = "//option[contains(.,'CA U$S 0001781-201/8')]"

    # # Detalla de movimiento
    titulo_detalle = "//label[text()='Detalle de movimiento']"
    span_operacion = "//span[contains(@caption, 'Operaci')]"
    span_fecha_realizacion = "//span[contains(@caption, 'Fecha de realizaci')]"
    span_hora_realizacion = "//span[contains(@caption, 'Hora de realizaci')]"
    span_fecha_imputacion = "//span[contains(@caption, 'Fecha de imputaci')]"
    span_cuenta = "(//span[contains(@caption, 'Cuenta')])[3]"
    span_terminal = "//span[contains(@caption, 'Terminal')]"
    span_canal = "//span[contains(@caption, 'Canal')]"
    span_numReferencia = "//span[contains(@caption, 'Nro. de referencia')]"
    span_moneda = "//span[contains(@caption, 'Moneda')]"
    span_DebOCred = "//span[contains(@caption, 'bito')]"
    span_importe = "//span[@caption='Importe']"


    # error 
    no_movimientos = "//p[contains(.,'No se registran movimientos.')]"