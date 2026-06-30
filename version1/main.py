from sort import Priority
from Input import Input
import csv

class Plan :

    def __init__(self):
    
            
        self.all_works = []
        self.priority = []
        
    def input (self):
        object_input = Input(self.all_works)
        input_status = object_input.get_input()
        if input_status :
            self.sort()
        else :
            self.input()
            
    def sort (self):
        object_sort = Priority(self.all_works,self.priority)
        sort_status = object_sort.priority_works()
        if sort_status :
            with open("to do list.csv", "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)

                for i, item in enumerate(self.priority):
                    writer.writerow([i+1, item])
        else :
            self.input()
            
            
object_plan = Plan()
object_plan.input()
