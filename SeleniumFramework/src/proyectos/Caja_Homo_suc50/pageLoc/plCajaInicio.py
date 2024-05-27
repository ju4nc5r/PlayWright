# -*- coding: utf-8 -*-
class plCajaInicio():

    # Identificar Cliente
    
    btn_identificarClients = "//span[@class='mat-button-wrapper'][contains(.,'IDENTIFICAR CLIENTE')]"
    txt_CuadroIngresoDatosCliente = "//span[contains(.,'Ingresá los datos del cliente')]"
    slc_tipoDoc = "//div[contains(@class,'mat-select-value ng-tns')][contains(.,'DNI')]"
    ipt_documento = "//input[contains(@formcontrolname,'documentId')]"
    
    # xpath para cualquier select
    opt_select = "//span[@class='mat-option-text'][contains(.,'{}')]"
    # xpath para cualquier select

    btn_identificar = "//span[contains(.,'IDENTIFICAR')]"
#     btn_identificar = "(//span[contains(.,'IDENTIFICAR')])[2]"
    btn_operaSinClave = "//button[@color='primary'][contains(.,'SIN CLAVE')]"
    btn_cerrar = "//button[contains(@class,'btnNo')]"
    
    cntRecuadroDatosCliente = "//it-client-identification-review[contains(@class,'ng-star-inserted')]"
    
    txt_nombreUser = "//td[contains(@class,'mat-column-nombre')]"
    txt_apellidoUser = "//td[contains(@class,'mat-column-apellido')]"

    lblnomyApeRegFirma = "(//span[contains(@class,'session-info-content')])[1]"
    lblNroDocRegFirma = "(//span[contains(@class,'session-info-content')])[2]"  
    imgFirmaRegFirma = "//img[contains(@src,'data:image')]"
    
    btn_FinalizarIdentificacion = "//button[contains(.,'FINALIZAR')]"
#     btnRegFirmaFinalizar = "//span[@class='mat-button-wrapper'][contains(.,'FINALIZAR')]" 
    

    btn_sidebar = "//button[contains(@class,'mat-button-hide')]/span"

    # xpath operaciones 
    btn_operaciones = "//mat-expansion-panel-header[contains(@id,'mat-expansion-panel-header-0')]"
    # xpath operaciones 

    # xpath compra/venta moneda Extranjera
    btn_moneda_extranjera = "//mat-expansion-panel-header[contains(@id,'mat-expansion-panel-header-1')]"

    title_out = "//div[contains(@class,'col-md-3') and contains(.,'Seleccione una cuenta')]"

    btn_compra_venta = "//a[contains(.,'Compra/venta Moneda Extranjera')]"
    
    slp_compraventa_Ini = "//div[@class='mat-tab-label-content'][contains(.,'"  
    slp_compraventa_Fin = " de Moneda Extranjera')]"  

    ipt_moneda = "//*[@formcontrolname='monedas']"
#     ipt_moneda = "descendant::input[@id='mat-input-4'][1]"
#     ipt_moneda = "//input[contains(@placeholder,'Moneda')]"
    
    opt_nroCuenta = "//mat-option[contains(.,'{}')]"
    # xpath compra/venta moneda Extranjera

    # xpath clientes 
    btn_clientes = "//mat-expansion-panel-header[contains(@id,'mat-expansion-panel-header-2')]"

    btn_certificacion_firma="//span[@class='menu-item-description'][contains(.,'Certificacion Firma')]"
    #btn_certificacion_firma = "//a[contains(.,'Certificacion Firma')]"

    chk_confirmar = "//mat-checkbox[contains(@formcontrolname,'check')]"
    # xpath clientes 


    ipt_nroDocMoneda = "//*[@formcontrolname='nd']"

    slc_moneda = "//div[contains(@class,'mat-select-value ng-tns')]"
#     slc_moneda = "(//div[contains(.,'Monedas')])[11]"
#     slc_moneda = "//*[@formcontrolname='moneda']"
    slc_moneda4 = "//div[@class='mat-select-value ng-tns-c69-8']"

    ipt_importe ="//input[@onlynumbers='true']"
    ipt_importe3 = "(//input[@onlynumbers='true'])[2]" 
    #ipt_importe = "//*[@formcontrolname='valor']"
    
    
    ipt_cuenta = "//input[contains(@name,'numeroCuenta')]"
    ipt_importe2 = "//input[@formcontrolname='valors']"
    
    lbl_importeCpraVta = "//input[contains(@formcontrolname,'imc')]"

    txt_CotizComprador = "(//input[contains(@placeholder,'Cotizacion Comprador')])[1]"
    
#     txt_CotizVendedor = "//input[contains(@placeholder,'Cotizacion Vendedor')])[1]"
    txt_CotizVendedor = "//input[contains(@placeholder,'Cotizacion Venderdor')]"

    txt_CotizAplicada = "//input[@formcontrolname='ccs']"
#     txt_CotizAplicada = "(//input[@placeholder='Cotizacion Aplicada'])[1]"
    
    txt_Cotizacion = "//input[@placeholder='Cotizacion']"
    
    txt_importeEnPesosCompra = "(//input[@placeholder='Importe en Pesos de la Compra'])[1]"
    
    txt_importeEnPesosVenta = "(//input[@placeholder='Importe Final de la Venta'])[1]"
    
    txt_importeEnPesos = "//input[@formcontrolname='isc']"

    slc_tipoDocMoneda = "//*[@formcontrolname='td']"
    
    lbl_NroIdentifTributaria =  "(//input[@placeholder='Numero de Documento'])[2]"
    
    ipt_nroCuenta = "//input[@formcontrolname='cuenta']"
    
    mat_nroCuentaIni ="//pre[contains(.,'"
    
    mat_nroCuentaFin ="')]"
    
    # xpath compra/venta moneda Extranjera

    btn_minimizedFirma = "//button[contains(@class,'button-minimized ')]"

    btn_finalizar = "//button[contains(.,'FINALIZAR')]"

    btn_confirmar = "//button[@color='primary'][contains(.,'Confirmar')]"
    #btn_confirmar = "descendant::button[contains(@class,'primary-button ') and contains(.,'Confirmar')]"
    
    btn_confirmar2 = "//span[@class='mat-button-wrapper'][contains(.,'Confirmar')]"
    
    btn_salir = "//span[@class='mat-button-wrapper'][contains(.,'SALIR')]"

    
    btn_confirmar3 = "(//span[@class='mat-button-wrapper'][contains(.,'Confirmar')])[2]"
    
    btn_aceptar = "descendant::button[contains(@class,'primary-button ') and contains(.,'Aceptar')]"
    
    btn_aceptar2 = "//span[contains(.,'Aceptar')]"
    
    btn_siguiente_3 = "descendant::button[contains(@class,'primary-button ') and contains(.,'Siguiente')][3]"
    
    btn_siguiente_2 = "(//button[@color='primary'][contains(.,'Siguiente')])[2]"
