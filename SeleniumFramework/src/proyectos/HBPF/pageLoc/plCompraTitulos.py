from nt import P_DETACH
class plCompraTitulo(object):
    titulo = "//span[contains(@class,'title') and contains(.,'Compra de t')]"
    select_cuentaComitente = "//select[@caption='Cuenta comitente']"
    radio_bonosTitulos = "//input[@type='radio' and @value=1]"
    radio_acciones = "//input[@type='radio' and @value=2]"
    button_cancelar = "//button[contains(.,'Cancelar')]"
    input_letrasEspecie = "//input[contains(@caption,'letras de la especie')]"
    button_buscar = "//button[contains(.,'Buscar')]"
    div_error = "//div[@id='errorPanel' or @id='errorPanelCollection']"
    tabla_titulos = "//table[@class='collection-table_default']"
    opcion_titulo = (
        "//table[@class='collection-table_default']//"
        "child::td[contains(.,'{opcion}')]//parent::tr//child::input"
    )
    input_cantidadNominales = (
        "//input[contains(@caption,'Cantidad de nominales')]"
    )
    button_continuar = "//button[contains(.,'Continuar')]"
    button_continuar_2 = "//p[@class='autoAdjustText'][contains(.,'continuar')]"

    input_precioCompra = "//input[contains(@caption,'Precio')]"
    select_cantRueda = "//select[@caption='Cantidad de ruedas']"
    select_cuentaDebito = "//select[contains(@caption,'Cuenta de d')]"
    checkbox_aceptarTerminos = "//input[@type='checkbox']"
    button_modificar = "//button[contains(.,'Modificar')]"

    # Pantalla confirmacion
    span_especie = "//span[@id='textField04']"
    span_cantNominales = "//span[@id='floatField0']"
    span_precioCompra = (
        "//span[@id='floatField01' or @id='floatField01222']"
    )
    span_montoEstimado = "//span[@id='floatField02']"
    span_cantRueda = "//span[@id='selectField03']"
    span_comisionBanco = "//span[@id='floatField012']"
    span_comisionMinima = "//span[@id='floatField0121']"
    span_comisionMercado = "//span[@id='floatField01214d']"
    span_cuentaDebito = "//span[@id='selectField2']"
    span_cuentaComitente = "//span[@id='selectField01']"
    checkbox_terminosCond = "//input[@id='checkFiel88']"
    button_confirmar = "//button[contains(.,'Confirmar')]"

    # Pantalla de resultados
    span_nroOrden = "//span[@id='textField055']"
    span_fechaHora = "//span[@id='dateField01']"
    button_nuevaOperacion = "//button[contains(.,'Nueva operaci')]"
    
    # Advertencias 
    
    p_warnig = "//p[@class='error-panel_title'][contains(.,'La especie ingresada no pudo ser encontrada.')]"


    btn_continuar = "//p[contains(.,'Continuar')]"