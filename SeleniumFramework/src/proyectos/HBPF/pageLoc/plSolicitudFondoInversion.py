class plSolicitudFondoInversion(object):
    titulo = (
        "//label[contains(@class,'title') and contains(text(),'Suscripci')]"
    )
    button_confirmar = "//button[@id='nextStateConfirmar']"
    continuar = "//button[@id='nextStateContinuar']"
    check_acuerdo= "//input[@id='checkFiel90']"
    importe = "//input[@id='floatField01']"
    cuentaDebito = "//select[@id='selectField1']"
    select_cuentaComitente = "//select[@caption='Cuenta comitente']"
    button_cancelar = "//button[contains(.,'Cancelar')]"
    button_continuar = "//button[@id='nextStateCuentaComitenteBis']"
    span_texto0 = "//span[@id='richText0']/p"
    span_texto1 = "//span[@id='richText0x']/p"
    span_texto2 = "//span[@id='richText01']/p"
    goal_pesos_A = "//div[contains(text(),'GOAL PESOS A')]"
    button_goalpesos_A = "//tbody/tr[7]/td[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/a[1]/img[1]"
    #goal_renta_dolar_estrA = "//tbody/tr[7]/td[1]/div[1]/div[4]/div[1]"
    goal_renta_dolares_plus = "//div[contains(text(),'GOAL RENTA DOLARES PLUS A')]"
    goal_renta_dolares_A = "//div[contains(text(),'GOAL RENTA DOLARES A')]"
    goal_renta_pesos_clase_A = "//div[contains(text(),'GOAL RENTA PESOS CLASE A')]"
    goal_renta_global = "//div[contains(text(),'GOAL RENTA GLOBAL (PESOS)')]"
    button_caracteristica = "//a[contains(text(),'caracteristicas de nuestros fondos')]"
    option_fondos = (
        "//table[@id='collectionTable0']/tbody//"
        "child::tr[contains(.,'{opcion}')]"
    )
    noHayFondos = "//div[contains(text(),'No hay fondos con {} que cumplan los criterios seleccionados')]"
    
