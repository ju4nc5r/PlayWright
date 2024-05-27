# -*- coding: utf-8 -*-
class plRecargaCelulares(object):
    lbl_titulo = (
        "//label[contains(text(),'Recarga de celulares')]"
    )
    
    cbo_cuenta_a_debitar = "//select[@caption='Cuenta a debitar']"
    
    cbo_operadora = "//select[@caption='Operadora']"
    
    cbo_numero = "//select[@title='Número de celular']"
    
    txtCodArea = "//input[contains(@title,'Código de área')]"
    
    txtNumero = "//input[contains(@title,'mero de celular')]" 
    
    txtDescripcion = "//input[@title='description']"
    
    cboImporte = "//select[@caption='importe cuota']"
    
    btnContinuar = "//p[contains(.,'continuar')]"
    
    btnConfirmar = "//button[contains(.,'Confirmar')]"
    
    frmTicket = "//*[@id='tableAlignFileComponent']"
    
    pdfTicket = "//*[@id='pdf']"
    
    msgExitoSinTicket = "//p[contains(.,'La transacción se realizó con éxito pero no se pudo generar el ticket.')]"
    
    
    

    
    btnContinuaTkt =   "//p[contains(.,'Continuar')]"      
#     
#     