#     btn_siguiente_2 = "descendant::button[contains(@class,'primary-button ') and contains(.,'Siguiente')][2]"

    btn_siguiente = "//button[@color='primary'][contains(.,'Siguiente')]"
    #btn_siguiente = "descendant::button[contains(@class,'primary-button ') and contains(.,'Siguiente')]"
    
    




    # xpath operaciones - comunes a varios tipos de operacion
    
    lbl_NroDeCuenta = "//h6[contains(.,'{}')]"
    lbl_Importe =  "(//h6[contains(.,'{}')])[2]"

    # xpath extracciones


    #btn_extracciones ="//a[@class='menu-item ng-star-inserted'][contains(.,'2Extracciones en Efectivo')]"
    btn_extracciones = "//span[@class='menu-item-description'][contains(.,'Extracciones en Efectivo')]"

    ipt_cuentaCliente ="(//div[contains(.,'Cuentas Cliente')])[10]"
    #ipt_cuentaCliente = "//input[@placeholder='Cuentas Cliente']"
    
    btn_FinalizarTrx = "//button[@color='primary'][contains(.,'Finalizar')]"
    btn_Finalizar_tas = "//span[@class='mat-button-wrapper'][contains(.,'FINALIZAR')]"

    btn_FinalizarIdenif = "//button[@color='primary'][contains(.,'FINALIZAR')] "

    # Depositos 
    
    
    btn_deposito_efectivo = "//span[@class='menu-item-description'][contains(.,'Deposito de Cliente')]"
#     btn_deposito_efectivo = "//mat-panel-title[contains(.,'Depósitos')]"
#     btn_deposito_efectivo = "//a[contains(.,'Deposito Efectivo')]"
    txt_recuadroComun = "//input[contains(@formcontrolname,'nroCuenta')]"
    txt_cuenta_firma = "//input[contains(@formcontrolname,'cuenta')]"
    txt_datos_comun = "//input[contains(@formcontrolname,'{}')]"
    btn_deposito_cliente = "//input[contains(@aria-haspopup,'true')]"#     btn_deposito_cliente = "//a[contains(.,'Deposito de Cliente')]"
    
    
    
   
    
    ipt_cuentaClienteDeposito = "//input[contains(@aria-label,'Number')]"
#     ipt_cuentaClienteDeposito = "//input[@placeholder='Cuentas cliente']"

    slc_monedaDeposito = "//*[@formcontrolname='monedaOperacion']"

    ipt_valorDeposito = "//*[@formcontrolname='valorDeposito']"

    btn_continuar = "//button[contains(.,'Continuar')]"

    ipt_cuentadeposito = "//*[@formcontrolname='cuenta']"
    
    lbl_cuentaDeposito = "//input[contains(@name,'numeroCuenta')]"

    lbl_cuentaDeposito2 ="(//input[contains(@name,'numeroCuenta')])[2]"
    
    ipt_importedeposito = "//*[@formcontrolname='importeADepositar']"
    
    lbl_validarDato = "//*[@formcontrolname='{}']"
    
    ipt_importeIngresado = "//*[@formcontrolname='importeIngresado']"


    # xpath ingreso/egreso 
    
    btn_ingreso = "//*[contains(@class,'mat-tab-label-content') and contains(.,'Ingreso Externo del Numerario')]"
           
    ipt_sucuorigen = "//*[@formcontrolname='sucuorigen']"  
    
    ipt_sucuorigenEgr = "//input[@formcontrolname='sucuorigenE']"
        
    ipt_sucudestino = "//*[@formcontrolname='sucudestino']"
    
    ipt_sucudestinoEgr = "//input[contains(@formcontrolname,'sucudestinoE')]"
    
    ipt_nrocontrol = "//*[@formcontrolname='numerocontrol']"
    
    ipt_nrocontrolEgr = "//input[contains(@formcontrolname,'numerocontrolE')]"
    
    ipt_valor = "//input[contains(@formcontrolname,'Valor')]"
#     ipt_valor = "//*[@formcontrolname='Valor']"    

    btn_EgresoExtNumerio = "//div[@class='mat-tab-label-content'][contains(.,'Egreso Externo del Numerario')]"

    btn_ingreso_egreso = "//span[@class='menu-item-description'][contains(.,'Ingreso / Egreso Externo')]"
    
    
    btn_ingreso_egreso_interno="//span[@class='menu-item-description'][contains(.,'Ingreso/Egreso Interno')]"
    
    slp_egreso_externo = "//*[contains(@class,'mat-tab-label-content') and contains(.,'Egreso Externo del Numerario')]"

    slp_ingresoExtNumerario = "//div[@class='mat-tab-label-content'][contains(.,'Ingreso Externo del Numerario')]"
 
    slp_EgresoExtNumerio = "//div[@class='mat-tab-label-content'][contains(.,'Egreso Externo del Numerario')]"

    slc_monedaE = "//*[@formcontrolname='monedaE']"

    ipt_sucuOrigenE = "//*[@formcontrolname='sucuorigenE']"

    ipt_sucuDestinoE = "//*[@formcontrolname='sucudestinoE']"

    ipt_nroControlE = "//*[@formcontrolname='numerocontrolE']"
    
    ipt_valorE = "//*[@formcontrolname='ValorE']"

    txt_exito = "//h4[contains(.,'{}')]"
    #txt_exito = "//p[contains(.,'La operacion finalizo correctamente')]"
    
    txt_exito_deposito = "//p[contains(.,'{}')]"
    
    txt_exito_deposito2 = "//h6[@class='title'][contains(.,'{}')]"

