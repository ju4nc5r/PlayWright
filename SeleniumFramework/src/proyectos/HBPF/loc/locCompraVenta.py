from SeleniumFramework.src.proyectos.HBPF.pageLoc.CompraVenta import CompraVenta
from SeleniumFramework.src.proyectos.HBPF.pageLoc.plLogin import plLogin


class locCompraVenta():
    titulo_compraVenta = CompraVenta.tile_h1_compra_venta_monteda
    ctaDebito = CompraVenta.list_cta_debito_item
    ctaComitente = CompraVenta.list_cta_comitente
    ctaAcreditacion = CompraVenta.list_cta_acreditacion_item
    importe = CompraVenta.input_importe
    monto = CompraVenta.input_monto
    tipoMoneda = CompraVenta.list_tipoMoneda_item
    slc_tipoMoneda = CompraVenta.select_tipoMoneda_item
    cmdContinuar = CompraVenta.cmdButtonContinuar
    spanConfirmar = CompraVenta.span_top_confirmacion
    cmdConfirmar = CompraVenta.cmdButtonConfirmar
    spanResultadoor = CompraVenta.span_top_Resultado
    spanResultado = CompraVenta.span_top_Resultado
    cmdContinuar_a_Ctas = CompraVenta.cmdButtonContinuar_a_cuentas
    boton_limite_diarios = CompraVenta.btn_lim_diario
    tabla_lim_diario = CompraVenta.tbl_lim_diario
    boton_cerrar = CompraVenta.btn_cerrar
    inp_enviarMail = CompraVenta.input_enviarMail
    inp_programar = CompraVenta.input_programar
    sel_programar = CompraVenta.select_programar
    inp_fechaProgramada = CompraVenta.input_fechaProgramada
    msj_error = CompraVenta.div_error
    inp_primeraFecha = CompraVenta.input_primeraFecha
    sel_cantRepe = CompraVenta.select_cantRepeticiones
    input_acepto = CompraVenta.checkbox_acepto
    # Pagina resultado
    btn_descarga = CompraVenta.btn_descarga
    boton_nueva_transf = CompraVenta.btn_nueva_transferencia
    titulo_esperado = plLogin.titulo_inicio
    image_ticket = CompraVenta.img_ticket
    # Pagina Confirmacion
    txt_cuentaDeb = CompraVenta.lbl_cuentaDebito
    txt_cuentaAcre = CompraVenta.lbl_cuentaAcreditacion
    txt_importe = CompraVenta.lbl_importe
    btn_cancelar = CompraVenta.btn_cancelar
    btn_modificar = CompraVenta.btn_modificar
    tbl_fecha_prog = CompraVenta.tbl_RealizarTransferenciaUnica
    tbl_primeraEjecucion = CompraVenta.tbl_primeraEjecucion
    tbl_diasSemanales = CompraVenta.tbl_diasSemanales
    tbl_repeticiones = CompraVenta.tbl_repeticionesProgramadas
    btn_declaracion = CompraVenta.btn_declaracion
