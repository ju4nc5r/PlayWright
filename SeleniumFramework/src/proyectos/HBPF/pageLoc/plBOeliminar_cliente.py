# -*- coding: utf-8 -*-
class plBOeliminar_cliente():
    txt_usuario_xpath = "//input[contains(@placeholder,'Usuario')]"
    btn_avanzar_xpath = "//button[contains(@id,'actionButtonIngresar')]"
    txt_clave_xpath = "//input[contains(@name,'password')]"
    btn_ingresar_xpath = "//button[contains(@id,'actionButtonIngresar')]"
    titl_control_center = "//span[contains(.,'Control Center')]"
    menu_administrarClientes = "//span[contains(@id,'span_enterprise')]"
    subMenu_cliente = "descendant::b[contains(.,'Clientes')][2]"
    h1_title_busquedaEmpresas = (
        "descendant::div[contains(.,'squeda de empresas')][4]")
    lbl_tipoDocumento = "//select[contains(@id,'tipoDocumento')]"
    input_nro_doc = "//input[contains(@id,'numeroDocumento')]"
    cmd_buscar_bo = "//input[@value='Buscar']"
