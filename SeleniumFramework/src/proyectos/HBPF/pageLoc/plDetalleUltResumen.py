class plDetalleUltResumen(object):
    lbl_tituloUltimoResumen = (
        "//*[@id='constantLabel0' and contains(.,'ltimo')]"
    )
    img_resumen = "//img[@id='fileObject01_0']"
    select_tarjeta = "//select[@id='selectField03']"
    span_sinResumen = "//span[@id='richText']/p"
    button_volver = "//button[contains(.,'Volver')]"
    button_verResumen = "//p[contains(text(),'ver resumen')]"
    button_pagar = "//button[contains(.,'Pagar')]"
    button_descargar = "//label[contains(.,'Descargar')]"
    checkbox_enviarMail = "//input[@type='checkbox' and @id='checkField60']"
    div_error = "//div[@id='errorPanelCollection']"
