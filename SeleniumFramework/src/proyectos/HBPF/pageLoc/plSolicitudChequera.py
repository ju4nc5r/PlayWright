class plSolicitudChequera(object):
    titulo = (
        "//label[contains(@class, 'title') and "
        "contains(text(), 'Solicitud de chequeras')]"
    )
    select_cuenta = "//select[@caption='Cuenta']"
    input_chequerasPedir = "//input[contains(@caption,'chequeras a pedir')]"
    select_tipoCheques = (
        "//select[contains(@caption,'Tipo y cantidad de cheques')]"
    )
    input_domicilioParticular = "//input[@type='radio' and @value='DOMICILIO']"
    input_RetiroSucu = "//input[@type='radio' and @value='SUCURSAL']"
    input_radicacion = "//input[@type='radio' and @value=3]"
    input_otra = "//input[@type='radio' and @value=4]"
    button_cancelar = "//button[contains(.,'Cancelar')]"
    button_continuar = "//button[contains(.,'Continuar')]"
    div_error = "//div[@id='errorPanel']"
    select_sucursal = "//select[contains(@caption,'Sucursal')]"
    table_formaEntrega = (
        "//table[@class='table-align_section' and "
        "contains(.,'Forma de entrega')]"
    )
    # Tabla sucursales
    titulo_sucursales = (
        "//label[contains(@class,'title') and contains(.,'Sucursales')]"
    )
    input_sucursal = (
        "//tr[contains(.,'{codigo}') and "
        "(@class='evenRow' or @class='oddRow')]//child::input"
    )
    button_volver = "//button[contains(.,'Volver')]"
    button_aceptar = "//button[contains(.,'Aceptar')]"


    # Pantalla confirmacion
    span_cuenta = "//span[@caption='Cuenta']"
    span_cantChequera = "//span[contains(@caption,'chequeras a pedir')]"
    span_tipoCantCheques = "//span[contains(@caption,'cantidad de cheques')]"
    table_lugarEntrega = (
        "//table[@class='table-align_section' and "
        "contains(.,'Lugar de entrega')]"
    )

    msgSolicitudExistente = ("//label[@class='constant-label_modal-mensaje'][contains(.,'Para la cuenta seleccionada, existe una solicitud de chequera ya registrada.')]"
                                 )
    
    btnContinuarSiHaySolicitudExistente = "//button[contains(@class,'action-button_primary')]"
    
    input_3erGrupo4digTarj = "//input[contains(@type,'text')]"
    
    input_claveCajero = "//input[contains(@type,'password')]"
    
    btnConfirmar = "//p[@class='autoAdjustText'][contains(.,'Confirmar')]"
    
    imgTicketSolicChequera = "//img[contains(@class,'image-component_ticket')]"
    
    msgErrorClaveCajaero = "//p[@class='error-panel_title'][contains(.,'La clave de tu tarjeta de d') and contains(.,'ingresada es incorrecta')]"
    
    