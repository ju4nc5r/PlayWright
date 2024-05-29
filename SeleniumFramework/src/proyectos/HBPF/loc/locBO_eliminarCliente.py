# -*- coding: utf-8 -*-
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plBOeliminar_cliente import plBOeliminar_cliente
from SeleniumFramework.common_functions import desbloqueoUsuarios


class locBO_eliminarCliente():

    inputUsuario = (plBOeliminar_cliente.txt_usuario_xpath)
    cmdContinuar = (plBOeliminar_cliente.btn_avanzar_xpath)
    inputClave = (plBOeliminar_cliente.txt_clave_xpath)
    cmdIngresar = (plBOeliminar_cliente.btn_ingresar_xpath)
    titulo_controlCenter = (plBOeliminar_cliente.titl_control_center)

    menuAdministracionClientes = (
        plBOeliminar_cliente.menu_administrarClientes
    )
    subMenu_cliente = (plBOeliminar_cliente.subMenu_cliente)
    Tit_busquedaEmpresas = (plBOeliminar_cliente.h1_title_busquedaEmpresas)
    
    desbloqueo_Operador = plBOeliminar_cliente.btn_desbloqueo

    TipoDocumento = (plBOeliminar_cliente.lbl_tipoDocumento)
    NroDocumento = (plBOeliminar_cliente.input_nro_doc)

    cmdBuscar = (plBOeliminar_cliente.cmd_buscar_bo)