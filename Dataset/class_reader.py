from math import nan
import pandas as pd

from generic_data import GenericData

def ClassReader(dailyFilePath: str, className: str, genericData: GenericData) -> None:
    dataClass: pd.DataFrame = pd.read_excel(dailyFilePath, sheet_name= className)
    keysAndNames: tuple[dict, list] = ExtractKeysAndNames(dataClass)
    keys: dict = keysAndNames[0]
    names: list = keysAndNames[1]

    # we iterate the first colums
    for index in range(len(names)):
        name = names[index]

        # nan value are skipped
        if type(name) != str:
            continue
        
        id: int = genericData.get_ID(name)

        # start to create all the information of out csv file
        out: str = str(id) + "," + str(genericData.day) + "-" + str(genericData.month) + "-" + str(genericData.year) + "," + className + ","
        
        for product in genericData.PRODUCTS:
            # verify if the key of the colums is part of the products
            if not product in keys:
                out += "0,"
                continue  
            key: str = keys[product]
            
            # to check if indx or indx+1
            val = dataClass[key][index]
            val = val if type(val) != float and len(str(val)) >= 2 else "Nan"
            out += "0," if val == "Nan" or not str(val)[1:].isdigit() else str(val)[1:] + ","

        out: str = out.strip(",") + "\n"
        genericData.dataset.write(out)
    return


def ExtractKeysAndNames(dataClass: pd.DataFrame) -> tuple[dict, list]:
    keys: dict = {}
    names: list = []
    count: int = 0

    # extrackting the keys of the excel file
    for key in dataClass:
        keys[key.lower()] = key

        # we like to extrack all the names while total apper
        if count == 0:
            for name in dataClass[key]:

                # total represent the total spent of the class
                if str(name).lower().strip() == "totale":
                    break
                names.append(name)
        count = -1
    
    return keys, names