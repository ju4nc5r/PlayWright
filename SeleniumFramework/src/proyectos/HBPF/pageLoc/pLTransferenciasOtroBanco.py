# -*- coding: utf-8 -*-
class plTransferenciasOtroBanco():

    title_transferencia_otro_banco = (
        "//span[contains(@class,'title-span') and "
        "contains(.,'Transferencia a otro banco')]"
    )
    list_cta_debito = "//select[contains(@caption,'Cuenta de d')]"
    option_transferInmediata = "//*[@id='radioButtonField2_opt_0']"
    option_transferNoInmediata = "//*[@id='radioButtonField2_opt_1']"
    list_cta_destino = "//select[@caption='Cuenta destino']"
    option_alias = "//option[contains(.,'Alias de la cuenta destino')]"
    input_cta_destino = "//input[contains(@class,'text-field_medium_nolabel')]"
    cmd_agenda = "/descendant::button[contains(.,'Agenda')][1]"
    list_caractCtaAcredit_uno = (
        "descendant::select[contains(@caption,'stica de la cuenta de acreditaci')][1]"
    )
    list_caractCtaAcredit = (
        "descendant::select[contains(@caption,'stica de la cuenta de acreditaci')][2]"
    )
    input_descCtaAcredit = (
        "//input[contains(@caption,'n cuenta de acreditaci')]"
    )
    check_AgendarDestinatario = (
        "/descendant::input[@caption='Agendar destinatario'][1]"
    )
    list_concepto = "//select[@id='TELECTFIELD']"
    inputDescConcepto = "//input[contains(@caption,'n concepto')]"
    inputImporte = "//input[contains(@caption,'Importe')]"
    select_moneda = "(//select[@caption='Moneda'])[1]"
    checkEnviarAviso = (
        "descendant::input[@caption='Enviar aviso al destinatario'][1]"
    )
    cmdCancelar = "descendant::button[contains(.,'Cancelar')][1]"
    cmdLimitesDiarios = "//button[contains(.,'mites Diarios')]"
    cmdContinuar = "//button[contains(.,'Continuar')]"
    div_error = "//div[@id='errorPanel']"
    # 2da Pantalla
    checkAccedoDesdePcPublica = (
        "//input[contains(@caption,'Accedo desde una PC p')]"
    )
    inputCoordenada1 = (
        "//input[contains(@caption,'Ingresar la primer coordenada')]"
    )
    inputCoordenada2 = (
        "//input[contains(@caption,'Ingresar la segunda coordenada')]"
    )
    inputClaveCajeroAutomatico = (
        "//input[contains(@caption,'La clave que utiliza en el "
        "cajero electrónico')]"
    )
    cmdConfirmar = (
        "//button[contains(@class,'action-button_main') and "
        "contains(.,'Confirmar')]"
    )
    table_comprobante = "//table[@id='tableAlign07']"

    table_Cuentas = '//*[@id="tableAlign065432"]'
    check_concepto = '//*[@id="conceptsCodeCheckField"]'
    spn_tipoTransferencia = "//span[contains(@caption,'Tipo de transferenc')]"
    spn_cuentaDebito = "//span[contains(@caption,'Cuenta d')]"
    spn_cbuAcred = "//span[contains(@caption,'CBU')]"
    spn_caracteristica = "//span[contains(@caption,'Caracter')]"
    spn_titular = "//span[contains(@caption,'Titular')]"
    spn_cuil = "//span[contains(@caption,'CUIL')]"
    spn_concepto = "//span[contains(@caption,'Concepto')]"
    spn_importe = "(//span[contains(@caption,'Importe a transferir')])[2]"

    # trasnferencia no indmediata

    cbu_no_inmediata = "//input[contains(@caption,'CBU')]"
    caracte_no_inmediata = "descendant::select[contains(@caption,'de la cuenta de')][2]"
    descrip_no_inmediata = "descendant::input[contains(@caption,'cuenta de acreditac')][2]"
    cuil_no_inmediata = "descendant::input[contains(@caption,'CUIL/CUIT/CDI')]"
    concepto_no_inmediata = "descendant::select[contains(@caption,'Concepto')][2]"
    descripConcepto_no_inmediata = "descendant::input[contains(@caption,'n concepto')][2]"
    importe_no_inmediata = "descendant::input[contains(@caption,'Importe')][2]"

    continuar_no_inmediata = "descendant::button[contains(.,'Continuar')][2]"
