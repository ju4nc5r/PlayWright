class CambioClave():
    # Cambio de clave
    # Encontrado en el menu de perfil
    titulo = (
        "//label[contains(@class,'title') and contains(.,'Cambio de clave')]"
    )
    check_PC_Publica_xp = "//*[@id='checkField0']"
    text_ClaveActual_xp = "//*[@id='textField1']"
    text_ClaveNueva_xp = "//*[@id='textField2']"
    text_Repetir_ClaveNueva_xp = "//*[@id='textField3']"
    btn_Confirmar_xp = "//*[@id='Continuar']"
    btn_Cancelar_xp = "//*[@id='actionButton0']"
    lbl_Error_xp = "//*[@id='errorPanelCollection']"
    lbl_Error_2_xp = "//*[@id='errorPanel']"
    img_Ticket = "//img[contains(@id,'imageComponent0')]"
