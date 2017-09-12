from Utilities.Test_Status import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from Utilities.Constants import Constants
from Utilities.excelread import excelUtil
from Utilities.module_mapping import driver_mapping
from Utilities.custom_logger import customLogger as lg
import logging


@pytest.mark.usefixtures("invoke_browser")
@ddt
class mainTests(unittest.TestCase):
    log = lg.log_utility(logging.INFO)

    # Initialize object instances for test case result, constants, exceldata, method mapping
    @pytest.fixture(autouse=True)
    def initialSetup(self, invoke_browser):
        self.ts = TestStatus(self.driver)
        self.constants = Constants()
        self.excel = excelUtil()
        self.drivermethod = driver_mapping(self.driver)

    # This is the main method that kicks in when execution starts (This in turn calls all the keywords)
    @pytest.mark.run(order=1)
    def test_main(self):

        self.excel.setExcelFile(self.constants.Path_TestData)
        self.execute_testCases()

    # Reads keywords, objects and other attributes to execute methods
    def execute_testCases(self):
        # Get row count in test suite worksheet
        ntotalTestCases = self.excel.getRowCount(self.constants.Sheet_TestCases)

        # loop through testsuite worksheet and get test ids (Row id 1 thru last row)
        for ntestCase in range(1, (ntotalTestCases - 1)):
            # Get test case id from test suite worksheet
            nTestCaseID = self.excel.getCellData(ntestCase, self.constants.Col_TestCaseID,
                                                 self.constants.Sheet_TestCases)
            # Get test case description
            nTestCaseDescrption = self.excel.getCellData(ntestCase, self.constants.Col_TestCaseDescription,
                                                         self.constants.Sheet_TestCases)
            # Get runmode from testsuite worksheet
            sRunMode = self.excel.getCellData(ntestCase, self.constants.Col_RunMode, self.constants.Sheet_TestCases)
            # If runmode is Yes then get first and last position of testcase id in TestSteps worksheet
            if sRunMode == 'Yes':
                self.log.info(
                    "*****************************************************************************************************")
                self.log.info("Test case: " + str(nTestCaseID) + ":" + str(nTestCaseDescrption))
                self.log.info(
                    "*****************************************************************************************************")
                # Start id of test step based on the tc id
                nStartStep = self.excel.getRowContains(nTestCaseID, self.constants.Col_TestCaseID,
                                                       self.constants.Sheet_TestSteps)
                # Last id of test step based on the tc id
                nEndStep = self.excel.getTestStepsCount(self.constants.Sheet_TestSteps, nTestCaseID, nStartStep)
                # Traverse through test steps
                for step in range(nStartStep, nEndStep):
                    # Get test step id
                    ntestStepId = self.excel.getCellData(step, self.constants.Col_TestScenarioID,
                                                         self.constants.Sheet_TestSteps)
                    # Get step description
                    nstepDescription = self.excel.getCellData(step, self.constants.Col_TestDescription,
                                                              self.constants.Sheet_TestSteps)
                    # Get object name
                    nObject = self.excel.getCellData(step, self.constants.Col_PageObject,
                                                     self.constants.Sheet_TestSteps)
                    # Get object xpath value
                    nObject_Value = self.excel.getObjectValue(self.constants.Sheet_Objectvalue, nObject)
                    # Get action keyword
                    nActionKeyword = self.excel.getCellData(step, self.constants.Col_ActionKeyword,
                                                            self.constants.Sheet_TestSteps)
                    # Get property value
                    nProperty = self.excel.getCellData(step, self.constants.Col_ObjProperty,
                                                       self.constants.Sheet_TestSteps)
                    # Get data value
                    if nActionKeyword == "dragto":
                        tempdata = self.excel.getCellData(step, self.constants.Col_Datavalue,
                                                          self.constants.Sheet_TestSteps)
                        ndataValue = self.excel.getObjectValue(self.constants.Sheet_Objectvalue, tempdata)
                    else:
                        ndataValue = self.excel.getCellData(step, self.constants.Col_Datavalue,
                                                            self.constants.Sheet_TestSteps)
                    # store step execution status (Pass/Fail)
                    stepresult = self.drivermethod.execute_keyword(nActionKeyword, nProperty, ndataValue, nObject_Value)
                    self.ts.mark(stepresult, nstepDescription)
                # Test case status (Pass or Fail)
                self.ts.markFinal(nTestCaseID, stepresult, nTestCaseDescrption)
