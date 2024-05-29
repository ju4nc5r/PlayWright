# -*- coding: utf-8 -*-
class plInversiones(object):
    td_plazoFijo = "//tr[contains(@id,'Inversiones_repeat1_collectionTable031235xx3q_ON-REGISTER')][1]"
    td_fondosComunes = (
        "//*[@id='Inversiones_repeat0_collectionTable031235xx_ON-REGISTER' "
        "and contains(.,'{}')]"
    )
    td_TitulosValores = (
        "//*[@id='Inversiones_repeat0_collectionTablePossession_ON-REGISTER' "
        "and contains(.,'{}')]"
    )
    td_plazoFijo_Efectivo = (
        "//*[contains(@id,'Inversiones') and contains(@id,'ON-REGISTER') "
        "and contains(.,'{}')]"
    )
    label_titulo_PlazoFijo = (
        "//*[@id='constantLabel0' and contains(.,'Plazo Fijo')]"
    )
    cmdButton_Volver_aInicio = (
        "//*[@id='actionButton100' and contains(.,'Volver')]"
    )
    cmdButton_tasasVigentes = "//button[@id='tasas_vigentes']"
    label_titulo_TasasVigentes = (
        "//*[@id='constantLabel0' and contains(.,'Tasa nominal anual')]"
    )
    cmdButton_cerrar_TasasVigentes = "//*[@id='Volver2']"
    span_tipoPlazoFijo = "//span[@id='textField0784']"
    sapn_numeroPlazoFijo = "//span[@id='textField04542']"
    span_fechaConstitucion = "//span[@id='dateField0']"
    span_fechaVencimiento = "//span[@id='dateField1']"
    span_plazo = "//span[@id='intField0']"
    span_renovacionAutomatica = "//span[@id='optionField0']"
    span_TNA = "//span[@id='floatField0']"
    span_TEA = "//span[@id='floatField1']"
    span_montoInicial = "//span[@id='floatField1144']"
    span_interesesDevegar = "//span[@id='floatField111']"
    span_montoAlVencimiento = "//span[@id='floatField144']"
    span_cuentaDebito = "//span[@id='richText0xx']/p"
    span_cuentaAcreditacion = "//span[@id='richText1']/p"
