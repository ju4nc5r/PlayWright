class plConsultaEcheq(object):
    titulo = (
        "//label[contains(@class,'title') and "
        "contains(text(),'Consulta de Echeq')]"
    )
    tbl_echeqs = "//table[contains(@id,'collectionTable0')]"

    tbl_detalles = "//table[@id='tableAlign0']"

    col_estado = "//tr[@id='collectionTable0_ON-REGISTER']//td[contains(.,'{}')]"