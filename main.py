from sort import Priority
from Input import Input
import csv
from customtkinter import *

# app = CTk()
# app.geometry("1280x720")
# app.title("To Do List")
# app.iconbitmap("icon.ico")

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
            
            
# object_plan = Plan()
# object_plan.input()
# button = CTkButton(master=app, text="start", corner_radius=45, width=200, height=60, font=()"Arial", 20), fg_color="#0726D4", hover_color="#049EFD"
#                    , border_color="#CEA226", border_width=1.5)
# button.place(relx = 0.5 , rely = 0.5, anchor = "center")
# app.mainloop()
