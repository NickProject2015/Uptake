from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from Utilities.custom_logger import customLogger as lg
from selenium.webdriver import ActionChains
from Utilities.Constants import Constants

import time
import logging


class SeleniumDriver():
    # Create object instance for logging
    log = lg.log_utility(logging.DEBUG)

    # Set init value for driver and Constants
    def __init__(self, driver):
        self.driver = driver
        self.constants = Constants()
        self.UIvalue = None

    # Method for browser navigation
    def navigate(self, datavalue):
        try:
            self.driver.get(datavalue)
            return True
        except:
            self.log.error("Navigation failed")
            return False

    # Get web element based on the locator value
    def getelement(self, locator):
        try:
            element = self.driver.find_element(By.XPATH, locator)
        except:
            self.log.info("Element not found")

        return element

    # Method to find web element occurance
    def findelement(self, locator):
        try:

            elementtofind = None
            elementtofind = self.driver.find_elements(By.XPATH, locator)
            # If element occurance found then return True
            if len(elementtofind) > 0:
                return True
            else:
                return False
                self.log.info("Element not found")
        except:
            self.log.info("Some error occured, element not found")
            return False

    # Method to wait for an element
    def waitforelement(self, locator):
        try:
            elementowait = None
            nwait = None
            # wait object with certain seconds and ignoring conditions
            nwait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                  ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                      ElementNotSelectableException])
            # Wait for an element until the expected conditions are met
            elementowait = nwait.until(EC.presence_of_element_located((By.XPATH, locator)))
            return elementowait

        except:
            self.log.info("Element was not found, wait limit exceeded")
            return False

    # Method to perform element click
    def elementClick(self, locator):
        try:
            self.getelement(locator).click()
            return True
        except:
            self.log.info("Element not clicked")
            return False

    # Method to capture screenshot
    def capturescreen(self):

        try:
            filename = "Scrnshot" + "_" + str(round(time.time() * 1000)) + ".png"
            folder_location = self.constants.Path_Snapshot
            destination = folder_location + filename
            self.driver.save_screenshot(destination)
            return True
        except NotADirectoryError:
            self.log.info("Capture screenshot failed")
            return False

    # Method to get page title
    def getTitle(self):
        return self.driver.title

    # Method to wait
    def wait(self, datavalue):
        try:
            nseconds = int(float(datavalue))
            time.sleep(nseconds)
            return True
        except:
            self.log.error("Wait for failed")
            return False

    # Method to verify Text, enabled, selected, displayed, exists, title
    def verify(self, property, value, locator):
        try:
            if property == "text":
                UI_Text = None
                UI_Text = self.driver.find_element(By.XPATH, locator).text
                if str(UI_Text) == str(value):
                    return True
                else:
                    return False
            elif property == "selected":
                select_flag = None
                select_flag = self.driver.find_element(By.XPATH, locator).is_selected()
                if str(select_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "displayed":
                display_flag = None
                display_flag = self.driver.find_element(By.XPATH, locator).is_displayed()
                if str(display_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "exists":
                exist_flag = None
                exist_flag = self.findelement(locator)
                if str(exist_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "title":
                title = str(self.getTitle())
                if title == value:
                    return True
                else:
                    return False

        except:
            self.log.error("Verify failed")
            return False

    # Method to move cursor to an element
    def moveto(self, locator):
        try:
            element = None
            element = self.driver.find_element(By.XPATH, locator)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            return True
        except:
            self.log.error("Cursor Move to element failed")
            return False
