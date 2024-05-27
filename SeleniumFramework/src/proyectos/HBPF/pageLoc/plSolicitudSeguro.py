class plSolicitudSeguro(object):
    
    titulo = ("//label[contains(@class,'title') and contains(.,'Solicitud de seguro')]")
#     titulo = (
#         "//label[contains(@class,'title') and "
#         "contains(.,'Solicitud de seguros')]"
#     )
    
    btn_seccion_seguro = "//button[contains(.,'{}')]"
    
    btn_contratar_tipo_seguro = "//div[@class='column-grande'][contains(.,'{}')]//button[contains(.,'Contratar')]"
    
    span_nombre = "//span[@caption='Nombre']"
    span_numDoc = "(//span[@unmasked='DNI' or @unmasked='LE'])[2]"
    select_seguro = "//select[@caption='Seguro']"
    span_lineaProd = "//span[@caption='Linea de producto']"
    span_producto = "//span[@caption='Producto']"
    table_planes = "//table[contains(@class,'collection-table')]"
    
    option_plan = "(//table[contains(@class,'collection-table')]//child::input)[{}]"  
      
#     option_plan = (
#         "//table[contains(@class,'collection-table')]//"
#         "child::tr[contains(.,'{plan}')]//child::input"
#     )
    button_cancelar = (
        "//button[contains(.,'cancelar') or contains(.,'Cancelar')]"
    )
    button_modificar = (
        "//button[contains(.,'modificar') or contains(.,'Modificar')]"
    )
    button_continuar = "//button[contains(.,'Continuar')]"
    button_confirmar = "//button[contains(.,'Confirmar')]"

    # carga de datos
    select_medioPago = "//select[@caption='Medio de pago']"
    select_cuenta = "//select[@caption='Cuenta']"
    select_tarjeta = "//select[@caption='Tarjeta']"
    span_edadMinima = (
        "//span[contains(@caption,'Edad') and contains(@caption,'nima')]"
    )
    span_edadMaxContratacion = (
        "//span[contains(@caption,'Edad') and "
        "contains(@caption,'xima de contrata')]"
    )
    span_edadMaxPermanencia = (
        "//span[contains(@caption,'Edad') and "
        "contains(@caption,'xima de permanencia')]"
    )
    checkbox_recibirInfo = (
        "//input[contains(@caption,'Deseo recibir informaci')]"
    )
    checkbox_termycond = "//*[@id='tableAlign098']//child::input"
    div_error = "//div[@id='errorPanel']"

    # Seguros hogar
    checkbox_igualTitular = (
        "//input[@type='checkbox' and contains(@caption,'Igual al Titular')]"
    )
    input_calle = "//input[@caption='Calle']"
    input_numero = "//input[@caption='Nro']"
    input_piso = "//input[@caption='Piso']"
    input_depto = "//input[@caption='Depto.']"
    input_codPostal = "//input[contains(@caption,'digo Postal')]"
    select_localidad = "//select[@caption='Localidad']"
    table_hogarAseguado = "//table[@id='tableAlign11']"

    # Pantalla de confirmacion
    span_plan = "//span[@caption='Plan']"
    span_sumaAsegurada = "//span[contains(@caption,'Suma asegurada')]"
    span_costo = "//span[@caption='Costo']"
    span_medioPago = "//span[@caption='Medio de Pago']"

    span_seguro = "//span[contains(@caption,'Producto') and contains(.,'{}')]"
    
    btn_seguro_option = "//select[@caption='Seguro']//option[contains(.,'{}')]"
    
    img_ticket = "//img[contains(@class,'ticket')]"
    
    btn_descargar ="//label[contains(.,'Descargar')]"
    
    lb_titulo_itau_seguros = "//h1[contains(.,'Seguros para tu patrimonio')]"
    lb_titulo_itau_seguros_negocios = "//strong[contains(.,'Seguro integral de negocios')]"
    pdf_itau_seguros_pyme ="//embed[@type='application/pdf']"
    lb_titulo_itau_seguros_consorcios ="//h1[contains(.,'Consorcios')]"
    
    
    