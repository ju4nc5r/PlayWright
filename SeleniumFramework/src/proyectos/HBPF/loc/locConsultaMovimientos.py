from SeleniumFramework.src.proyectos.HBPF.pageLoc.plConsultaMovimientos import (
    plConsultaMovimientos as plCM)


class locConsultaMovimiento(object):
    titulo = plCM.titulo
    lbl_cuenta = plCM.label_cuenta
    sel_cuenta = plCM.select_cuenta
    lbl_movimiento = plCM.label_movimiento
    sel_movimiento = plCM.select_movimiento
    btn_volver = plCM.button_volver
    tbl_movimiento = plCM.table_movimientos
    tbl_sinResultado = plCM.p_sinResultado
    inp_importeDesde = plCM.input_importeDesde
    inp_importeHasta = plCM.input_importeHasta
    inp_fechaDesde = plCM.input_fechaDesde
    inp_fechaHasta = plCM.input_fechaHasta
    btn_buscar = plCM.button_buscar
    div_error = plCM.div_error
    # Para visualizar el movimiento, se tiene que pasar x format el indice
    opc_visualizar = plCM.img_visualizarMovimiento

    # cuenta CA
    segunda_cuenta = plCM.segunda_cuenta

    # Pantalla de detalle
    titulo_detalle = plCM.titulo_detalle
    txt_operacion = plCM.span_operacion
    txt_fechaRealizacion = plCM.span_fecha_realizacion
    txt_horaRealizacion = plCM.span_hora_realizacion
    txt_fechaImputacion = plCM.span_fecha_imputacion
    txt_cuenta = plCM.span_cuenta
    txt_terminal = plCM.span_terminal
    txt_canal = plCM.span_canal
    txt_numReferencia = plCM.span_numReferencia
    txt_moneda = plCM.span_moneda
    txt_debCred = plCM.span_DebOCred
    txt_importe = plCM.span_importe

    # error

    no_movimientos = plCM.no_movimientos
