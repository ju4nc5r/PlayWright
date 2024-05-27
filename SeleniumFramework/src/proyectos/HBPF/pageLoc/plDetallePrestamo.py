class plDetallePrestamo(object):
    colTable_inicio_prestamo = (
        "//*[@id='sectionPrestamos_repeat0_collectionTable0312354321_ON-REGISTER']")
    label_tituloDetallePrestamo = (
        "//*[@id='constantLabel0' and contains(.,'Detalle del Pr')]")
    cmdButton_volver_aInicio = (
        "//*[@id='actionButton1' and contains(.,'Volver')]")
    
    
    text_tipoPrestamo = (
        "//*[@id='textField0']")
    text_numeroPrestamo = (
        "//*[@id='textField1']")
    text_montoOriginal = (
        "//*[@id='floatField0']")
    text_otrosGastos = (
        "//*[@id='floatField3']")
    text_montoCancelacion = (
        "//*[@id='floatField5']")
    text_CFTEA = (
        "//*[@id='floatField2']")
    
    
    cmdButton_detalleCuotas = (
        "//*[@id='nextState']")
    label_tituloDetalleCuotas = (
        "//*[@id='constantLabel0' and contains(.,'Detalle de cuotas')]")
    cmdButton_volver_aPrestamo = (
        "//*[@id='Volver']")
    td_numeroCuota = (
        "//td[@sortvalue='{}']")