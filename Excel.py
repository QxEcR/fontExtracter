import openpyxl
from pathlib import Path

class Excel:
    def __init__(self, filename):
        #opening the xlsx file
        self.filename = filename
        xlsx_path = Path(self.filename)
        self.xlsx_file = openpyxl.load_workbook(xlsx_path) 

        #getting the sheets
        self.inputSheet = self.xlsx_file['Input']
        self.outputSheet = self.xlsx_file['Output']
    
    def getInputs(self):
        list = []
        #iterating through the input sheet to get all the urls
        for row in self.inputSheet.iter_rows(max_row=self.inputSheet.max_row):
            for cell in row:
                if cell.value.startswith("http"):
                    list.append(cell.value)
        return list

    def writeToExcel(self, isCSS, list):
        pass