class ConsultaCanjePuntos():
    span_puntos = "//span[contains(@id,'BINTPuntosSUGA')]"
    span_puntos_other = "//button[contains(@id,'menu_usuario')]//span"

    btn_volver = "//button[contains(@id,'cancelar')]"
    btn_ingresar = "//button[contains(@id,'actionButton0')]"
    btn_continuar = "//label[contains(@id,'constantLabel0') and contains(.,'Continuar')]"

    puntos_otherpage = "//button[contains(@id,'menu_usuario')]//span"