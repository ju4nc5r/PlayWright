# -*- coding: utf-8 -*-
class plLogin():

    # Casilla Usuario
    txt_usuario_xpath = "//*[@id='login_textField0']"
    txt_usuario_id = "login_textField0"

    # Boton Avanzar despues de ingresar usuario
    btn_avanzar_xpath = "//button[contains(.,'Continuar')]"
    btn_avanzar_id = "nextStateCont"

    # Casilla Clave
    txt_clave_xpath = "//*[@id='login_textField1']"
    txt_clave_id = "login_textField1"

    # Boton Ingresar despues de ingresar usuario
    btn_ingresar_xpath = '//*[@id="nextStateCont"]'
    btn_ingresar_id = "nextStateIngresar"

    # Olvide Mi Clave
    lnk_olvide_xpath = "//*[@id='Olvide']"
    lnk_olvide_id = "Olvide"

    # Boton Registrarme Ahora (adherir)
    btn_adherir_xpath = "//*[@id='nextAdherir']"
    id_adherir_xpath = "nextAdherir"

    # Accedo desde Una PC Publica
    lnk_PCPublica_xpath = "//*[@id='constantLa2bel0dxddvvv']"
    lnk_PCPublica_id = "constantLa2bel0dxddvvv"
    chk_PCPublica_xpath = "//*[@id='checkField0']"
    chk_PCPublica_id = "checkField0"

    # ELEMENTOS DE LOGUEO NO EXITOSO
    # USUARIO INVALIDO
    lbl_ClaveUsuarioInvalido_xpath = (
        "//*[@id='richText0' and contains(.,'Tu clave de acceso')] ")
    # Clave Usuario Invalido
    lbl_ClaveUsuarioInvalido_id = "richText0"

    # USUARIO BLOQUEADO
    lbl_UsuarioBloqueado_xpath = "//*[@id='richText0']/div"

    # CLAVE VENCIDA
    lbl_ClaveVencida_xpath = "//*[@id='richText0']/p/b/font"
    LBL_MensajeClaveVencida_xpath = "//*[@id='tableAlign15']/tbody/tr/td"

    # Cambio de clave
    lbl_Titulo_ClaveVencida_xpath = "//*[@id='constantLabel0']"

    # TITULO APLICACION USUARIO VENCIDO
    lbl_Titulo_Usuario_Vencido = "//*[@id='constantLabel0']"

    # CLAVE ACTUAL
    txt_Clave_Actual_xpath = "//*[@id='textField1']"
    lbl_Clave_Actual_xpath = "//*[@id='constantLabel01']"

    # CLAVE NUEVA
    txt_Clave_Nueva_xpath = "//*[@id='textField2']"
    lbl_Clave_Nueva_xpath = "//*[@id='constantLabel1']"

    # REINGRESA CLAVE NUEVA
    txt_Reingresa_Clave_Nueva_xpath = "//*[@id='textField3']"
    lbl_Reingresa_Clave_Nueva_xpath = "//*[@id='constantLabel2']"

    # BOTONES
    btn_Cancelar_Clave_Vencida_xpath = "//*[@id='actionButton0']"
    btn_Continuar_Clave_Vencida_xpath = "//*[@id='Continuar']"

    # 0008-0009
    lbl_ClaveVencidaMensaje = "//*[@id='richText0']/p[1]/b/font"

    # USUARIO VENCIDO
    # Usuario vencido se corrobora con el txt de ingreso de nuevo usuario
    txt_UsuarioVencido_xpath = "//*[@id='label_textField1']"
    # Ingresá un nuevo usuario

    # se muestra el mensaje de cambio de usuario
    lbl_UsuarioVencido_xpath = "//*[@id='richText0']/p[2]/font"

    # Cambio de usuario
    lbl_Titulo_UsuarioVencido_xpath = "//*[@id='constantLabel0']"

    # USUARIO DESADHERIDO
    # SE CORROBORA CON LA ETIQUETA DE SOLICITUD DE ACTIVACION DE USUARIO
    lbl_CompletarAdhesion_xpath = "//*[@id='constantLabel2']"
    lbl_Completar_Adhesion_Titulo_xpath = "//*[@id='constantLabel0']"
    lbl_Codigo_Activacion_xpath = "//*[@id='label_textField1']"
    # Código de activación

    # INTENTE MAS TARDE
    lbl_IntenteMasTarde_xpath = "//*[@id='table1']"
    btn_IntenteMasTarde_xpath = "//*[@id='nextStateCan']"
    lbl_Intenta_Mas_arde_Msj_xpath = "//*[@id='constantLabel0']"

    # USUARIO BLOQUEADO
    lbl_Usuario_Bloqueado_Msj_xpath = "//*[@id='richText0']/div"

    # TERMINOS Y CONDICIONES
    lbl_TerminosyCondiciones_xpath = "//*[@id='constantLabel06']"
    # Términos y condiciones

    chk_acepto_xpath = "//*[@id='checkField0']"
    btn_Cancelar_xpath = "//*[@id='nextStateCancelar']"
    btn_Descargar_xpath = "//*[@id='tablealign_rightButtons2']/tbody/tr/td/a"
    btn_Aceptar_xpath =  "//*[@id='nexstate1']"
    txt_contrato_xpath = "//*[@id='textField0']"

    # Mensajes de error Login
    # lbl_error_msg="//*[@id='constantLabel0']"
    lbl_error_msg = '//*[@id="tableAlignFalta"]'
    texto_lbl_error_msg = "//*[@id='constantLabel0']"
    input_codigo = "//input[@id = 'textField1']"
    titulo_inicio = (
        "//label[contains(@class,'title-noline-nomargin') and "
        "contains(.,'Cuentas')]"
    )
    boton_config = "//a[@id='CONFIGURACION']"
    boton_salir = "//a[@id='Salir']"
    label_cerrar_sesion = ("//p[contains(.,'Hasta luego') and contains(.,'de forma correcta')]")
#     label_cerrar_sesion = ("//label[contains(text(),'finalizada correctamente')]")

    # Cartel de Registro de Dispositivo
    
    banner_registro = "//table[@id='table0']"
    btn_noRegistrar = "//button[@id='nextStateNoRegistrar']"
    
    button_reingreso = "//a[contains(text(),'acá')]"

    seg_singIn = "//body/div[1]/div[3]/main[1]/div[1]/div[4]/form[1]/div[1]/input[13]"
    seg_user = "//input[@id='login_field']"
    seg_pass = "//input[@id='password']"