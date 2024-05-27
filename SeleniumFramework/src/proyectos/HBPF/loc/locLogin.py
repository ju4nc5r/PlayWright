# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plLogin import plLogin


class locLogin():

    # inputUsuario = (By.XPATH, plLogin.txt_usuario_xpath)
    inputUsuario = (plLogin.txt_usuario_xpath)
    cmdContinuar = (plLogin.btn_avanzar_xpath)
    inputClave = (plLogin.txt_clave_xpath)
    cmdIngresar = (plLogin.btn_ingresar_xpath)
    lblError_msg = (plLogin.lbl_error_msg)
    texto_Error = (plLogin.texto_lbl_error_msg)
    clave_vencida = plLogin.lbl_ClaveUsuarioInvalido_xpath

    boton_registro = plLogin.btn_adherir_xpath
    boton_recupero = plLogin.lnk_olvide_xpath

    titulo_esperado = plLogin.titulo_inicio
    input_cod_activacion = plLogin.input_codigo

    btnConfig = plLogin.boton_config
    btnSalir = plLogin.boton_salir
    lblCerrarSesion = plLogin.label_cerrar_sesion
    
    registrarDispositivo = plLogin.banner_registro
    boton_noregistrar = plLogin.btn_noRegistrar
    
    button_reingreso = plLogin.button_reingreso

    seg_user = plLogin.seg_user
    seg_pass = plLogin.seg_pass
    seg_buttonSingIn = plLogin.seg_singIn