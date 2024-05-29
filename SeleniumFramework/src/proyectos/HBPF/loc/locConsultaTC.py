from SeleniumFramework.src.proyectos.HBPF.pageLoc.plConsultaTC import plConsultaTC
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plLogin import plLogin


class locConsultaTC(object):
    titulo_consultaTC = plConsultaTC.titulo_esperado
    sel_tarjeta = plConsultaTC.select_tarjeta
    btn_adherirDebAuto = plConsultaTC.button_adherirDebAuto
    tbl_detalle = plConsultaTC.tablle_detalle
    txt_debAuto = plConsultaTC.span_debAutomatico
    txt_stopDeb = plConsultaTC.span_stopDeb
    txt_limCompra = plConsultaTC.span_limCompra
    span_modif_debito = plConsultaTC.span_modif_debito

    btn_volver = plConsultaTC.button_volver
    btn_bloqueo = plConsultaTC.button_bloqueo
    btn_reposicion = plConsultaTC.button_reposicion
    btn_pagar = plConsultaTC.button_pagar
    btn_cerrar = plConsultaTC.button_cerrar
    btn_cancelarBloq = plConsultaTC.button_cancelar_bloqueo
    btn_cancelarAdherirDebAuto = plConsultaTC.button_cancelar_adherirDebAuto
    href_pagosPesos = plConsultaTC.a_pagosRealizadosPesos
    href_pagosDolares = plConsultaTC.a_pagosRealizadosDolar
    tabla_pagosRealizados = plConsultaTC.table_pagosRealizados

    tabla_bloqueo = plConsultaTC.tabla_bloqueo

    titulo_inicio = plLogin.titulo_inicio
    titulo_reposicion = plConsultaTC.titulo_reposicion
    titulo_pagar = plConsultaTC.titulo_pagar
    div_error = plConsultaTC.div_error
    titulo_adicionales = plConsultaTC.titulo_adicionales
