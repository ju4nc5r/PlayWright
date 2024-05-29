class plComprobantes():
    titulo_esperado = "//label[contains(.,'comprobantes')]"

    # Pagina de consultas

    # Botones pago mis cuentas
    button_itau = "//button[@id='tab1']"
    button_visa = "//button[@id='Visa']"

    # Campos de operaciones 
    label_operaciones = (
        "//*[contains(@id,'label_selectField') and contains(.,'Operaci')]"
    )
    select_operaciones = "//select[contains(@caption, 'Operaci')]"

    # Campos fecha desde
    label_fecha_desde = (
        "//label[contains(@id, 'dateField') and contains(.,'desde')]"
    )
    input_fecha_desde = "//input[@caption='Fecha desde']"

    # Campos fecha hasta
    label_fecha_hasta = (
        "//label[contains(@id, 'dateField') and contains(.,'hasta')]"
    )
    input_fecha_hasta = "//input[@caption='Fecha hasta']"

    # Campos canal
    label_canal = "//label[contains(.,'Canal')]"
    select_canal = "//select[@caption='Canal']"

    # Campos numero de operacion
    label_num_operacion = "//label[contains(.,'mero de operaci')]"
    input_num_operacion = "//input[contains(@caption,'mero de operaci')]"

    # Botones inferiores
    button_volver = "//button[contains(.,'Volver')]"
    button_buscar = "//button[contains(.,'Buscar')]"

    # Tabla de resultados
    table_resultados = "//table[contains(.,'Tipo de operaci') and @pagenumber]"
    table_sin_resultados = "//span[@id='noCuentas']"
    img_primer_pdf = "(//*[@id='collectionTable0_DETAIL'])[1]/img"
    img_ticket = "//img[contains(@id,'image')]"

    # Mensaje de error
    div_error = "//div[@id='errorPanel']"