#     txt_exito_cpravtaME = "//p[contains(.,'Operacion Realizada Con Exito')]"
    txt_exito_cpravtaME = "(//div[contains(@class,'col-md-12')])[3]"    
                       
#     txt_exitoEI = "//mat-dialog-container[@id='mat-dialog-0']//div[contains(@class,'row')]//font"
#     txt_exitoEI = "//p[contains(.,'{}')]"
    
    txt_exitoEI = "//span[contains(.,'{}')]"
    
  
    txt_TrxNoAutorizada = "//p[contains(.,'TRANSACCION NO AUTORIZADA')]"
    
    
    
    txt_ImpresionOK = "//p[contains(.,'Impresion OK')]"
#     txt_ImpresionOK = "//font[contains(.,'Impresion OK')]"
    
    
    
    
    btn_cerrarMjeExito_X ="//button[contains(.,'X')]"
    btn_cerrarMjeExito = "(//button[contains(.,'Aceptar')])[2]"
    #btn_cerrarMjeExito = "//span[contains(.,'X')]" 
    
    btn_cerrarMjeAlert = "//span[contains(.,'X')]"
    
#     btn_cerrarMjeImpresionOK  = "descendant::span[contains(.,'X')][1]" 
    
    btn_cerrarMjeImpresionOK  = "descendant::span[@class='mat-button-wrapper'][contains(.,'X')][2]"     
    
#Ingreso Egreso Interno 


    mnu_Ingreso_Egreso_Interno="//span[@class='menu-item-description'][contains(.,'Ingreso / Egreso Interno')]"
    
    slp_Ingreso_Interno_Del_Numerario="//div[@role='tab'][contains(.,'Ingreso Interno del Numerario')]"
    
    slp_Egreso_Interno_Del_Numerario="//div[@role='tab'][contains(.,'Egreso Interno del Numerario')]"
    
    btn_AceptarComun = "//button[@color='primary'][contains(.,'Aceptar')]" 
    
    btn_Aceptar2 = "(//button[@color='primary'][contains(.,'Aceptar')])[2]" 

    
    msj_txt_operacion_Exitosa_ = "//div[@class='confirmacion-message-container'][contains(.,'{}')]"
    
    #msj_txt_operacion_Exitosa_="(//font[contains(.,'La operacion finalizo correctamente')])[2]"
    
    btn_aceptar_cerrarMjeExito = "(//button[contains(.,'Aceptar')])[2]"
    
    
    
    #############################Depositos de 3ros######################################################################
  
    
    btn_deposito_tercero = "//span[@class='menu-item-description'][contains(.,'Deposito a Terceros')]"

    btn_RadioBtn = "//span[@class='mat-radio-label-content'][contains(.,'{}')]"
    
    btn_sigiente_3ros = "(//button[@color='primary'][contains(.,'Siguiente')])[3]"

    ipt_cuenta_terceros = "//mat-select[contains(@formcontrolname,'cuenta')]"

    ipt_documento2 = "//input[contains(@formcontrolname,'numeroDocumento')]"
    
    ipt_Alias = "//input[contains(@formcontrolname,'alias')]"
    
    ipt_documento_Depositante = "//input[contains(@formcontrolname,'numeroDocumentoDepositante')]"
    
    ipt_documento_Ordenante =  "//input[contains(@formcontrolname,'numeroDocumentoOrdenante')]"
    
    ipt_importeDepo3ros = "//input[contains(@formcontrolname,'importe')]"
    
    ipt_nroDocumenteDepositante = "//input[contains(@formcontrolname,'numeroDocumentoDepositante')]"

    lbl_importeDeposito3ros = "//input[contains(@name,'valor')]"
    
    lbl_MonedaDepo3ros = "//input[contains(@name,'codMoneda')]"

    lbl_Nombre3ros = "//input[contains(@name,'nombreCuenta')]"
    
    lbl_NombreOrdenante = "//input[contains(@formcontrolname,'nombreOrdenante')]"
    
    lbl_nombreYapellido_Depositante = "//input[contains(@formcontrolname,'nombreApellidoDepositante')]"
    
    lbl_nombreYapellido_ordenante = "//input[contains(@formcontrolname,'nombreOrdenante')]"

    lbl_cuil = "//mat-select[@role='combobox'][contains(.,'CUIL: 27248541321 - GUERBI, MARIA EUGENIA')]"
    
    opt_select2 = "//span[@class='mat-option-text'][contains(.,'Ingresar manualmente')]"


    slc_tipoDoc3 = "//mat-select[contains(@formcontrolname,'tipoDocumentoOrdenante')]"
   
    slc_tipoDocDepositante = "//mat-select[contains(@formcontrolname,'tipoDocumentoDepositante')]"
      
    slc_selec_manual = "(//span[contains(.,'CUIL: 20120620135 - CARDOZO, HUGO')])[2]"

    txt_recuadroComun = "//input[contains(@formcontrolname,'nroCuenta')]"  
    
    txt_CBU = "//input[contains(@formcontrolname,'nroCbu')]"
      
    txt_Raiz = "//input[contains(@formcontrolname,'raiz')]"  
       
    txt_DocDepositante = "//input[contains(@formcontrolname,'numeroDocumentoDepositante')]"
    
    slc_cuenta = "//div[contains(@class,'mat-select-value ng-tns')]"
    
    slc_cuenta2 = "(//div[contains(@class,'mat-select-value ng-tns')])[2]"


