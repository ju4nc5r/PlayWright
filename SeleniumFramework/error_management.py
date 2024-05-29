import pytest


class errors(object):
    def fail_msg(self, description):
        """
        Method to show a fail in the test. Attach an image in allure and,
        print in the log the error
        :param description: String. Description of the image.
        """
        self.capture_image(description)
        self.log.error(description)
        raise Exception(description)

    def skip_msg(self, description):
        """
        Method to skip a test. Attach an image in allure and,
        print a warning in the log.
        :param description: String. Description of the image.
        """
        self.capture_image(description)
        self.log.warning(description)
        pytest.skip(description)

    def fail_test(self, error):
        """
        Method to show a fail in the test. And write the error in the log
        """
        msg = 'Test Fail'
        self.capture_image(msg)
        msg = '{msg}\n{error}'.format(msg=msg, error=error)
        self.log.error(msg)
        pytest.fail(msg)

    def ok_test(self):
        self.log.info('Test OK')
