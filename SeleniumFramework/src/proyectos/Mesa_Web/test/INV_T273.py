# -*- coding: utf-8 -*-
import unittest
import allure
import traceback
import getpass
from SeleniumFramework.src.proyectos.Mesa_Web.pageLoc.pl_MesaWebPerfil import pl_MesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebInicio import stMesaWebInicio
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebPerfil import stMesaWebPerfil
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebPrecios import stMesaWebPrecios
from SeleniumFramework.src.proyectos.Mesa_Web.st.stMesaWebBandeja import stMesaWebBandeja
from SeleniumFramework.src.proyectos.Mesa_Web.st import inicioMesaWeb
from SeleniumFramework.src.proyectos.Mesa_Web.st import fin
from SeleniumFramework.src.proyectos.Mesa_Web.settings import get_user_mesaWeb_homo
from SeleniumFramework.constants.excel_constants import NROCLIENTE, MSJ_ESPERADO, CUENTA, INSTRUMENTO, CANTIDAD

    

             

@allure.feature(u'Operaciones')
@allure.story(u'Carga de precios Cierre')
@allure.testcase(u"Mesa_Web - INV-273 - Carga de precios Cierre")
@allure.title(u'Mesa_Web - INV-273 - Carga de precios Cierre')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    u"""
1.-Ir a https://waslibhomo.sis.ad.bia.itau/tradingNS/pages/login.xhtml</br>                              
2.-Poner Usuario y Contraseña de Red y luego presionar ingresar </br>                               
3.-Presionar en la sección perfil sobre el operador asignado </br>                                 
4.-Elegir perfil BAckOfficeConf y luego presionar "Cambiar Perfil"(de ser perfil default, presionar Cancelar)</br>                           
5.-Dentro del menú de "Precios" ir a la opción "Precios Cierre" y realizar click en el submenú "Administrar Precios Cierre" </br>                               
6.-Realizar exportación de archivo TXT y guardar en un carpeta para luego ser importado</br>                               
7.-Cargar Archivo TXT del paso 6 con el "Boton" examinar</br>                                
8.-Una vez cargado el archivo presionar importar</br>                                
    9.-Una vez importado el archivo presionar "actualizar precios"</br>                                
10.-Presionar "Aceptar" </br>                               
11.-Luego de unos segundos debe aparecer un cartel verde con la leyenda "Precios Cierre Precios actualizados Satifactoriamente"</br>                             
 </br>
    """
)
class INV_T273(unittest.TestCase, stMesaWebInicio, stMesaWebPerfil,stMesaWebPrecios, stMesaWebBandeja):
    def setUp(self):
        inicioMesaWeb(self)
        
    def test_INV_T273(self):
        try:
            self.usuario = get_user_mesaWeb_homo(self._testMethodName)
            self.getDatos()
            self.login()
            self.perfil(pl_MesaWebPerfil.operador_backOffice)
            self.seleccionar_precios()
            self.seleccionar_precios_cierre()
            self.seleccionar_admin_precios_cierre()
            self.seleccionar_btn_exportar()
            self.seleccionar_btn_slc_archivo()
            self.seleccionar_importar_archivo()
            self.seleccionar_btn_actualizar_precios()
            self.seleccionar_btn_aceptar()
            self.seleccionar_visualizar_msj_actualizados_satisfactoriamente()
            user = getpass.getuser()
            self.eliminar_archivo_txt(r'C:\Users\{}\Downloads\Precios.txt'.format(user.lower()))  
            self.cerrarSesion()
            self.finalizo = True
        except Exception:
            self.cerrarSesion()
            self.error = traceback.format_exc()

    def tearDown(self):
        fin(self)

    def getDatos(self):
        
        self.nrocliente = self.usuario.get(NROCLIENTE)
        self.mensaje_esperado = self.usuario.get(MSJ_ESPERADO)
        self.cuenta = self.usuario.get(CUENTA)
        self.instrumento = self.usuario.get(INSTRUMENTO) 
        self.cantidad = self.usuario.get(CANTIDAD)
        self.orden = ""
        

if __name__ == "__main__":
    unittest.main()