################################AUTORIZACION BOX-T40#################################################
   
    btn_aceptar_Autoriz = "//span[@class='ng-star-inserted'][contains(.,'ACEPTAR')]"
     
    recuadro_autoriz = "//div[contains(@class,'table flex row-center content-background')]"
    
    btn_Finalizar = "//button[contains(.,'FINALIZAR')]"
    
    lbl_Nro_Autorizacion = "//td[@class='text-align-center'][contains(.,dddd)][1]"
################################CERTIFICACION DE FIRMA###############################################

    opt_cuentaFirma = "//pre[contains(.,'{}')]"

    btn_aqui = "//b[contains(.,'aqu')]"

    btn_template = "//b[contains(.,'Imprimir template de firma')]"

################################ CONSULTA DE POSICION Y SALDO DE CUENTA#####################################
     
    txt_raices_Cliente = "//mat-select[contains(@role,'combobox')]"
    
    txt_cuadroNecesitaIdentificarse = "//it-card[contains(.,'¿Necesita identificar al cliente? no  si')]"
    
    input_cuentas = "//input[contains(@minlength,'5')]"

    ipt_cuentaRaices = "//span[contains(.,'{}')]"
    
    ipt_cuenta3 = "//pre[contains(.,'{}')]"
    
    btn_consultar = "//span[contains(.,'Consultar')]"
    
    btn_consultar2 = "//button[contains(.,'Consultar')]"
    
    btn_ticked = "//span[contains(.,'Ticket')]"
    
    btn_SI = "//button[contains(.,'si')]"
    
    btn_NO  = "//button[contains(.,'no')]"
    
    msgExito_consulta  = "//span[contains(@class,'notification-message')]"
    
    btn_consuta_posicion_cuenta = "//span[contains(.,'Posición de Cuenta')]"
    
    btn_consuta_saldos_cuenta = "//span[contains(.,'Consulta de Saldos de Cuentas')]"
    
