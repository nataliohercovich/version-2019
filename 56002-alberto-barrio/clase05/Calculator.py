class Calculator(object):

    def __init__(self):
        self.operator=None
        self.input_1= 0
        self.input_2= 0
    def input_number(self,character):
        try:
            number=int(character)
            if self.operator:
                self.input_2=number
            else:
                self.input_1=self.input_1*10+number
        except:
            if character=='=':
                if self.operator=='+':
                    self.input_1+=self.input_2

                self.operator=None
                self.input_2=0
            else:
                self.operator=character
    def display(self):
        return str(self.input_1)
   