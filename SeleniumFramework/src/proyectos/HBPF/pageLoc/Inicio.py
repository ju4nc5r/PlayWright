class Inicio(object):
    span_identificador_PersonalBank_xp = (
        ".//*[@id='section3_repeat0_textField0123' and "
        "contains(.,'Personal') and contains(.,'Bank')]"
    )
#     span_identificador_310_xp = "//span[@id='c3richText03ddd']/p"
    span_identificador_310_xp = "//td[@class='collection-column_align-left_tarjetas_200 left-align']"
    tbl_Titulo_Tarjetas_xp = (
        "//*[@id='section44_repeat0_collectionTable183_ON-REGISTER']")
    btn_Inversiones_despliegue_xp = "//*[@id='actionButton011031']"
    span_Inversiones_310_xp = "//*[@id='c3richText03ddd2']/p"
    table_inversiones = (
        "(//table[contains(.,'Inversiones') and "
        "contains(@class,'colapsable')]//"
        "table[@class='table-align_wrap-nowidth'])[2]"
    )

    btn_Prestamos_despliegue_xp = "//button[@id='actionButton0111']"
    span_Prestamos_310_xp = "//*[@id='3richText0225']/p"
    span_prestamos = (
        "//table[contains(@id,'Prestamo') "
        "and @class='collection-table_selectable']"
        "//child::tr[contains(.,'{prestamo}')]"
    )
    table_prestamos = "//div[@id='sectionPrestamos']"
    table_sin_prestamos = (
        "//table[contains(.,'stamos') and contains(@class,'colapsable')]//"
        "table[contains(@class,'seg-mensaje')]"
    )
    btn_Caja_despliegue_xp = "//button[@id='2actionButton0110']"
    lbl_Caja_No_Disponible_xp = (
        "//table[contains(.,'Cajas de seguridad') and "
        "contains(@class,'colapsable')]//"
        "table[contains(@class,'seg-mensaje')]"
    )
    table_cajasSeguridad = "//table[contains(@id,'sectionCajas')]"
    lbl_Sin_Cajas_xp = "//*[@id='3richText03']/p[1]"
    btn_Seguros_despliegue_xp = "//button[@id='12actionButton0111']"
    table_seguros = "//div[@id='sectionSeguros']"
    table_sin_seguros = (
        "//table[contains(.,'Seguros') and contains(@class,'colapsable')]//"
        "table[contains(@class,'seg-mensaje')]"
    )
    lbl_Seguros_310_xp = (
        "//*[@id='sectionSeguros_repeat0_collectionTableInsurence_"
        "ON-REGISTER']")

    lbl_Titulo_Cuentas_xp = "//*[@id='constantLabel0']"
    tbl_Contenedor_Cuentas_xp = (
        "//*[@id='section3_repeat0_collectionTable0_ON-REGISTER' and "
        "contains(.,'{}')]"
    )
    btn_Cuentas_pliegue_xp = "//button[@id='actionButton01112']"
    btn_Cuentas_despliegue = "//button[@id='actionButton011']"
    btn_Tarjetas_pliegue_xp = "//button[@id='actionButton011125']"

    span_tarjetaDebito = (
        "//table[contains(.,'Tarjetas') and contains(@class,'colapsable')]//"
        "child::tr[@class='evenRow' and contains(.,'Debit') and "
        "contains(.,'{}')]"
    )
    span_tarjetaCredito = (
        "//table[contains(.,'Tarjetas') and contains(@class,'colapsable')]//"
        "child::table[contains(.,'tarjeta de cr') and "
        "contains(@class,'tarjetas-consolidada')]//"
        "child::tr[contains(.,'{}')]"
    )

    option_cajaSeguridad = (
        "//table[contains(@id,'sectionCajas') and "
        "contains(@class,'table_selectable')]//"
        "child::td[contains(.,'{caja}')]"
    )

    table_cuentas = (
        "//table[contains(@class,'colapsable') and contains(.,'Cuentas')]//"
        "table[contains(@class,'consolidada_collection')]"
    )
    table_tarjetas = (
        "//table[contains(@class,'colapsable') and contains(.,'Tarjetas')]//"
        "table[contains(@class,'consolidada_collection')]"
    )
    option_administracionAlertas = (
        "//p[contains(.,'Administraci') and contains(.,'de alertas')]"
    )
    
    btn_Vencimientos = (
        "//*[@id='rightPanelItau']/div[3]/p")
