# -*- coding: utf-8 -*-
'''
Created on 2024-02-28

@author: FO433151
'''

import unittest, time
from itauQAAutomationHelper import TN5250Helper
from itauQAAutomationHelper import TN5250Event

class Test(unittest.TestCase):

    def setUp(self):
        self.consoleDriver = TN5250Helper()
        self.verificationErrors = []

    def tearDown(self):
        self.consoleDriver.quit()
        self.assertEqual([], self.verificationErrors)

    def test(self):
        self.consoleDriver.sendKeys('CAPACIT') 
        self.consoleDriver.sendEvent(TN5250Event.TAB)
        self.consoleDriver.sendKeys('CAPACIT') 
        self.consoleDriver.sendEventAndWaitScreenChange(TN5250Event.ENTER)
        self.consoleDriver.sendEventAndWaitScreenChange(TN5250Event.ENTER)
        self.consoleDriver.sendKeys('3') 
        self.consoleDriver.sendEventAndWaitScreenChange(TN5250Event.ENTER)
        self.consoleDriver.sendEventAndWaitScreenChange(TN5250Event.ENTER)

if __name__ == "__main__":
        unittest.main()