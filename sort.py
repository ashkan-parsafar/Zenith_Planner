class Priority:
    def __init__(self,all_works):
        self.all_works = all_works
        self.priority = []
        for j in range(len(self.all_works)):
            self.priority.append(chr(97+j))
    
    def priority_works(self):
        for i in self.all_works:
            print(i)
            work_index = int(input(f'This is something you want to do for the umpteenth time؟(you can enter the number betwen 1 to {len(self.all_works)})'))  # a  = 3

            work_index = str(work_index - 1)  # 2
            self.priority[work_index].append(i)

        
            
