import allure
#from SeleniumFramework.constants.spanish_messages import MsgAllure


class allure_driver(object):
    def attach_element(self, image, description):
        """
        Method to attach a image in allure
        :param image: Image. Image to attach
        :param description: String. Description of attached image
        """
        allure.attach(image, description,
                      attachment_type=allure.attachment_type.PNG)
        self.log.info(MsgAllure.MSG_ATTACH_IMAGE.format(description))

    def step(self, description):
        """
        Method to obtain allure step.
        The sentence to use is: with self.step(step_number, description):
        :param number: Integer. Number of step
        :param description: String. Desciption of step
        """
        step = allure.step(MsgAllure.MSG_STEP.format(self.paso, description))
        self.paso += 1
        return step

    def simple_step(self, msg):
        """
        Method to insert a step in allure
        :param msg: String. Text of step
        """
        return allure.step(msg)
