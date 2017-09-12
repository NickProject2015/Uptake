from Driver.selenium_driver import SeleniumDriver

class driver_mapping(SeleniumDriver):

    def __init__(self,driver):
        super(driver_mapping, self).__init__(driver)
        self.driver = driver

    # Execute the keyword functions and return the status
    def execute_keyword(self,keyword,attribute,value,objectname):
        if keyword == 'navigate':
            result = None
            result = self.navigate(value)
            return result

        elif keyword == "click":
            result = None
            result = self.elementClick(objectname)
            return result

        elif keyword == "wait":
            result = None
            result = self.wait(value)
            return result

        elif keyword == "verify":
            result = None
            result = self.verify(attribute,value,objectname)
            return result

        elif keyword == "moveto":
            result = None
            result = self.moveto(objectname)
            return result

        elif keyword == "waitFor":
            element_wait = self.waitforelement(objectname)
            if element_wait:
                return True
            elif element_wait is None:
                return False
            else:
                return False

        elif keyword == 'snapshot':
            result = None
            result = self.capturescreen()
            return result

        elif keyword == "waitfor":
            result=None
            result=self.waitforelement(objectname)
            return result

        else:
            self.log.info("Bad keyword or not found. All keywords should be in lowercase!!")
            return False


