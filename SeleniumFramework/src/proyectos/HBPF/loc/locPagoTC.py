from SeleniumFramework.src.proyectos.HBPF.pageLoc.PagoTC import PagoTC


class locPagoTC(object):

    tituloPagoTC = PagoTC.title_h1_PagoTC
    tarjeta = PagoTC.list_tc_option
    anularPagoTC = PagoTC.btn_anularPago
    saldopesos = PagoTC.button_saldopesos
    saldodolares = PagoTC.button_saldodolares
    cuentaDebito = PagoTC.list_ctaDebito
    opt_OtroImporte = PagoTC.option_OtroImporte
    input_OtroImporte = PagoTC.input_OtroImporte
    cmdContinuar = PagoTC.cmdContinuar
    cmdConfirmar = PagoTC.cmdConfirmar
    spanResultado = PagoTC.spanClass_resultado
    cmdDescargar = PagoTC.cmdButton_descargar
    tblSinTC = PagoTC.tblTable_CuentaSinTarjetaCredito
    tblSaldoMayor = PagoTC.tbl_saldoMayor
    cerrarTblSaldoMayor = PagoTC.button_CerrarSaldoMayor
    tblAutoDebActivo = PagoTC.tbl_debitoAutomaticoActivo
    cerrarTbl = PagoTC.cmdButton_CerrarTable
    errorPanel = PagoTC.pnlErrorPanel
    diverrorCollection = PagoTC.div_error
    opt_ImporteMinimo = PagoTC.option_ImporteMinimo
    opt_importeTotalPesos = PagoTC.radio_importeTotalPesos
    opt_importeTotalDolar = PagoTC.radio_importeTotalDolar
    cmdNuevoPago = PagoTC.cmdButton_NuevoPago
    cmdInicio = PagoTC.cmdButton_continuar_Inicio
    img_ticket = PagoTC.img_ticket
    msg_exitoSinTkt = PagoTC.lblExitoSinTkt
    checkbox_mail = PagoTC.input_enviarMail
    txt_pesosHastaFecha = PagoTC.txt_PagoPesosHastaFecha
    txt_dolaresHastaFecha = PagoTC.txt_PagoDolaresHastaFecha
    button_cerrar = PagoTC.button_cerrar
    btn_continuar = PagoTC.btn_continuar
