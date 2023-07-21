import pandas as pd
from class_reader import ClassReader
from generic_data import GenericData

def DailyReader(dailyFilePath: str, genericData: GenericData) -> None:

    workBook = pd.ExcelFile(dailyFilePath)
    lisOfSheets: list = workBook.sheet_names
    
    for className in lisOfSheets:
        if className.lower().strip().count("riepilogo") == 1:
            continue
        ClassReader(dailyFilePath, className, genericData)
