class plResumenesAnteriores(object):
    lbl_tituloResumenesAnteriores = (
        "//*[@id='constantLabel0' and contains(.,'anteriores')]"
    )
    opt_TarjetasResumenesAnteriores = "//*[@id='nextStateBuscar2']"
    opt_TarjetasUltimoResumen = "//*[@id='selectField03']"
    div_error = "//div[@id='errorPanelCollection']"
    span_sinResumen = "//span[@id='Error' or @id='richText']/p"
