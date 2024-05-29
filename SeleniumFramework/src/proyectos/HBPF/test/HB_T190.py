import unittest
import allure
import traceback
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin
from SeleniumFramework.src.proyectos.HBPF.st.stCambioClave import stCambioClave
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.common_functions import get_user 
from SeleniumFramework.constants.excel_constants import USERS_HB


@allure.feature(u'Login')
@allure.story(u'Login con los usuarios habilitados')
@allure.testcase( u"HB-T190 - Login con diferentes usuarios")
@allure.title(u'HB-T90 - Login con diferentes usuarios')
@allure.severity(allure.severity_level.NORMAL)
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T106")
@allure.description(u'Verificar que se encuentren habilitadas las credenciales correspondientes a cada usuario.')

class HB_T190 (unittest.TestCase, stLogin, stCambioClave):
    def setUp(self):
        inicio_test(self)

    def test_CDPF_T393(self): 

            try:
                for users in USERS_HB:                        
                    self.usuario = get_user(users)
                    self.getDatos()
                    self.login()
                    self.deslogueo()
                    self.close_browser()
                    
                    if users == USERS_HB[-1]: 
                        self.login
                        self.finalizo = True
                        self.tearDown()
                    
                    self.openHB()
                    
            except Exception:
                self.error = traceback.format_exc()
        
    def getDatos(self):
            self.user = self.usuario[0]
            self.clave = self.usuario[1]
            
    def tearDown(self):
        finalizar_test(self)


if __name__ == "__main__":
    unittest.main()
