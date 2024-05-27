# -*- coding: utf-8 -*-
class plResumenDigital(object):
    lbl_titulo = (
        "//label[contains(text(),'Resumen digital de cuentas')]"
    )
    
    cbo_cuenta = "//select[@caption='Cuenta']"
    
    cbo_anio = "//select[contains(@caption,'Año')]"
    
    imgLupaFecha1 = "(//img[@src='images/lupa.gif'])[1]"
    
    pdfResumen = "//div[@class='div_campos_interno'][contains(.,'Your browser does not support embedded PDF files.')]"
       
    btnCerrar = "//p[contains(.,'Cerrar')]"
    
    lnkResumenDigital = "//p[contains(.,'resumen digital')]"
    
   
    
  
#     
#     
