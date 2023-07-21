import os
from daily_reader import DailyReader


MONTH_TO_INT = {"settembre": 9, "ottobre": 10, "novembre": 11, "dicembre": 12, "gennaio": 1,
                "febbraio": 2, "marzo": 3, "aprile": 4, "maggio": 5, "giugno": 6 }

def MonthReader(genericData,  monthlyDataPath):
    genericData.month = TakeMonthFromDir(monthlyDataPath)
    genericData.year = TakeYearFromDir(monthlyDataPath)

    for dailyFile in os.listdir(monthlyDataPath):
        if dailyFile == ".DS_Store":
            continue

        dailyFilePath = monthlyDataPath + "/" + dailyFile
        genericData.day = TakeDayFromDir(dailyFilePath)

        DailyReader(dailyFilePath, genericData)
    

def TakeMonthFromDir(dir):
    # we take only the name of the math than we would like to analyze 
    # split the contontent every " ", and than transform the name in lowerCase
    # it's correct because the name of the montly dir is "month year"
    monthName = dir.split("/")[-1].split()[0].strip().lower()
    return MONTH_TO_INT[monthName]

def TakeYearFromDir(dir):
    # we can assume than the name of the montly dir is "month year"
    year = dir.split("/")[-1].split()[1].strip()
    return int(year)

def TakeDayFromDir(dir):
    # we have to delete the file ext "xlsx" in our case
    # and the structure of the date usually is day"div"month"div"year%2000
    name = dir.split("/")[-1].replace(".xlsx", "").replace("-", " ").replace("_", " ")

    #structure = name- dayname date or name- date dayname
    informations = name.split()
    for info in informations:
        if info.isdigit():
            # from the structure of the date we can assume than the day is in the first position
            return int(info)
