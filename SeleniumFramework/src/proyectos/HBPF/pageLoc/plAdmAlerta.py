class plAdmAlert(object):
    titulo = (
        "//label[contains(@class,'title') and contains(text(),'de alertas')]"
    )
    # Pantalla de adm alertas
    checkbox = (
        "(//td[contains(@class,'collection-column_align-left_"
        "width530-no-lowercase_radio')])"
    )
    input_debitoAuto = "{}[1]/input".format(checkbox)
    input_devolucionDebAuto = "{}[2]/input".format(checkbox)
    input_RechazoDebAuto = "{}[3]/input".format(checkbox)
    input_acredSueldo = "{}[4]/input".format(checkbox)
    input_usoAcuerdo = "{}[5]/input".format(checkbox)
    input_vencimientoPlazoFijo = "{}[6]/input".format(checkbox)
    input_recepcionTransferencia = "{}[7]/input".format(checkbox)
    input_chequesRechazados = "{}[8]/input".format(checkbox)
    input_pagoCheques = "{}[9]/input".format(checkbox)
    input_extracciones = "{}[10]/input".format(checkbox)
    input_depositos = "{}[11]/input".format(checkbox)
    input_comprasDebito = "{}[12]/input".format(checkbox)
    input_vencimientoPrestamo = "{}[13]/input".format(checkbox)
    input_vencimientoVisa = "{}[14]/input".format(checkbox)
    input_vencimientoMaster = "{}[15]/input".format(checkbox)
    input_vencimientoPIN = "{}[16]/input".format(checkbox)
    input_seleccionarTodosCuentas = (
        "(//th[@class='collection-table_column_headerCheckboxButton'])[1]"
    )
    input_seleccionarTodosTarjetas = (
        "(//th[@class='collection-table_column_headerCheckboxButton'])[3]"
    )

    button_cancelar = "//button[contains(.,'Cancelar')]"
    button_continuar = "//button[contains(.,'Continuar')]"

    # Pantalla de confirmacion
    subtitulo_confirmacion = (
        "//label[contains(@class,'subtitle') and "
        "contains(text(),'activas las siguientes alertas')]"
    )
    span_sinAlertas = "//span[@id='noAlertas']"
    table_alertas = "//table[@id='collectionTable0_1']"
    option_alertas = "//table[@id='collectionTable0_1']/tbody//child::tr"
    button_confirmacion = "//button[contains(.,'confirmar')]"
    button_modificar = "//button[@id='corregir']"

    # Pantalla resultado
    img_ticket = "//img[@id = 'imageComponent0']"
    button_nuevaAlerta = "//button[@id='nextStateNueva']"
    button_descargar = "//div[@id='downloadLink0']"
