import xlrd
from Utilities.custom_logger import customLogger as lg
from Utilities.Constants import Constants
import logging


class excelUtil():
    log = lg.log_utility(logging.DEBUG)
    constants = Constants()

    # Open excel
    def setExcelFile(self, path):
        try:
            self.workbook = xlrd.open_workbook(path)
        except:
            self.log.error("Data file was not opened")

    # Get rowcount
    def getRowCount(self, sheetname):
        try:
            self.worksheet = self.workbook.sheet_by_name(sheetname)
            iNum = self.worksheet.nrows + 1
            return iNum
        except:
            self.log.error("Failed to get row count")

    # Get cell value
    def getCellData(self, RowNum, ColNum, sheetname):
        try:
            self.worksheet = self.workbook.sheet_by_name(sheetname)
            self.CellData = str(self.worksheet.cell_value(RowNum, ColNum))
            return self.CellData
        except:
            self.log.error("Failed to get cell data: " + str(RowNum) + " " + str(sheetname))

    # Search for a value and exit if found and return rowid
    def getRowContains(self, testname, ColNum, sheetname):
        RowNum = 0
        try:
            rowCount = 0
            rowCount = self.getRowCount(sheetname)
            for RowNum in range(0, rowCount):
                if self.getCellData(RowNum, ColNum, sheetname) == testname:
                    break
        except:
            self.log.error("Row contains check failed")
        return RowNum

    # Return test steps count
    def getTestStepsCount(self, sheetname, testname, stepstart):
        try:
            rowCount = 0
            rowCount = self.getRowCount(sheetname)
            for i in range(stepstart, rowCount):
                if str(testname) != str(self.getCellData(i, self.constants.Col_TestCaseID, sheetname)):
                    return i
        except:
            self.log.error("Failed to get steps count")
            return 0

    # Return object xpath value
    def getObjectValue(self, sheetname, objectname):
        try:
            rowcount = self.getRowCount(sheetname)
            for i in range(0, rowcount):
                if objectname == "":
                    break
                elif str(objectname) == str(self.getCellData(i, 0, sheetname)):
                    object_value = str(self.getCellData(i, self.constants.Col_Object_Value, sheetname))
                    return object_value
        except:
            self.log.error("Failed to get object value")
