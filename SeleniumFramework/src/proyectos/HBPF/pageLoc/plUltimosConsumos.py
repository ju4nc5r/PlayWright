# -*- coding: utf-8 -*-
class plUltimosConsumos():
    label_SinConsumos = (
        "//*[@id='richTextSinConsumos']/p")
    label_Titulo_UltimosConsumos = (
        "//*[@id='constantLabel0' and contains(.,'consumos')]")
    selectField_Tarjetas =(
        "//*[@id='selectField0']")
    cmdButton_Volver = (
        "//*[@id='actionButton0' and contains(.,'Volver')]")
    label_TotalDeConsumos = (
        "//*[@id='constantLabel10' and contains(.,'CONSUMOS')]")
    table_ListaConsumos_1 = (
        "//*[@id='section0_repeat1_collectionTable0_Establecimiento / Cuota' and contains(.,'{}')]")
    table_ListaConsumos_2 = (
        "//*[@id='section0_repeat1_collectionTable0_Establecimiento / Cuota']")
    label_Cartel_DetalleConsumo = (
        "//*[@id='constantLabel0' and contains(.,'Detalle')]")
    cmdButton_Cerrar_Cartel_DetalleConsumo = (
        "//*[@id='actionButton0' and contains(.,'Cerrar')]")