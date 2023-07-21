from io import TextIOWrapper
import os
from month_reader import MonthReader
from generic_data import GenericData
'''
- create the dataset "csv file"
- analyze all the year in "Data" folder
    - read the moths
        - read the daily data
            - take an ID to all the students and remember it
            - save it in the dataset
'''

# dataset structure= ID: int, date: str, class : str, [all the possible snacks] : int
def Main() -> None:
    dataset: TextIOWrapper = open("dataset.txt", "w+")
    dataset.write_through
    genericData = GenericData(dataset)

    # write the structure of the dataset
    genericData.dataset.write("ID,DAY,CLASS,PANINO CON FESA DI TACCHINO,PANINO PROSCIUTTO COTTO,PIZZA PATATE E COTTO,PANINO COTOLETTA CON INSALATA E POMODORO,PANINO MORTADELLA,PANINO SALAME,RIPIENA COTTO E MOZZARELLA,SUPPLÌ,PIZZA DIAVOLA,PIZZA BIANCA,MARGHERITA,PIZZA CON WURSTEL,HAMBURGER CON INSALATA E POMODORO,PIZZA PATATE,PIZZA ROSSA,PIZZA CON NUTELLA,PANINO PROSCIUTTO CRUDO,PIZZA BIANCA CON MORTADELLA\n")
    dataPath: str = "Data"

    for annualData in os.listdir(dataPath):
        annualDataPath: str = dataPath + "/" + annualData

        if annualData == ".DS_Store": #or not os.path.isdir(annualDataPath):
            continue

        for monthlyData in os.listdir(annualDataPath):
            if monthlyData == ".DS_Store":
                continue

            monthlyDataPath: str = annualDataPath + "/" + monthlyData
            MonthReader(genericData,  monthlyDataPath)
    return True

Main()