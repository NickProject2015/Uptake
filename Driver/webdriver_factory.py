from selenium import webdriver
import os
from Utilities.Constants import Constants


class GetWebdriverInstance():
    def __init__(self, browser):
        self.browser = browser
        self.constants = Constants()

    # Method to invoke browser based on the input from the command prompt
    def getbrowserInstance(self):
        if (self.browser == 'IE'):

            driver_location = self.constants.Path_IE_driver
            os.environ["webdriver.IE.driver"] = driver_location
            driver = webdriver.Ie(executable_path=driver_location)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()

        elif (self.browser == 'Chrome'):

            driverLocation = self.constants.Path_Chrome_driver
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(executable_path=driverLocation)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()

        elif (self.browser == 'Firefox'):
            driverLocation = self.constants.Path_Firefox_driver
            os.environ["webdriver.firefox.driver"] = driverLocation
            driver = webdriver.Firefox(executable_path=driverLocation)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()

        return driver
