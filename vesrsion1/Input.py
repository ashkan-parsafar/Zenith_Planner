class Input:
    def __init__(self,all_works):
        self.all_works = all_works
        self.coun = True # shorts of countinue

    def get_input(self):
        while self.coun:
            input_work = input('Enter your work you want do it to day :')  # a b c d

            self.all_works.append(input_work)
            return self.countinue()

    def countinue(self):
        desire_to_continue = input('Do you want to countinue?(yes/no)')

        if desire_to_continue == 'yes':
            print('Ok continiue!')
            return self.get_input()
        elif desire_to_continue == 'no':
            print('This step is end')
            self.coun = False
            return True
        else:
            print('Enter a valid value')
            return self.countinue()