################################## COBROS Y PAGOS ###########################################################

    btn_cobrosVarios = "//span[contains(.,'Cobros Varios')]"

    btn_AceleramientoDeOficios = "//span[contains(.,'Arancelamiento de Oficios')]"
        
    btn_PagosVarios = "//span[contains(.,'Pagos Varios')]"
    
    btn_Siguiente = "//button[contains(.,'siguiente')]"
    
    btn_validar = "//span[contains(.,'Validar')]"
    
    ipt_Importe2 = "//h6[contains(.,'{}')]"
    
    ipt_moneda2 = "//h6[contains(.,'{}')]"
    
    ipt_operacion = "//h6[contains(.,'{}')]"
    
    ipt_operacion2 = "//span[contains(.,'{}')]"
    
    ipt_moneda3 = "//span[@class='mat-option-text'][contains(.,'{}')]"
    
    txt_tipoDeOperacion = "//mat-select[contains(@formcontrolname,'tipo')]"
    
    txt_cantidadDeOficios ="//input[contains(@formcontrolname,'cantidad')]"
    
    txt_importeTotal = "//input[contains(@formcontrolname,'importeTotal')]"
     
    txt_moneda = "(//mat-select[contains(@role,'combobox')])[2]"
    
    imput_importe = "//input[contains(@autocomplete,'off')]" 
    
    msgExito_Operacion = "//div[@class='notification-container success'][contains(.,'{}')]"
    msgExito_Almacenamientos = "//span[@class='notification-message'][contains(.,'{}')]"
    
    
    ########CIERRE DE CAJA
    
    btn_cierreDeaCaja = "//span[contains(.,'Cierre de Caja')]"
    
    txt_cierre_moneda = "//p[contains(.,'Cierre de la moneda {} realizado.')]"
    
    txt_cierre_Caja = "//p[contains(.,'Cierre de la moneda {} realizado. La caja ha sido cerrada con exito.')]"
    
    txt_cierre_Sucursal = "//p[contains(.,'Cierre de la moneda {} realizado. La sucursal ha sido cerrada con exito.')]"
    
    ########ATMBANELCO , LIVERACIONES
    
    btn_ATMBanelco = "//span[contains(.,'ATM Banelco')]"
    
    btn_ATMLiveraciones = "//span[contains(.,'ATM Liberaciones')]"
    
    slc_trassaccion = "//mat-select[contains(@formcontrolname,'ion')]"

    slc_numeroATM = "//span[contains(.,'{}')]"
    
    slc_numeroTAS = "//span[contains(.,'{}')]"

    
    slc_moneda3 = "(//mat-select[@role='combobox'])[3]"
    
    opt_selectTransaccion = "//span[@class='mat-option-text'][contains(.,'{}')]"
    
    opt_selectnumeroATM = "(//mat-select[@role='combobox'])[2]"
    
    msj_atm_estado_cargado = "//h6[@class='title'][contains(.,'BE1744 - ATM en estado cargado.')]"
    
    text_sucursal = "(//h6[contains(.,'{}')])[2]"
    
    text_importe_total = "(//h6[contains(.,'{}')])[2]"

    text_importe_total_a_liberar = "(//h6[contains(.,'{}')])"
    
    text_moneda= "(//h6[contains(.,'{}')])"
    
    text_operacion = "//h6[contains(.,'{}')]"

    text_trasaccion = "//h6[contains(.,'{}')]"
    
    text_nombre_2 = "(//h6[contains(.,'{}')])[2]"
    
    text_nombre = "//h6[contains(.,'{}')]"

    text_cuenta = "//h6[contains(.,'{}')]"
    
    text_cbu = "//h6[contains(.,'{}')]"

    text_cuit_cuil = "//h6[contains(.,'{}')]"
    
    text_concepto = "(//h6[contains(.,'{}')])"
    
    text_referencia = "(//h6[contains(.,'{}')])[2]"

    ####### ENVIO DE REMESAS 
    
    btn_EnvioDeRemesas = "//span[contains(.,'Envio de Remesa de Cheques')]"
    
    msj_txt_saldo_insuficiente = "//h6[@class='title'][contains(.,'No hay suficiente saldo en el tesoro/caja para la operación')]"
 
    msj_txt_saldo_insuficiente_depositos = "//h6[@class='title'][contains(.,'GTDE0002-Error, saldo insuficiente en la caja en Depósito.')]"
 
    msj_txt_no_hay_operaciones_con_cheques = "//h6[@class='message'][contains(.,'No se registra ninguna operación con cheques')]"

    text_destino = "(//h6[contains(.,'{}')])"
    
    text_origen = "(//h6[contains(.,'{}')])"

    

    ###### DEPOSITO DE CHEQUES
    
    btn_deposito_de_cheques = "(//span[contains(.,'Deposito Cheques')])[1]"
    
    btn_deposito_de_chequesPropios = "//span[contains(.,'Deposito Cheques Propios')]"
    
    btn_finDeCarga = "//span[contains(.,'Fin Carga')]"
    
    btn_validarCheques = "//button[@color='primary'][contains(.,'VALIDAR CHEQUES')]"
    
    btn_validar_cheques_dps = "//span[@class='mat-button-wrapper'][contains(.,'Validar cheque')]"

      
    input_datos_cheques = "//input[contains(@formcontrolname,'{}')]"

    input_datosCheques_2 = "//input[contains(@id,'numeroCuenta')]"

    
    ###### PAGOS CHEQUES 
    
    btn_pago_de_cheques = "(//span[contains(.,'Pago de Cheque')])[1]"
    
    chek_cliente = "(//span[contains(@class,'mat-checkbox-inner-container')])[2]"
    
    ###### PAGOS CHEQUES CERTIFICADO 
    
    btn_pago_de_cheques_certificado = "//span[contains(.,'Pago de Cheque Certificado')]"
    
    chek_cliente = "(//span[contains(@class,'mat-checkbox-inner-container')])[2]"
    
    ##### TRASFERENCIAS
    
    btn_TrasferenciasAotrosClientes = "//span[@class='menu-item-description'][contains(.,'Transferencias a Otro Cliente')]"
    
    btn_TrasferenciasEntreCuentas = "//span[contains(.,'Transferencias Entre Cuentas Propias')]"
    
    btn_TrasferenciasAOtrosBancos = "//span[contains(.,'Transferencias a Otros Bancos')]"
    
    btn_Ingresar = "//span[contains(.,'ingresar')]"
    
    btn_Siguiente4 ="//span[contains(.,'siguiente')]"
    
    inputCuit_Cuil = "//input[contains(@minlength,'11')]"
    
    inputReferencia = "//input[contains(@formcontrolname,'referencia')]"
    
    txt_dialogo ="//mat-dialog-container[contains(.,'Ingresar el CUIT / CUIL del DestinatarioCUIT / CUIL Cancelar  ingresar')]"
    
    btn_deposito_cliente2  =   "(//input[contains(@aria-haspopup,'true')])[2]"
    
    ipt_cuentaClienteDeposito2 ="(//input[contains(@aria-label,'Number')])[2]"
    
    
    
    #####PAGO DE TARJETA DE CREDITO 
    
    btn_CobroDeTargetasDecredito = "//span[contains(.,'Cobro de Tarjeta de Credito')]"
    
    slc_formaDePago = "(//div[contains(@class,'mat-select-value ng-tns')])[2]"
    
    list_box_monedas = "//div[contains(@role,'listbox')]"
    
    slc_visa = "(//div[contains(@class,'mat-select-value ng-tns')])[1]"

    txt_nroTarjeta = "//input[contains(@formcontrolname,'numero')]"
    
    lbl_datosTarjetaMaster = "(//span[contains(.,'Master      005399096821061008  -  Titular')])[1]"
    

    ##### TAS LIBERACIONES
    
    btn_tasLiberaciones = "//span[contains(.,'TAS Liberaciones')]"
    
    input_NroTas = "(//input[contains(@autocomplete,'off')])[1]" 
    
    input_Importe6 = "(//input[contains(@autocomplete,'off')])[2]"
    
    input_Importe5= "(//input[contains(@autocomplete,'off')])[3]"
    
    btn_Redepositar = "//span[contains(.,'Redepositar')]"
    
    
    
    
    
    ####### ENVIO DE REMESA INTERNA
    
    btn_EnvioDeRemesaInterna = "//span[contains(.,'Envio de Remesa Interna')]"
    
    ####### ENVIO DE REMESA INTERNA
    
    btn_EnvioDeRemesa = "(//span[contains(.,'Envio de Remesa')])[1]"

  
    ######CONSULTA DE SALDO
    
    
    btn_ConsultaDeSaldos = "(//span[contains(.,'Consulta de Saldos')])[2]"
    
    btn_Salir ="//span[contains(.,'Salir')]"
    
    cellMoneda = "(//td[contains(@class,'saldoCaja ')])[{}]"
    
    cellMonedaCaf = "(//td[contains(@class,'-saldoTesoroIntermedio')])[{}]"
    
    cellMonedaTrosucursal = "(//td[contains(@class,'saldoTesoroSucursal')])[{}]"
    
    ####CONSULTA DE TOTALES
    
    btn_ConsultaDeTotales = "//span[contains(.,'Consulta de Totales')]"
    
    btn_cancelar = "//span[contains(.,'Cancelar')]"
    
    
    #####VENTANA DE SALDO EXEDIDO CAF - CAJA
    
    slp_saldoExedidoCajaCaf = "//it-card[contains(.,'Saldo excedido en CAJA o CAF Continuar')]"
    
    slp_saldoExedidoCajaCaf2 = "//it-card[contains(.,'Bloqueo de terminal por exceso de saldo en CAJA o CAFSe necesita autorizacion Continuar')]"
     
    btn_Si = "//button[@color='primary'][contains(.,'SI')]"
    
    chekCierre = "(//span[contains(@class,'mat-checkbox-inner-container')])[{}]"
    
    btn_CierreMoneda = "(//span[contains(.,'Cerrar moneda')])[{}]"
    
    btn_CierreCaja = "//span[contains(.,'Cerrar caja')]"
    
    msgMonedaCerrada = "//h6[@class='message'][contains(.,'Cierre de moneda {} realizado con éxito')]"
    
    msgCajaCerrada ="//h6[@class='title success ng-star-inserted'][contains(.,'Cierre de caja realizado con éxito')]"
    
    msgSucursalCerrada = "//h6[@class='title success ng-star-inserted'][contains(.,'Cierre de sucursal realizado con éxito')]"
 
    msj_txt_existen_cajas_sin_cerrar = "//h6[@class='title'][contains(.,'Existen cajas sin cerrar')]"

    msj_txt_advertencia = "//h6[@class='title'][contains(.,'Si inicia el proceso de cierre no podrá realizar más operaciones')]"
 
    colum_cierra ="(//div[@class='row'])[{}]"
    msj_txt_existen_monedas_con_saldos = "//h6[@class='title'][contains(.,'Existen monedas con saldo en cajón')]"
   
    ######Consulta de Posición del Líquido de la Sucursal
    
    btn_ConsultaDelLiquidoDeLaSucursal = "//span[contains(.,'Consulta de Posicion del Liquido de la Sucursal')]"
    
    cell_saldos = "//div[@class='row row-line p-2 ng-star-inserted'][contains(.,'{}')]"

    input_transaccion = "//input[contains(@placeholder,'Buscar por código o nombre')]"
    
    msg_transaccionNoAutorizada3 = "//div[@class='error-message-container'][contains(.,'{}.')]"

    btn_aceptar3 = "//span[contains(.,'ACEPTAR')]"

    
    #####
    
    lbl_datoValidar1 =  "//h6[contains(.,'{}')]"

    lbl_datoValidar2 =  "(//h6[contains(.,'{}')])[2]"

    lbl_cantidadCheques =  "(//h6[contains(.,'1')])[2]"
    
    lbl_cantidadCheques2 = "(//h6[contains(.,'{}')])[4]"
    
    lbl_cantidadCheques3 = "(//h6[contains(.,'1')])[2]"
    
    lbl_cantidadCheques4 = "(//h6[contains(.,'1')])[3]"

    #### CONSULTA DE REMESAS POR SUCURSAL
    
    lbl_consultaRemesasPorSucursal = "//span[contains(.,'Consulta de Remesas por Sucursal')]"
    
    msg_transaccionNoAutorizada = "//it-card[contains(.,'Transaccion no autorizadaUsted no es centralizador')]"
    
    msg_transaccionNoAutorizada2 = "//it-card[contains(.,'{}')]"
    #### CONSULTA DE REMESAS POR SUCURSAL
    
    lbl_consultaRemesasPorOperador = "//span[contains(.,'Consulta de Remesas por Operador')]"
    
    msg_transaccionNoAutorizada2 = "//div[contains(@class,'text-align-center')]"
    #### CONSULTA DE LIQUIDO DE CUENTA
    
    lbl_consultaDeLiquidoDeCuenta = "//span[contains(.,'Consulta del Liquido en Caja')]"
    
    msg_ok = "//div[@class='notification-container success'][contains(.,'El ticket se imprimió correctamente')]"

    #### CONSULTA DE SALDOS SUCURSAL
    
    lbl_consultaDeSaldosSucursal = "//span[contains(.,'Consulta de Saldos Sucursal')]"
    
    div_consultaSaldosSucursal = "//div[@class='col-12 col-header down center'][contains(.,'Operadores Tesoro Intermedio Tesoro Sucursal')]"
    
    td_saldosOperador = "//div[contains(@class,'table-container ng-star-inserted')]"
    
    td_tesoroIntermedio = "//div[contains(@class,'table-container ng-star-inserted')]"
    
    td_tesoroSucursal = "//div[contains(@class,'table-container ng-star-inserted')]"
    
    btn_listar = "//span[contains(.,'Listar')]"
    
    
    btn_parametro = "//span[contains(.,'{}')]"

    btn_Busqueda = "//div[@class='col-12 col'][contains(.,'Búsqueda')]"

    #### COBRO DE MULTAS
    
    lbl_cobroDeMulta = "//span[contains(.,'Cobro de Multas')]"

    ipt_cuenta ="//input[@onlynumbers='true']"

    chek_multa = "(//span[contains(@class,'mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin')])[2]"
    
    lbl_monedavalidar = "(//h6[contains(.,'{}')])[2]"
    
    lbl_importeTotal = "(//h6[contains(.,'{}')])[2]"
    
    msg_not_Multas = "//p[contains(.,'No hay multas impagas asociadas a esta cuenta.')]"
    
    btn_buscarCuentas = "//span[contains(.,'Buscar Cuentas')]"
     
    #### REVERSO DE TRANSACCION 
    
    lbl_reversoTrassaccion = "//span[contains(.,'Reverso de Transaccion')]"
    
    imput_NroSecuencia = "//input[contains(@type,'number')]"
    
    slc_motivo = "//div[contains(@class,'mat-select-value ng-tns')]"
    
    ###### RECEPCION DE REMESAS 
    
    btn_recepcionDeRemesas = "//span[contains(.,'Recepcion de Remesas')]"

    tilde_verde = "//i[contains(@class,'it-icon-success-fill')]"
    
    msj_saldos_excedidos = "//it-card[contains(.,'Saldo excedido en CAJA o CAF Continuar')]"
    
    ##### CHEQUES CERTIFICADOS
    
    msj_cheque_sin_firmantes = "//h6[@class='title'][contains(.,'DO5455 - El Cheque No Es Certificado')]"
    
    
    ##CONSULTA DE REMESA GENERAL POR SUCURSAL
    
    lbl_consulta_de_remesa_general_por_sucursal = "//span[contains(.,'Consulta de Remesas por Operador')]"

    slc_origen = "(//div[contains(@class,'mat-select-value ng-tns')])[1]"
    
    slc_destino = "(//div[contains(@class,'mat-select-value ng-tns')])[2]"
    
    slc_estado = "(//div[contains(@class,'mat-select-value ng-tns')])[3]"
    
    slc_moneda_remesas = "(//div[contains(@class,'mat-select-value ng-tns')])[4]"
    
    
    btn_pago_de_jubilaciones = "//span[contains(.,'Pago de Jubilaciones Italianas')]"
    
    msj_sin_beneficios = "//td[@colspan='7'][contains(.,'No hay beneficios de pensiones italianas pendientes de pago para este beneficiario')]"
    
    check_numero_de_pension = "(//span[contains(@class,'mat-radio-inner-circle')])[1]"

    check_numero_de_doc = "(//span[contains(@class,'mat-radio-outer-circle')])[2]"
    
    check_numero_de_pension_2 = "(//span[contains(@class,'mat-radio-outer-circle')])[3]"

    check_pago = "(//span[contains(@class,'mat-radio-outer-circle')])[5]"
    
    check_pago_2 = "(//span[contains(@class,'mat-radio-outer-circle')])[4]"

    check_beneficiario = "//span[contains(.,'Beneficiario')]"
    
    check_beneficiario_2 = "(//span[contains(@class,'mat-radio-inner-circle')])[5]"

    input_nro_pension = "//input[contains(@name,'numeroPension')]"
    
    input_nro_documento = "//input[contains(@name,'numeroDocumento')]"
    
    input_nro_documento_2= "(//input[contains(@name,'numeroDocumento')])[2]"
    
    data_pension = "(//div[contains(@class,'row')])[3]"
    
    data_pension_3 = "(//div[@class='row'])[3]"
    
    data_pension_2 = "(//div[contains(@class,'row')])[5]"
    
    data_pension_4 = "(//div[@class='row'])[4]"
     
    data_operacion = "(//div[@class='ng-star-inserted'])[3]"
    
    data_operacion_2 = "(//div[@class='ng-star-inserted'])[4]"    
    
    data_comprobante = "//html[contains(.,'Banco ITAU  0050 ')]"
    
    data_pagos_pendientes = "//div[contains(@class,'mat-tab-body-wrapper')]"
    
    data_pantalla = "//div[contains(@class,'d-flex justify-content-start')]"
    
    slc_tipo_doc= "//div[contains(@class,'mat-select-value ng-tns')]"
    
    btn_siguiente_4 = "(//span[@class='mat-button-wrapper'][contains(.,'Siguiente')])[4]"
    
    btn_buscar_pension = "//span[contains(.,'​ Buscar Pensión')]"
    
    txt_importe = "//h6[contains(.,'{}')]"
    
    #PLAZO FIJO
    
    btn_deposito_plazo_fijo_en_cuenta = "//span[contains(.,'Deposito a Plazo Fijo en Cuenta')]"
    
    div_cuentas_debito = "(//mat-select[contains(@role,'combobox')])[1]"
    
    div_plazos_fj = "//mat-select[contains(@formcontrolname,'tipoPF')]"
    
    circle = "(//span[contains(@class,'mat-radio-outer-circle')])[2]"
    
    button_calendario = "//button[@class='mat-focus-indicator mat-icon-button mat-button-base']"

    item_cuenta_cc = "//mat-option[@role='option'][contains(.,'CA')]"

    item_tipo_plazo_fijo = "//span[contains(.,'{}')]"

    ipt_dia = "//input[contains(@formcontrolname,'dia')]"
    
    btn_simular = "//button[contains(.,'SIMULAR')]"
    
    datos_simulacion = "//it-page-frame[contains(@class,'bg mb-5')]"

    check_marca_si_coincide = "//span[@class='mat-checkbox-label'][contains(.,'Marcar si coincide')]"
    
    btn_confirmar_2 = "//span[@class='mat-button-wrapper'][contains(.,'confirmar')]"

    btn_consulta_de_plazo_fijo = "//span[contains(.,'Consulta de Plazo Fijo')]"
    
    btn_pago_de_plazo_fijo = "//span[@class='menu-item-description'][contains(.,'Pago de Plazo Fijo en Efectivo')]"
    
    btn_imprimir = "//span[contains(.,'IMPRIMIR')]"

    input_nro_certificado = "//input[contains(@formcontrolname,'numeroCertificado')]"
    
    msj_no_hay_deposito = "//h6[@class='title'][contains(.,'PF1051 - Depósito no disponible para pago')]"
    
    datos_plazo_fijo = "//div[contains(@class,'content-card content-background')]"
    
    recueadro_firmante = "//it-card[@class='ng-star-inserted'][contains(.,'Rodrigo Apellido330 DNI 29954576')]"
    
    check_firmante = "//span[contains(@class,'mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin')]"

