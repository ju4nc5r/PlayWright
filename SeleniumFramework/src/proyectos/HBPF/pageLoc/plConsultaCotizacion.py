class plConsultaCotizacion(object):
    titulo = (
        "//label[contains(@class,'title') and "
        "contains(text(),'Consulta de Echeq')]"
    )
    
    dolar_compra = "//p[contains(.,'lar')]/../following-sibling::div[contains(@class,'card-monto')]/div[1]"
    dolar_venta = "//p[contains(.,'lar')]/../following-sibling::div[contains(@class,'card-monto')]/div[2]"

    euro_compra = "//p[contains(.,'Euro')]/../following-sibling::div[contains(@class,'card-monto')]/div[1]"
    euro_venta = "//p[contains(.,'Euro')]/../following-sibling::div[contains(@class,'card-monto')]/div[2]"

    real_compra = "//p[contains(.,'Real')]/../following-sibling::div[contains(@class,'card-monto')]/div[1]"
    real_venta = "//p[contains(.,'Real')]/../following-sibling::div[contains(@class,'card-monto')]/div[2]"