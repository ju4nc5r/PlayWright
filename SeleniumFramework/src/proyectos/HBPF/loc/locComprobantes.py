from SeleniumFramework.src.proyectos.HBPF.pageLoc.plComprobantes import plComprobantes as comp


class locComprobantes():
    titulo = comp.titulo_esperado
    boton_itau = comp.button_itau
    boton_visa = comp.button_visa
    txt_operaciones = comp.label_operaciones
    sel_operaciones = comp.select_operaciones
    txt_fecha_desde = comp.label_fecha_desde
    inp_fecha_desde = comp.input_fecha_desde
    txt_fecha_hasta = comp.label_fecha_hasta
    inp_fecha_hasta = comp.input_fecha_hasta
    txt_canal = comp.label_canal
    sel_canal = comp.select_canal
    txt_num_op = comp.label_num_operacion
    inp_num_op = comp.input_num_operacion
    boton_volver = comp.button_volver
    boton_buscar = comp.button_buscar
    tbl_comprobantes = comp.table_resultados
    tbl_sin_comprobantes = comp.table_sin_resultados
    icono_primer_pdf = comp.img_primer_pdf
    image_ticket = comp.img_ticket
    div_error = comp.div_error
