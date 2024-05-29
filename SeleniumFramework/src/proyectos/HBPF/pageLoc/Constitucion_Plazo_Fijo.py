# -*- coding: utf-8 -*-
class Constitucion_Plazo_Fijo():

    # Ingresar datos
    lbl_constitucion_plazo_fijo_xpath = "//*[@id='constantLabel0']"

    # SIMULAR#
    lbl_cuenta_xpath = "//*[@id='label_selectField0']"
    dpd_cuenta_xpath = "//*[@id='selectField0']"
    lbl_tipo_plazo_fijo_xpath = "//*[@id='label_selectField20']"
    dpd_tipo_plazo_fijo_xpath = "//*[@id='selectField20']"
    lbl_plazo_xpath = "//*[@id='label_intField30']"
    txt_plazo_xpath = "//*[@id='intField30']"
    lbl_fecha_vencimiento_xpath = "//*[@id='label_dateField0']"
    txt_fecha_vencimiento_xpath = "//*[@id='dateField0']"
    lbl_monto_inicial_xpath = "//*[@id='label_floatField0']"
    txt_monto_inicial_xpath = "//*[@id='floatField0']"
    btn_cancelar_xpath = "//*[@id='nextStateVolver']"
    btn_tasas_vigentes_xpath = "//*[@id='nextStateTasas1']"
    btn_simular_xpath = "//*[@id='nextStateSimular']"
    btn_popup_Volver_xpath = "//*[@id='Volver2']"
    lbl_ConfirmacionDeTransaccion_xpath = (
        "//*[@id='richText0']//*[contains(., 'realizada con')]")

    # Mensaje de error
    lbl_mensaje_Error_CuentaObligatorio__xpath = "//*[@id='errorPanel']/ul/li"
    lbl_mensaje_Error_MayorACero_xpath = "//*[@id='errorPanel']/ul/li"
    lbl_Contenedor_Errores_xpath = "//*[@id='errorPanel']"
    lbl_Dia_No_Habil_xpath = "//*[@id='richText0xx']/p"
    lbl_SaldoInsuficiente_Xpath = "//*[@id='errorPanelCollection']/p"
    # u"El saldo disponible para realizar la operación es insuficiente."

    lbl_mensaje_Error_PlazoInferiorA_xpath = "//*[@id='errorPanel']/ul/li"
    # u"Plazo es inferior al mínimo (30)"

    lbl_Fallas_Xpath = "//*[@id='errorPanelCollection']/p"

    # Simulacion de plazo fijo
    lbl_tasas_vigentes_css = "#constantLabel0"
    lbl_fecha_css = "#label_dateField1"
    lbl_fecha_dia_css = "#dateField1"

    # CONSTITUIR#
    lbl_TNA_xpath = "//*[@id='label_floatField60']"
    lbl_TEA_xpath = "//*[@id='label_floatField61']"
    lbl_TNA_Simulacion_xpath = "//*[@id='tableAlign166']/tbody/tr[3]/td"
    lbl_TEA_Simulacion_xpath = "//*[@id='tableAlign166']/tbody/tr[4]/td"
    lbl_intereses_devengar_xpath = "//*[@id='constantLabel010']"
    lbl_monto_vencimiento_xpath = "//*[@id='constantLabel10110']"
    lbl_Impuesto_Sellos_xpath = "//*[@id='tableAlign166']/tbody/tr[9]/td"
    btn_cancelar2_xpath = "//*[@id='nextStateCancelNA']"
    btn_constituir_plazo_xpath = "//*[@id='nextStateConstNA']"
    btn_continuar_xpath = "//*[@id='nextStateVolverNA']"
    lbl_exito_xpath = "//*[@id='richText0']"

    # Confirmacion de plazo fijo
    # CONFIRMACION#
    lbl_Confirmacion_PF_Paso2_xpath = "//*[@id='step-process_step-2']/span"
    lbl_Tipo_PlazoFIjo_Paso2_xpath = "//*[@id='tableAlign21']/tbody/tr/td"
    lbl_Fecha_Constitucion_Paso2_xpath = "//*[@id='tableAlign41']/tbody/tr/td"
    lbl_Fecha_Vencimiento_Paso2_xpath = "//*[@id='tableAlign61']/tbody/tr/td"
    lbl_plazo_inicial_Paso2_xpath = "//*[@id='tableAlign81']/tbody/tr/td" 
    lbl_TNA_conf_Paso2_xpath = "//*[@id='tableAlignAjustables']/tbody/tr[7]/td"
    lbl_TEA_conf_Paso2_xpath = "//*[@id='tableAlignAjustables']/tbody/tr[8]/td"
    lbl_monto_inicial_Paso2_xpath = (
        "//*[@id='tableAlignAjustables']/tbody/tr[9]/td")
    lbl_intereses_devengar_Paso2_xpath = (
        "//*[@id='tableAlignAjustables']/tbody/tr[12]/td")
    lbl_Impuestos_Sellos_Paso2_xpath = (
        "//*[@id='tableAlignAjustables']/tbody/tr[16]/td")
    lbl_monto_vencimiento_Paso2_xpath = (
        "//*[@id='tableAlignAjustables']/tbody/tr[17]/td")
    lbl_cuenta_debito_Paso2_xpath = "//*[@id='tableAlign241']/tbody/tr/td"
    lbl_cuenta_acredito_Paso2_xpath = "//*[@id='tableAlign261']/tbody/tr/td"
    btn_cancelar_Paso2_xpath = "//*[@id='nextStateCancelNA']"
    btn_confirmar_Paso2_xpath = "//*[@id='nextStateConstNA']"
    btn_modificar_Paso2_xpath = "//*[@id='nextStateModificarNA']"
    btn_nuevo_plazo_fijo_xpath = "//*[@id='nextStateNuevoPF']"

    # Paso 3 Resultado plazo fijo
    lbl_Resultado_Paso3_xpath = "//*[@id='step-process_step-3']/span"
    lbl_Contenedor_Comprobante_Paso3_xpath = (
        "//*[@id='tableAlignas1']/tbody/tr/td")
    lbl_Comprobante_Paso3_xpath = "//*[@id='imageComponent0']"
    chk_Enviar_mail_Paso3_xpath = "//*[@id='checkField60']"
    lbl_enviar_email_paso3_xpath = "//*[@id='constantLabel01230']"
    txt_email_paso3_xpath = "//*[@id='texto']"
    txt_Comentarios_Email_paso3_xpath = "//*[@id='textArea079']"
    btn_EnviarEmail_Paso3_xpath = "//*[@id='actionButton07890']"
    btn_Nuevo_Plazo_Fijo_Paso3_xpath = "//*[@id='nextStateNuevoPF']"
    btn_Continuar_Paso3_xpath = "//*[@id='label_downloadLink0']"
    btn_descargar_paso3_xpath = "//*[@id='tableAlign1522']/tbody/tr/td[2]"