### COMPRA MONEDA EXTRANJERA

    btn_compra_moneda_extranjera = "//span[contains(.,'Compra Moneda Extranjera')]"

    btn_venta_moneda_extranjera = "//span[contains(.,'Venta Moneda Extranjera')]"
    
    slc_tipo_doc_4 = "//mat-select[contains(@formcontrolname,'tipoDocumento')]"
    
    slc_debe_precentar = "//mat-select[contains(@formcontrolname,'debePresentar')]"
    
    slc_tipo_moneda = "//mat-select[contains(@formcontrolname,'moneda')]"
    
    item_DNI = "//span[@class='mat-option-text'][contains(.,'DNI')]"

    item_CUIL = "//span[@class='mat-option-text'][contains(.,'CUIL')]"

    item_MONEDA = "//span[@class='mat-option-text'][contains(.,'Dólares')]"

    input_dni = "//input[contains(@formcontrolname,'numeroDocumento')]"
    
    input_cuil = "//input[contains(@formcontrolname,'numeroCuilCuitCdi')]"
    
    input_importe_a_comprar = "(//input[contains(@formcontrolname,'monto')])[1]"
    
    button_cotizar = "//span[contains(.,'Cotizar')]"

    label_cotizacion = "//mat-label[contains(.,'Cotiza')]"
    
    html_ticket = "//html[contains(.,'Banco BMA 0050')]"


