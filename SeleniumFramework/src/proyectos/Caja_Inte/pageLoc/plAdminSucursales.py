# -*- coding: utf-8 -*-
class plAdminSucursales():
    
    mnuBtnSucursales = "//span[@class='mat-button-wrapper'][contains(.,'Sucursales')]/.."
    
    txt_titulo = "//h1[contains(.,'{}')]"

    recuadro_operador = "//table[contains(@class,'mat-table')]"
    
    txt_titulo_apertura_forzada = "//div[@class='mat-dialog-content'][contains(.,'Se procederá a la apertura forzada de la sucursal luego de un cierre forzado.')]"

    btn_operador = "//td[contains(.,'{}')]//preceding-sibling::td[1]//mat-radio-button"

    btn_aceptar = "//button[contains(.,'Aceptar')]"
    msjAperturaExitosa = "//div[@class='mat-dialog-content'][contains(.,'Se ha asignado correctamente el operador centralizador:') and contains(.,'Apertura de sucursal realizada!')]"
#     msjOk = "//div[contains(@class,'header') and contains(.,'Se ha asignado correctamente el operador centralizador. Apertura de caja realizada !')]"

# Para ver despues y agregar el usuario
#     msgOk=""//div[@class='mat-dialog-content'][contains(.,'Se ha asignado correctamente el operador centralizador:UIC10003  .
# Apertura de sucursal realizada!')]"

    msjErrCajaYaEstaAbierta = "//div[@class='mat-dialog-content'][contains(.,'No se puede aperturar la sucursal,ya se encuentra abierta')]"
#     msjSkip = "//div[contains(@class,'alertMessage') and contains(.,'No se pudo realizar la apertura de la caja. La caja ya se abrio y hay un usuario asignado para cerrarla')]"
   
    btnCerrar= "//button[@class='btnYes'][contains(.,'Cerrar')]"
    
    btnYes = "//button[@class='btnYes'][contains(.,'Aceptar')]"

    btnNo = "//button[@class='btnNo'][contains(.,'Cancelar')]"