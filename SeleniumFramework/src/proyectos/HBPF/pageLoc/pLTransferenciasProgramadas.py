# -*- coding: utf-8 -*-
class plTransferenciasProgramadas():
# trasnferencia no indmediata
    title_programar_transferencia = (
        "//label[contains(@class,'constant-label_title') and contains(.,'Programar transferencia')]"
    )

    cbu_no_inmediata = "//input[contains(@caption,'CBU')]"
    caracte_no_inmediata = "descendant::select[contains(@caption,'de la cuenta de')]"
    descrip_no_inmediata = "descendant::input[contains(@caption,'cuenta de acreditac')]"
    cuil_no_inmediata = "descendant::input[contains(@caption,'CUIL/CUIT/CDI')]"
    concepto_no_inmediata = "descendant::select[contains(@caption,'Concepto')]"
    descripConcepto_no_inmediata = "descendant::input[contains(@caption,'n concepto')]"
    importe_no_inmediata = "descendant::input[contains(@caption,'Importe')]"

    select_periodo = "//select[contains(@id,'nextStatePerioricidad')]"
    periodo_unica_vez = "//select[contains(@id,'nextStatePerioricidad')]/option[contains(.,'nica vez')]"
    periodo_semanalmente = "//select[contains(@id,'nextStatePerioricidad')]/option[contains(.,'Semanalmente')]"
    periodo_mensualmente = "//select[contains(@id,'nextStatePerioricidad')]/option[contains(.,'Mensualmente')]"

    input_fecha = "//*[contains(@title,'DD/MM/YYYY')]"

    calendario = "//*[contains(@title,'Calendar')]"
    dia_unica_vez = "//*[contains(@data-handler,'selectDay')]"

    dias_repeticiones = "//select[contains(@id,'optionField2')]"

    trans_otro_banco = "//select[contains(@id,'option3')]/option[contains(.,'A otro banco')]"

    continuar_programado = "descendant::button[contains(.,'Continuar')]"

    continuar_no_inmediata = "descendant::button[contains(.,'Continuar')]"

    ctaDebito = "//select[contains(@caption,'Cuenta de d')]"

    validacion_carga_datos = "//li[contains(@class,'step-process_active') and contains(.,'cargar datos')]"

    validacion_confirmacion = "//li[contains(@class,'step-process_active') and contains(.,'confirmac')]"

    validacion_error_dia = "//ul[contains(@class,'error-panel_list')]/li[contains(.,'El d')]"

    validacion_fecha_mayor = "//ul[contains(@class,'error-panel_list')]/li[contains(.,'debe ser una fecha mayor a')]"