### PAGO DE VALES

    btn_pago_de_vales = "//span[contains(.,'Pago de Vales')]"

    slc_rdo_cuenta_debito = "//mat-form-field[contains(.,'Cuenta Débito')]"

    slc_rdo_numero_de_legajo = "//mat-form-field[contains(.,'Numero de Legajo')]"

    item_cuenta_dbt = "(//span[contains(.,'{}')])[2]"
    
    item_cuenta_dbt_2 = "//span[contains(.,'{}')]"


    input_dni_2 = "//input[contains(@formcontrolname,'nroDocumento')]"
    
    input_dni_3 = "//input[contains(@formcontrolname,'numeroDocumento')]"
    
    input_legajo = "//input[contains(@formcontrolname,'nroLegajo')]"
    
    input_comprobante = "//input[contains(@formcontrolname,'comprobante')]"
    
    
    btn_reintegro_de_vales = "//span[contains(.,'Reintegro de Vales')]"

    btn_listado_de_caja_chica = "//span[contains(.,'Listado de Caja Chica')]"
    
    btn_barra = "(//span[contains(.,'BARRA')])[1]"
    
    recuadro_servicio = "//mat-select[contains(@formcontrolname,'service')]"
    
    item_servicio = "//span[@class='mat-option-text'][contains(.,'{}')]"
    
    input_codigo_barra = "//input[contains(@formcontrolname,'codigo')]"
    
    datos_servicio = "//it-card[@class='mb-3']"
    
    
