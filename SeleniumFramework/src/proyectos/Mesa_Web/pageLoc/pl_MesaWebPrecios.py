# -*- coding: utf-8 -*-
class pl_MesaWebPrecios():
    # Menu precios
    slp_precios = "(//a[@onclick='return false;'][contains(.,'Precios')])[1]"
    
    slp_precios_cierre = "//a[@onclick='return false;'][contains(.,'Precios Cierre')]"

    slp_precios_fci = "//a[@href='/tradingNS/pages/FCI/PreciosFCI.xhtml'][contains(.,'Precios FCI')]"

    slp_admin_precios_cierre = "//a[@href='/tradingNS/pages/configuration/preciosCierre/actualizacionPreciosCierre.xhtml'][contains(.,'Administrar Precios Cierre')]"
    
    btn_exportar = "//input[contains(@name,'j_id_33:j_id_3b')]"
    
    btn_importar = "//input[contains(@name,'j_id_3c:j_id_3i')]"

    btn_seleccionar_archivo = "//input[@type='file'][contains(@id,'3c:file')]"
    
    btn_actualizar_precios = "//input[contains(@name,'j_id_3c:j_id_5s:j_id_5w')]"
    
    btn_aceptar_1 = "//span[contains(.,'Aceptar')]"
    
    msj_actualizados_satisfactoriamente = "//div[@class='ui-pnotify-text'][contains(.,'Precios actualizados satisfactoriamente.')]"

    msj_fondo_actualizado = "//div[@class='ui-pnotify-text'][contains(.,'El precio del Fondo se ha actualizado correctamente.')]"
   
    cell_editar = "(//i[contains(@class,'fa fa-pencil')])[{}]"
    
    input_valor_cuotaparte = "//input[contains(@name,'j_id_4l')]"
    
    btn_aceptar = "//input[contains(@name,'j_id_4r')]"

    