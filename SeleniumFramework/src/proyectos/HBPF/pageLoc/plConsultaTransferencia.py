class plConsultaTransferencia(object):
    titulo = (
        "//label[contains(.,'Consulta') and "
        "contains(.,'transferencias programadas')]"
    )
    label_tipoTransferencia = "//label[text()='Tipo de transferencia']"
    select_tipoTransferencia = "//select[@caption='Tipo de transferencia']"
    label_sinOperacion = (
        "//p[contains(.,'No ten') and "
        "contains(.,'s transferencias programadas')]"
    )
    table_resultados = "//table[@class = 'collection-table_selectable']"
    tr_opcionesTabla = "//tr[@id='collectionTablePropias_ON-REGISTER']"
    button_volver = "//button[contains(.,'Volver')]"
    button_programarTransferencia = (
        "//button[contains(.,'Programar Nueva Transferencia')]"
    )

    # Segunda pagina
    table_datosProgramacion = "(//table[@class = 'table-align_section'])[1]"
    label_cuentaDebito = "//label[contains(.,'Cuenta de d')]"
    span_cuentaDebito = "//span[contains(@caption,'Cuenta de d')]"
    label_cuentaAcreditacion = "//label[contains(.,'Cuenta de acreditaci')]"
    span_cuentaAcreditacion = (
        "(//span[contains(@caption,'Cuenta de acreditaci')]//following::td)[1]"
    )
    label_fechaSolicitud = "//label[contains(.,'Fecha de solicitud')]"
    span_fechaSolicitud = "//span[contains(@caption,'Fecha de solicitud')]"
    label_tipoTransferencia = "//label[contains(.,'Tipo de transferencia')]"
    span_tipoTransferencia = (
        "//span[contains(@caption,'Tipo de transferencia')]"
    )
    label_periodicidad = "//label[contains(.,'Periodicidad')]"
    span_periodicidad = "//span[contains(@caption,'Periodicidad')]"
    label_repeticiones = "//label[contains(.,'repeticiones')]"
    span_repeticiones = "//span[contains(@caption,'repeticiones')]"
    label_importe = "//label[contains(.,'Importe')]"
    span_importe = (
        "(//span[contains(@caption,'Importe')]//parent::div[1])[2]/span"
    )
    button_eliminar = "(//button[contains(.,'Eliminar')])[1]"
    table_detalleEjecuciones = "(//table[@class = 'table-align_section'])[2]"
    radio_opcionesEjecuciones = "//input[@type='radio']"
    button_eliminarRepeticion = "//button[contains(.,'Eliminar Repetici')]"

    # Tercera pagina
    label_numero = "//label[contains(.,'N') and contains(.,'mero')]"
    span_numero = (
        "//span[contains(@caption,'N') and contains(@caption,'mero')]"
    )
    label_fechaEjecucion = "//label[contains(.,'Fecha de ejecuci')]"
    span_fechaEjecucion = "//span[contains(@caption,'Fecha de ejecuci')]"
    label_estado = "//label[(.='Estado')]"
    span_estado = "//span[(@caption='Estado')]"
    button_confirmar = "//button[contains(.,'Confirmar')]"
