class plRescate(object):
    titulo = (
        "//label[contains(@class,'title') and contains(.,'Rescate')]"
    )
    select_cuentaComitente = "//select[@caption='Cuenta comitente']"
    span_texto1 = "//span[@id='richText02']/p"
    span_texto2 = "//span[@id='richText023']/p"
    span_texto3 = "//span[@id='richText024']/p"
    tabla_alertaSinTenencia = "//table[@class='table_modal-alerta']"
    button_cerrar = "//button[contains(.,'Cerrar')]"
    table_fondosSeleccionables = (
        "//table[@class='collection-table_selectable']"
    )
    button_cancelar = "//button[contains(.,'cancelar')]"
    opcion_fondoSeleccionable = (
        "//table[@class='collection-table_selectable']//"
        "child::tr[contains(.,'{opcion}')]"
    )
    span_cuentaComitente = "//span[@class='select-field_nobox_nolabel']"
    span_fondoRescatar = "(//span[@class='text-field_nobox_nolabel'])[1]"
    select_cuentaAcreditacion = (
        "//select[contains(@caption,'Cuenta de acreditaci')]"
    )
    span_moneda = "(//span[@class='text-field_nobox_nolabel'])[2]"
    span_valorCuotaParte = "(//span[@class='float-field_nobox_nolabel'])[1]"
    span_salgo = "(//span[@class='float-field_nobox_nolabel'])[2]"
    radio_monto = "//input[@type='radio' and @value='monto']"
    radio_cuota = "//input[@type='radio' and @value='parcial']"
    radio_total = "//input[@type='radio' and @value='total']"
    input_monto = "//input[@id='floatMonto']"
    input_montoParcial = "//input[@id='floatParcial']"
    input_totalCuotaparte = "//input[@id='floatField1']"
    button_valorCuotaparte = "//button[@id='nextStateCuotapartes']"
    button_modificar = "//button[contains(.,'modificar')]"
    button_continuar = "//button[contains(.,'Continuar')]"
    table_valorCuotaparte = "//table[@class='table_modal']"
    button_cerrar = "//button[contains(.,'Cerrar')]"
    div_errorPanel = "//div[@id='errorPanel' or @id='errorPanelCollector]"

    # Pantalla de confirmacion
    textarea_info = "//textarea[@id='textAreaInfo']"
    span_declaracionSubtitulo = "//span[@id='richTextDecJurada']/p[1]"
    span_declaracionTexto = "//span[@id='richTextDecJurada']/p[2]"
    button_confirmar = "//button[@id='confirmar']"
    span_cuentaAcred = (
        "//label[@id='cuentaAcredit']//parent::td//following-sibling::td"
    )
    span_fechaEstimada = (
        "//label[contains(.,'Fecha estimada')]//parent::td//"
        "following-sibling::td//child::span"
    )
    span_cantCuotaparte = "//span[@id='floatParcial']"
    img_ticket = "//img[contains(@id,'imageComponent')]"
    checkbox_mail = "//input[@type='checkbox' and contains(@caption,'mail')]"
    button_nuevaOperacion = "//button[@id='nextStateNuevoRescate']"
    button_descargar = "//div[contains(@id,'download')]"

