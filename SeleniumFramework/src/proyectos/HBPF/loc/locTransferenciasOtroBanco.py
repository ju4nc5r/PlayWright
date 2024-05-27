from SeleniumFramework.src.proyectos.HBPF.pageLoc.pLTransferenciasOtroBanco import plTransferenciasOtroBanco


class locTransferenciasOtroBanco():

    Titulo = plTransferenciasOtroBanco.title_transferencia_otro_banco
    ctaDebito = plTransferenciasOtroBanco.list_cta_debito
    TransfInmediata = plTransferenciasOtroBanco.option_transferInmediata
    TransfNoInmediata = plTransferenciasOtroBanco.option_transferNoInmediata
    cbuAliasDestino = plTransferenciasOtroBanco.list_cta_destino
    optionAlias = plTransferenciasOtroBanco.option_alias
    inputCbuAlias = plTransferenciasOtroBanco.input_cta_destino
    caractCtaAcreditacion_uno = plTransferenciasOtroBanco.list_caractCtaAcredit_uno
    caractCtaAcreditacion = plTransferenciasOtroBanco.list_caractCtaAcredit
    
    descCtaAcreditacion = plTransferenciasOtroBanco.input_descCtaAcredit
    checkAgendarDestinatario = (
        plTransferenciasOtroBanco.check_AgendarDestinatario)
    concepto = plTransferenciasOtroBanco.list_concepto
    descConcepto = plTransferenciasOtroBanco.inputDescConcepto
    importe = plTransferenciasOtroBanco.inputImporte
    moneda = plTransferenciasOtroBanco.select_moneda
    checkEnviarAviso = plTransferenciasOtroBanco.checkEnviarAviso
    div_error = plTransferenciasOtroBanco.div_error
#     email=plTransferenciasOtroBanco.
#     comentario=plTransferenciasOtroBanco.
    cancelar = plTransferenciasOtroBanco.cmdCancelar
    limitesDiarios = plTransferenciasOtroBanco.cmdLimitesDiarios
    continuar = plTransferenciasOtroBanco.cmdContinuar
    # 2da Pantalla
    check_AccesoPcPublica = plTransferenciasOtroBanco.checkAccedoDesdePcPublica
    coordenada1 = plTransferenciasOtroBanco.inputCoordenada1
    coordenada2 = plTransferenciasOtroBanco.inputCoordenada2
    claveCajero = plTransferenciasOtroBanco.inputClaveCajeroAutomatico
    confirmar = plTransferenciasOtroBanco.cmdConfirmar
    txt_tipoTransferencia = plTransferenciasOtroBanco.spn_tipoTransferencia
    txt_cuentaDebito = plTransferenciasOtroBanco.spn_cuentaDebito
    txt_cbuAcred = plTransferenciasOtroBanco.spn_cbuAcred
    txt_caracteristica = plTransferenciasOtroBanco.spn_caracteristica
    txt_titular = plTransferenciasOtroBanco.spn_titular
    txt_cuil = plTransferenciasOtroBanco.spn_cuil
    txt_concepto = plTransferenciasOtroBanco.spn_concepto
    txt_importe = plTransferenciasOtroBanco.spn_importe
    # 3ra Pantalla
    comprobante = plTransferenciasOtroBanco.table_comprobante
    tabla_Cuentas = plTransferenciasOtroBanco.table_Cuentas
    checkConcepto = plTransferenciasOtroBanco.check_concepto

    # No inmediata 
    cbu_no_inmediata = plTransferenciasOtroBanco.cbu_no_inmediata
    caracte_no_inmediata = plTransferenciasOtroBanco.caracte_no_inmediata
    descrip_no_inmediata = plTransferenciasOtroBanco.descrip_no_inmediata
    cuil_no_inmediata = plTransferenciasOtroBanco.cuil_no_inmediata
    concepto_no_inmediata = plTransferenciasOtroBanco.concepto_no_inmediata
    descripConcepto_no_inmediata = plTransferenciasOtroBanco.descripConcepto_no_inmediata
    importe_no_inmediata = plTransferenciasOtroBanco.importe_no_inmediata
    continuar_no_inmediata = plTransferenciasOtroBanco.continuar_no_inmediata
