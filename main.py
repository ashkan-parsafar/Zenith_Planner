from sort import Sort
from Input import Input

class Plan :

    def __init__(self):
    
            
        self.all_works = [
    
        ]
        object_input = Input(self.all_works)
    def input (self):
        input_status = object_input.get_input()
        if input_status :
            self.sort()
        else :
            self.input()
            
    def sort (self):
        object_sort = Input(self.all_works)
        sort_status = object_sort.get_input()
        if input_status :
            self.sort()
        else :
            self.input()