class plExtracciones(object):
    titulo = (
        "//label[contains(@class, 'title') and "
        "contains(text(), 'Extracci')]"
    )

    titulo_consulta = "//label[contains(@class, 'title') and contains(text(), 'Consulta')]"
    ipt_monto = "//input[contains(@caption,'Importe')]"

    btn_continuar = "//button[contains(.,'continuar')]"

    btn_continuar_2 = "//button[contains(.,'Continuar')]"

    btn_confirmar = "//button[contains(.,'confirmar')]"

    btn_volver = "//button[@id='actionButton100']"

    input_checkboxTerminos = "//input[@type='checkbox']"

    img_ticket = "//img[contains(@id,'image')]"

    first_row_registros = "//tr[contains(@id,'collectionTable031235xx3_ON-REGISTER')][1]//td[contains(.,'Pendiente')]"
    second_row_registros = "//tr[contains(@id,'collectionTable031235xx3_ON-REGISTER')][2]//td[contains(.,'Pendiente')]"
    row_random = "//tr[contains(@id,'collectionTable031235xx3_ON-REGISTER')][5]//td[contains(.,'Vencido')]"

    row_pendiente = "//span[contains(.,'Pendiente')]//ancestor::table[contains(@id,'tableAlign3')]"

    btn_otra_persona = "//button[contains(@id,'otraPersona')]"

    ipt_num_dc = "//input[contains(@id,'textField0')]"