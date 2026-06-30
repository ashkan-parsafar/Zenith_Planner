class Priority:
    def __init__(self, all_works, priority):
        self.all_works = all_works
        self.priority = priority
        for j in range(len(self.all_works)):
            self.priority.append(chr(97+j))
    
    def priority_works(self):
        for i in self.all_works:
            print(i)
            work_index = int(input(f'This is something you want to do for the umpteenth time؟(you can enter the number betwen 1 to {len(self.all_works)})'))  # a  = 3

            if type(work_index) != int and len(self.all_works) < work_index < 1:
                print('your value is invalid ! pleas enter a valid value')
                self.priority_works()

            work_index = work_index - 1  # 2
            self.priority[work_index] = (i)
        
        return True
