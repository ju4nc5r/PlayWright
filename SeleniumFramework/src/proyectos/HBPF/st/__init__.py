def inicio_test(self):
    self.finalizo = False
    self.openHB()


def finalizar_test(self):
    if self.finalizo:
        self.deslogueo()
        self.close_browser()
        self.ok_test()
    else:
        self.fail_test(self.error)