#CIERRE FORZADO 

    btn_cierre_forzado = "//span[contains(.,'Cierre Forzado de Caja')]"
    
    btn_cancelar= "//span[contains(.,'Cancelar')]"


    slc_rdo_operadores = "//mat-form-field[contains(.,'Operadores')]"
    
    list_operadores = "//div[contains(@role,'listbox')]"
    
    check_saldos = "(//span[contains(@class,'mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin')])[{}]"
    
    btn_cerrar_caja = "//span[contains(.,'CIERRE DE CAJA')]"
    
    
    msg_exito_no_hay_operadores_activos  = "//h6[@class='title'][contains(.,'Operadores no disponibles')]"


#COBROS CML/sire

    btn_cobros_sire = "//span[contains(.,'Cobro de Servicios - SIRE')]"


    btn_cobros_cml = "//span[contains(.,'Servicio de Cobros CML')]"
    
    check_box_mismo_doc = "//span[contains(.,'Mismo Documento que Cliente Identificado')]"
    
    btn_siguiente_5 ="//span[contains(.,'Siguiente')]"
    
    recuadro_c_h = "//mat-select[contains(@tabindex,'0')]"
    
    item_cobros_cml = "//span[@class='mat-option-text'][contains(.,'{}')]"
    
    siguiente_6 = "(//span[@class='mat-button-wrapper'][contains(.,'Siguiente')])[2]"
    
    b_nuevo_doc = "//b[contains(.,'Nuevo Documento')]"
    
    recuadro_tipo = "(//mat-select[contains(@role,'combobox')])[3]"
    
    factura = "(//div[contains(.,'FACTURA')])[7]"
    
    imput_numero = "//input[contains(@maxlength,'22')]"
    
    imput_cuota = "//input[contains(@formcontrolname,'cuota')]"
    
    input_monto = "//input[contains(@formcontrolname,'monto')]"
    
    btn_agregar = "//span[@class='mat-button-wrapper'][contains(.,'AGREGAR')]"
    
    flecha_azul_claro = "(//button[@class='btn btn-link d-inline'][contains(.,'->')])[2]"
    
    monto_validar = "//button[@class='btn btn-link font-weight-bold text-success'][contains(.,'{}')]"
    
    btn_fin_de_carga = "//button[@color='primary'][contains(.,'Fin carga')]"

    btn_SI = "//button[contains(.,'si')]"
    
    btn_NO  = "//button[contains(.,'no')]"
    
    datos_resumen = "//div[contains(@class,'row frame')]"
    
    imput_monto_2 ="//input[contains(@maxlength,'15')]"

    input_monto_3 = "(//input[contains(@formcontrolname,'monto')])[3]"

    input_monto_5 = "(//input[contains(@formcontrolname,'monto')])[5]"

    btn_costumeres = "//i[contains(@class,'it-icon-chevron-right')]"
    
    btn_imprimir_2 = "//span[contains(.,'Imprimir')]"
    
    btn_calendario = "//button[contains(@aria-label,'Open calendar')]"
    
    td_fecha = "//td[@aria-label='{} de {} de {}']"

    btn_fin_de_carga_2 = "//button[@color='primary'][contains(.,'Fin Carga')]"

    recuadro_cuentas_debito = "//mat-select[contains(@formcontrolname,'cuentasCliente')]"
    
    item_cuentas_debito = "//span[@class='mat-option-text'][contains(.,'{}')]"
    
    btn_coincide = "//span[contains(.,'Marcar si coincide')]"
    
    recuadro_pagos ="//mat-select[contains(@role,'combobox')]" 
    
    item_pago="//mat-option[@role='option'][contains(.,'CC $ - 0000178-100/4')]" 
    
    btn_debito_cuenta ="(//span[contains(.,'Debito en Cuenta')])[2]"
    
    datos_moneda_cambio  = "(//div[contains(@class,'content-card content-background')])[1]"
    
    datos_pdf = "/html[1]/body[1]/pre[1]"
    
### MONEDA EXTRANJERA 

    dato_moneda_extranjera = "//mat-horizontal-stepper[contains(@role,'tablist')]"