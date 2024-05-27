# -*- coding: utf-8 -*-
class pl_MesaWebOperaciones():
    # Menu operaciones
    operaciones = "//a[@onclick='return false;'][contains(.,'Operaciones')]"
    acciones = "//a[@onclick='return false;'][contains(.,'Acciones')]"
    operaciones_genericas = "//a[contains(.,'Operaciones Genéricas')]"
    titulos = "//a[@onclick='return false;'][contains(.,'T')]"
    compra = "//a[@href='/tradingNS/pages/mesa/mainMesa.xhtml?op=COMPRA&ti=BONO'][contains(.,'Compra')]"
    compra_2 = "//a[@href='/tradingNS/pages/mesa/mainMesa.xhtml?op=COMPRA&ti=ACCION'][contains(.,'Compra')]"
    venta = "//a[@href='/tradingNS/pages/mesa/mainMesa.xhtml?op=VENTA&ti=ACCION'][contains(.,'Venta')]"
    venta_2 = "//a[@href='/tradingNS/pages/mesa/mainMesa.xhtml?op=VENTA&ti=BONO'][contains(.,'Venta')]"
    
    
    #Lista de clientes venta
    lista_cliente = "//select[contains(@name,'formCliente:j_id_38')]"
    lista_cliente_2 = "//select[contains(@name,'formCliente:j_id_39')]"
    input_cliente = "//input[@type='text']"
    tipo_cliente_Nom = "//option[@value='NOMBRE'][contains(.,'Nombre/Razón Social')]"
    tipo_cliente_Nro = "//option[@value='NRO_CLI'][contains(.,'Nro. Cliente')]"
    tipo_cliente_CUIT = "//option[@value='CUIT'][contains(.,'CUIT')]"
    tipo_cliente_CUIL = "//option[@value='CUIL'][contains(.,'CUIL')]"
    tipo_cliente_Doc = "//option[@value='DOCUMENTO'][contains(.,'Documento')]"
    
    btn_buscarCliente ="//input[contains(@name,'formCliente:applyFiltersButton')]"
    btn_seleccionar  = "(//input[contains(@value,'Seleccionar')])[5]"
    btn_seleccionar_2  = "//input[contains(@name,'j_id_mi:j_id_ml:1:j_id_n4')]"
    btn_seleccionar_3 = "//input[contains(@name,'j_id_cv:j_id_cy:0:j_id_df')]"
    
    # Boton selecccionar asociado a datos
    select_Nom_Razon_social = "//input[contains(@name,'j_id_ln:j_id_lq:0:j_id_m8')]"
    select_cuenta= "//input[contains(@name,'j_id_mi:j_id_ml:0:j_id_n4')]"
    
    #Boton siguiente genérico
    btn_siguiente = "//input[contains(@value,'Siguiente')]"
    
    #boton venta del banco
    btn_venta_banco = "//input[contains(@name,'formPreOrden:btnVentaBanco')]"
    
    #boton aceptar generico
    btn_aceptar = "//span[contains(.,'Aceptar')]"
    
    #boton aceptar orden de venta    
    btn_aceptar_ord_venta= "//input[contains(@name,'formOrden:j_id_ft:j_id_fz')]"
    
    #contenedores de datos
    contains_automatizacion= "(//td[contains(.,'AUTOMATIZACIÓN MESA WEB')])[2]"

    contains_empresa_alfa_10= "(//span[contains(.,'EMPRESA ALFA10 - 6411')])[2]"
    
    msj_no_posee_clasificacion = "//li[contains(.,'El cliente no posee clasificación')]"

    contains_cuenta="//span[@class='centerColumn'][contains(.,'00000000098')]"
    
    #lista de instrumentos
    #lista_instrumentos = "//input[@name='selectInstrumento']"
    lista_instrumentos = "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[1]/form[1]/span[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]/div[1]/div[1]/input[1]"
    autocompletar_instrumento = "(//ul[contains(@class,'ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all')])[3]"
    
    #Cantidad
    cantidad_VN= "//input[contains(@name,'formPreOrden:inputCantidad')]"

    cantidad_VN_2= "//input[@name='cantidadId']"

    
    readro_instrumentos = "//input[contains(@name,'selectInstrumento')]"
    #Ultimo precio
    
    ultimo_precio = "(//td[contains(.,'Ult. Pcio. Oper.$')])[3]"
    precio = "//input[contains(@name,'formPreOrden:inputPrecio')]"
    precio_2 = "//input[contains(@name,'precioId')]"

    #Numero de orden
    
    nro_orden = "/html[1]/body[1]/div[1]/div[2]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/span[1]"
   
   #boton compra de banco
   
    btn_compra_banco = "//input[contains(@name,'formPreOrden:btnCompraBanco')]"
    
    item = "//a[contains(.,'AO20 - BONO NAC ARG USD 8 BONAR20')]"
    
    #boton aceptar
    
    
    btn_aceptar_1 = "//input[contains(@name,'formOrden:j_id_ft:j_id_fz')]"
    
    btn_aceptar_orden = "//span[contains(.,'Aceptar')]"
    
    #boton aceptar
    
    btn_mostrar_orden = "//a[contains(.,'Mostrar datos de la orden para Imprimir')]"

  
    #checkbox
    check_box = "//input[contains(@type,'checkbox')]"

    
    
    #mensaje exito 
    
    msj_la_orden_exito = "//label[@class='title2'][contains(.,'La orden se dio de alta')]"
     
    btn_imprimir = "//a[contains(@onclick,'javascript: window.print();')]"
    
    btn_ir_a_bandeja = "//a[contains(.,'Ir a Bandeja')]"
    
    #ITEM 
    
    recuadro_seleccionar = "//select[contains(@name,'selectEspeciePago')]"
    
    item_moneda = "//option[@value='2'][contains(.,'{}')]"
    
    item_si = "//option[@value='true'][contains(.,'{}')]"
    
    item_no = "//option[@value='false'][contains(.,'{}')]"

    recuadro_mercado = "//select[contains(@name,'selectMercado')]"
    
    recuadro_tipo = "//select[contains(@name,'selectTipoOperacion')]"
    
    recuadro_especie_pago = "//select[contains(@name,'selectEspeciePago')]"

    recuadro_carpeta_propia = "//select[contains(@name,'j_id_81')]"

    check_referencia_mae = "//input[contains(@name,'checkRefNum')]"

    check_orden_mae = "//input[contains(@name,'checkNroOrdenMae')]"
 
    item_moneda_us = "//option[@value='U$S'][contains(.,'U$S')]"
    
    item_vnta = "//option[@value='Vnta'][contains(.,'Vnta')]"

    item_merval = "//option[@value='MERVAL'][contains(.,'MERVAL')]"
    
    item_mae = "//option[@value='MAE'][contains(.,'MAE')]"

    imput_instrumento = "//input[contains(@name,'selectEspecie')]"
    
    item_al30 = "//a[@class='ui-corner-all ui-state-focus'][contains(.,'AL30')]"
    
    btn_aceptar = "//span[@class='ui-button-text'][contains(.,'Aceptar')]"

    btn_aceptar_2 = "//input[contains(@name,'j_id_c8:j_id_ce')]"

    btn_operaciones_2 = "//span[@class='ui-button-text'][contains(.,'Operaciones')]"
    
    label_cambio = "//span[@class='ui-button-text'][contains(.,'Operaciones')]"

    nro_operacion = "(//td[contains(.,'{}')])[1]"
    
    btn_editar= "(//i[contains(@class,'fa fa-pencil')])[2]"

    recuadro_book= "//select[contains(@name,'j_id_c6:editBook')]"
    
    recuadro_estrategia= "//select[contains(@name,'j_id_c6:selectEstrategia')]"
    
    item_banking = "//option[@value='2'][contains(.,'BANKING')]"
    
    item_banca_patrimonial = "//option[@value='7'][contains(.,'BANCA PATRIMONIAL')]"
    
    btn_aceptar_3 = "//input[contains(@name,'j_id_c6:j_id_gr')]"
    
    btn_cerrar_detalles= "//span[contains(@class,'ui-button-icon-primary ui-icon ui-icon-closethick')]"

    btn_detalles = "(//i[contains(@class,'fa fa-search-plus')])[1]"



    
    
