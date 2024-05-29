class CompraVenta():

#     tile_h1_compra_venta_monteda = 
#     (
# #         "//label[contains(.,'Transferencia entre cuentas propias - "
# #         "compra/venta de moneda extranjera')]")

    tile_h1_compra_venta_monteda ="//label[contains(@class,'title')]"

    list_cta_comitente = "//select[@id='selectField0']"
    list_cta_debito_item = "//select[contains(@caption,'Cuenta de d')]"
    list_cta_acreditacion_item = (
        "//select[contains(@caption,'Cuenta de acreditaci')]")
    input_importe = "//input[@caption='Importe']"
    input_monto = "//input[@id='Monto']"
    list_tipoMoneda_item = "//select[contains(@title,'Moneda')]"
    select_tipoMoneda_item = "//select[contains(@title,'Moneda')]/option[contains(.,'{}')]"
    cmdButtonContinuar = "//button[contains(.,'Continuar')]"
    span_top_confirmacion = "//span[contains(.,'confirmaci')]"
    cmdButtonConfirmar = "//button[contains(@id,'actionButtonConfirmar')]"
    #span_top_Resultadoor = "//span[contains(.,'resultado')]"
    span_top_Resultado = "//span[contains(text(),'03. Resultado')]"
    cmdButtonContinuar_a_cuentas = (
        "//button[contains(@id,'actionButton') and contains(.,'Continuar')]")
    btn_lim_diario = "//button[@id='actionButton0']"
    tbl_lim_diario = "//table[@class='table_modal']"
    btn_cerrar = "//button[contains(.,'Cerrar')]"
    div_error = "//div[@id='errorPanel']"
    input_programar = "//input[@type='checkbox']"
    select_programar = ("//select[contains(@caption,'Realizar esta "
                        "transferencia')]")
    input_fechaProgramada = "//input[contains(@caption,'El d')]"
    input_primeraFecha = "//input[contains(@caption,'Fecha primera')]"
    select_cantRepeticiones = "//select[@caption='Cantidad de repeticiones']"
    checkbox_acepto = (
        "//table[contains(.,'Acepto') and "
        "@class='table-align_wrap-nowidth']//child::input"
    )

    # Pantalla de confirmacion
    lbl_cuentaDebito = "//label[contains(.,'Cuenta de d')]"
    lbl_cuentaAcreditacion = "//label[contains(.,'Cuenta de acreditaci')]"
    lbl_importe = "//label[contains(.,'Importe')]"
    # # Campos para la pantalla de transferencia por unica vez
    tbl_RealizarTransferenciaUnica = "//table[contains(@id,'UnicaVez')]"
    # # Campos para pantalla de transferencia programada semanalmente
    tbl_primeraEjecucion = "//span[contains(@caption,'Fecha primera')]"
    tbl_diasSemanales = "//span[contains(@caption,'Los d')]"
    tbl_repeticionesProgramadas = (
                "//span[contains(@caption,'Cantidad de repeticiones')]")

    btn_cancelar = "//button[contains(.,'Cancelar')]"
    btn_modificar = "//button[contains(.,'Modificar')]"

    # Pantalla de resultado
    img_ticket = "//img[contains(@id,'image')]"
    input_enviarMail = "//input[contains(@caption,'Enviar')]"
    btn_descarga = "//label[@id='label_downloadLink1']"
    btn_nueva_transferencia = "//button[contains(.,'Nueva transferencia')]"

    btn_declaracion = "//input[contains(@name,'bool_field_checkFiel88')]"