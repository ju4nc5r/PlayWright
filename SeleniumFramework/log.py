import os
from time import strftime
from SeleniumFramework.src.utils.Log import Log
from SeleniumFramework.src.utils.settings import path_evidence
from SeleniumFramework.constants.spanish_messages import MsgLog
from SeleniumFramework.constants.constants import LOG_PATH


class log(object):

    def createPath(self):
        """
        Create the path of test folder. If the folder doesn't exist, it's
        created
        """
        dia = strftime("%Y-%m-%d")  # aaaa/mm/dd format
        hora = strftime("%H%M%S")  # 24 hours format
        TestCase = self.__class__.__name__
        horaAct = hora
        self.path = os.path.join(path_evidence, dia, TestCase, horaAct, '')
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def createLog(self):
        """
        Create the log of test. The log is created in the test folder
        """
        self.createPath()
        TestCase = self.__class__.__name__
        log_path = LOG_PATH.format(self.path, TestCase)
        self.log = Log(log_path)
        self.log = self.log.get_logger()
        self.log.info(MsgLog.MSG_CREATE_LOG.format(log_path))
