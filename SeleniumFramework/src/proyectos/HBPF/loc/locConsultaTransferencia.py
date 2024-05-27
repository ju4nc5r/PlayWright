from SeleniumFramework.src.proyectos.HBPF.pageLoc.plConsultaTransferencia import (
    plConsultaTransferencia as pl
)

class locConsultaTransferencia(object):
    titulo = pl.titulo
    lbl_tipoTransferencia = pl.label_tipoTransferencia
    sel_tipoTransferencia = pl.select_tipoTransferencia
    lbl_sinOperacion = pl.label_sinOperacion
    tbl_tablaResultados = pl.table_resultados
    tr_opcionesTabla = pl.tr_opcionesTabla
    btn_volver = pl.button_volver
    btn_programarTransferencia = pl.button_programarTransferencia

    # Segunda pagina
    tbl_datosProgramcion = pl.table_datosProgramacion
    lbl_cuentaDeb = pl.label_cuentaDebito
    txt_cuentaDeb = pl.span_cuentaDebito
    lbl_cuentaAcred = pl.label_cuentaAcreditacion
    txt_cuentaAcred = pl.span_cuentaAcreditacion
    lbl_fechaSolicitud = pl.label_fechaSolicitud
    txt_fechaSolicitud = pl.span_fechaSolicitud
    lbl_tipoTransferencia = pl.label_tipoTransferencia
    txt_tipoTransferencia = pl.span_tipoTransferencia
    lbl_periodicidad = pl.label_periodicidad
    txt_periodicidad = pl.span_periodicidad
    lbl_repeticiones = pl.label_repeticiones
    txt_repeticioens = pl.span_repeticiones
    lbl_importe = pl.label_importe
    txt_importe = pl.span_importe
    btn_eliminar = pl.button_eliminar
    tbl_detalleEjecuciones = pl.table_detalleEjecuciones
    rdo_opcionesEjecuciones = pl.radio_opcionesEjecuciones
    btn_eliminarRepeticion = pl.button_eliminarRepeticion

    # Tercera pagina
    lbl_numero = pl.label_numero
    txt_numero = pl.span_numero
    lbl_fechaEjecucion = pl.label_fechaEjecucion
    txt_fechaEjecucion = pl.span_fechaEjecucion
    lbl_estado = pl.label_estado
    txt_estado = pl.span_estado
    btn_confirmar = pl.button_confirmar

