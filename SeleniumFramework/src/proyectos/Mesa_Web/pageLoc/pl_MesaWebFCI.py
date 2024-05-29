# -*- coding: utf-8 -*-
class pl_MesaWebFCI():
    # Menu operaciones
    FCI = "//a[contains(.,'FCI')]"
    liquidacion = "//a[@onclick='return false;'][contains(.,'Liquidación')]"
    movimiento = "//a[@onclick='return false;'][contains(.,'Movimientos')]"
    movimiento_a_imputar = "//a[contains(.,'Movimientos a Imputar')]"
    procesos = "//a[@onclick='return false;'][contains(.,'Procesos')]"
    acciones = "//a[@onclick='return false;'][contains(.,'Acciones')]"
    titulos = "//a[@onclick='return false;'][contains(.,'T')]"
    compra = "//a[@href='/tradingNS/pages/mesa/mainMesa.xhtml?op=COMPRA&ti=BONO'][contains(.,'Compra')]"
    compra_2 = "//a[@href='/tradingNS/pages/mesa/mainMesa.xhtml?op=COMPRA&ti=ACCION'][contains(.,'Compra')]"
    venta = "//a[@href='/tradingNS/pages/mesa/mainMesa.xhtml?op=VENTA&ti=ACCION'][contains(.,'Venta')]"
    venta_2 = "//a[@href='/tradingNS/pages/mesa/mainMesa.xhtml?op=VENTA&ti=BONO'][contains(.,'Venta')]"
    auto_pendientes = "//a[contains(.,'Autorizaciones Pendientes')]"
    
    
    #Lista de clientes venta
    lista_cliente = "//select[contains(@name,'formCliente:j_id_38')]"
    input_cliente = "//input[@type='text']"
    tipo_cliente_Nom = "//option[@value='NOMBRE'][contains(.,'Nombre/Razón Social')]"
    tipo_cliente_Nro = "//option[@value='NRO_CLI'][contains(.,'Nro. Cliente')]"
    tipo_cliente_CUIT = "//option[@value='CUIT'][contains(.,'CUIT')]"
    tipo_cliente_CUIL = "//option[@value='CUIL'][contains(.,'CUIL')]"
    tipo_cliente_Doc = "//option[@value='DOCUMENTO'][contains(.,'Documento')]"
    
    btn_buscarCliente ="//input[contains(@name,'formCliente:applyFiltersButton')]"
    btn_seleccionar  = "//input[contains(@name,'j_id_mi:j_id_ml:4:j_id_n4')]"
    btn_seleccionar_2  = "//input[contains(@name,'j_id_52:j_id_55:0:j_id_5m')]"


    # Boton selecccionar asociado a datos
    select_Nom_Razon_social = "//input[contains(@name,'j_id_ln:j_id_lq:0:j_id_m8')]"
    select_cuenta= "//input[contains(@name,'j_id_mi:j_id_ml:0:j_id_n4')]"
    
    #Boton siguiente genérico
    btn_siguiente = "//input[contains(@value,'Siguiente')]"
    
    #boton venta del banco
    btn_venta_banco = "//input[contains(@name,'formPreOrden:btnVentaBanco')]"
    
    #boton aceptar generico
    btn_aceptar = "//span[contains(.,'Aceptar')]"
    
    btn_aprobar = "//input[@value='Aprobar']"
    
    btn_fondos_comunes = "//a[contains(.,'Fondos Comunes')]"

    item_fondos = "//input[contains(@value,'G AHMAX B')]"
    
    item_fondos_pesosB = "//input[contains(@value,'GPESOS B')]"
 
    item_fondos_pesosA = "//input[contains(@value,'GPESOS A')]"
   
    btn_suscripcion = "//input[@name='formFCI:btnSuscripcion']"
    
    btn_rescate_cuota_parte = "//input[contains(@name,'formFCI:btnRescateCuota')]"
  
    #boton aceptar orden de venta    
    btn_aceptar_ord_venta= "//input[contains(@name,'formOrden:j_id_ft:j_id_fz')]"
    
    #contenedores de datos
    contains_automatizacion= "(//td[contains(.,'AUTOMATIZACIÓN MESA WEB')])[2]"
 
    contains_david_food_2661= "(//td[contains(.,'DAVID FOOD 2661')])[2]"
    
    contains_producto_nuevo_vanes= "(//td[contains(.,'PRODUCTO NUEVO VANES *')])[2]"


    contains_empresa_alfa_10= "(//span[contains(.,'EMPRESA ALFA10 - 6411')])[2]"

    contains_cuenta="//span[@class='centerColumn'][contains(.,'00000000098')]"
    
    #lista de instrumentos
    #lista_instrumentos = "//input[@name='selectInstrumento']"
    lista_instrumentos = "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[1]/form[1]/span[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]/div[1]/div[1]/input[1]"
    autocompletar_instrumento = "(//ul[contains(@class,'ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all')])[3]"
    
    #Cantidad
    cantidad_VN= "//input[contains(@name,'formPreOrden:inputCantidad')]"
    
    readro_instrumentos = "//input[contains(@name,'selectInstrumento')]"
    #Ultimo precio
    
    ultimo_precio = "(//td[contains(.,'Ult. Pcio. Oper.$')])[3]"
    precio = "//input[contains(@name,'formPreOrden:inputPrecio')]"
    imput_monto = "//input[contains(@name,'formOpFCI:inputCantidad')]"
    imput_cuotas = "//input[contains(@name,'formOpFCI:inputCantidad')]"
    imput_nro_operacion = "//input[contains(@name,'mainForm:accordionFilter:j_id_38:j_id_3w')]"

    
    #Numero de orden
    
    nro_orden = "/html[1]/body[1]/div[1]/div[2]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/span[1]"
   
   #boton compra de banco
   
    btn_compra_banco = "//input[contains(@name,'formPreOrden:btnCompraBanco')]"
    
    item = "//a[contains(.,'AO20 - BONO NAC ARG USD 8 BONAR20')]"
    
    #boton aceptar
    
    
    btn_aceptar_1 = "//input[contains(@value,'Aceptar')]"
        
    btn_aceptar_orden = "//span[contains(.,'Aceptar')]"
    
    btn_confirmar = "//input[@value='Confirmar']"

    #boton aceptar
    
    btn_mostrar_orden = "//a[contains(.,'Mostrar datos de la orden para Imprimir')]"

    
    #checkbox
    check_box = "//input[contains(@type,'checkbox')]"

    
    
    #mensaje exito 
    
    msj_la_orden_exito = "//label[@class='title2'][contains(.,'La orden se dio de alta')]"
    
    msj_exito = "//div[@class='ui-pnotify-text'][contains(.,'La operación ha sido anulada satisfactoriamente.')]"

    msj_exito_2 = "//div[@class='ui-pnotify-text'][contains(.,'Se realizaron las imputaciones de movimientos de las operaciones seleccionadas.')]"
  
    
    btn_imprimir = "//a[contains(@onclick,'javascript: window.print();')]"
    
    btn_ir_a_bandeja = "//a[contains(.,'Ir a Bandeja')]"
    
    btn_bandeja = "//a[contains(.,'Bandeja')]"
    
    btn_FCI = "//span[@class='ui-button-text'][contains(.,'FCI')]"
    
    td_numero_orden = "(//td[contains(.,'{}')])[1]"
    
    btn_X = "(//i[contains(@class,'fa fa-times-circle')])[1]"

    check_ok = "//i[contains(@class,'fa fa-check')]"
    
    btn_aprobar = "//input[contains(@name,'j_id_4u:j_id_5w:j_id_60')]"
    
    btn_aceptar = "//span[@class='ui-button-text'][contains(.,'Aceptar')]"
    
    btn_buscar = "//input[@value='Buscar...']"

    check_box_2 = "//input[contains(@type,'checkbox')]"
    
    btn_imputar = "//input[@value='Imputar...']"
    
    btn_bajas = "//span[@class='ui-button-text'][contains(.,'Bajas')]"
    
    cell_nro_orden = "//td[@class=' '][contains(.,'{}')]"

    