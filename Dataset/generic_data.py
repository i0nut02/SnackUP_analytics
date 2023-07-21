"""
contain : 
    - the products
    - the ID of the students
    - date information 
    - dataset file
"""
from io import TextIOWrapper

class GenericData():
    # they're all the products than offer our supplier
    PRODUCTS: list[str] = [
                    'panino con fesa di tacchino', 'panino prosciutto cotto', 'pizza patate e cotto', 
                    'panino cotoletta con insalata e pomodoro', 'panino mortadella', 'panino salame', 
                    'ripiena cotto e mozzarella', 'supplì', 'pizza diavola', 'pizza bianca', 'margherita', 
                    'pizza con wurstel', 'hamburger con insalata e pomodoro', 'pizza patate', 'pizza rossa', 
                    'pizza con nutella', 'panino prosciutto crudo', 'pizza bianca con mortadella'
                ]

    def __init__(self, datasetFile: TextIOWrapper) -> None:
        self.dataset: TextIOWrapper = datasetFile

        self.nextID: int = 0
        self.nameToID: dict[str, int] = {}
        
        self.day: int = -1
        self.month: int = -1
        self.year: int = -1
    
    def add_ID(self, name: str) -> None:
        self.nameToID[name] = self.nextID
        self.nextID += 1
    
    def get_ID(self, name: str) -> int:
        if not name in self.nameToID:
            self.add_ID(name)
        
        return self.nameToID[name]
