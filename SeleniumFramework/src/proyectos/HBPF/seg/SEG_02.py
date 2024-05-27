# -*- coding: utf-8 -*-
import unittest
import allure
import requests, random, string
import traceback
from SeleniumFramework import browser
from SeleniumFramework.src.proyectos.HBPF.st import inicio_test, finalizar_test
from SeleniumFramework.src.proyectos.HBPF.st.stLogin import stLogin

@allure.feature(u'Cambio de clave')
@allure.story(u'Realizar cambio de clave')
@allure.testcase( u"HB-T106 -0032- Cambio de clave - clave actual incorrecta")
@allure.title(u'HB-T106 -0032- Cambio de clave - clave actual incorrecta')
@allure.severity(allure.severity_level.NORMAL)
@allure.link(u"https://jira.sis.ad.bia.itau/secure/Tests.jspa#/testCase/HB-T106")
@allure.description(
    u"""
    """
)
class SEG_01 (unittest.TestCase, stLogin):
    def setUp(self):
        self.openChrome_seg(url="https://github.com/login")

    def test_SEG_01(self):
        try:
            self.getDatos(length_user=8)
            self.seg_login()

        except Exception:
            self.error = traceback.format_exc()

    def getDatos(self, length_user):
        self.username = ''.join(random.choices(string.ascii_lowercase, k=length_user))
        self.claveRandom = random.randint(1111111111, 9999999999)

    def tearDown(self):
        pass



if __name__ == "__main__":
    unittest.main()
