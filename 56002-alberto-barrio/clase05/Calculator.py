class Calculator(object):

    def __init__(self):
        self.operator=None
        self.operator_before=None
        self.input_1= 0
        self.input_2= 0
    def input_number(self,character):
        try:
            
            number=int(character)
            if self.operator:
                self.input_2=self.input_2*10+number
            else:
                self.input_1=self.input_1*10+number

        except:
            
            operator_before=False
            
            if self.operator!=None:
                operator_before=True
            if character=='=' or operator_before==True:
                if self.operator=='+':
                    self.input_1+=self.input_2

                self.operator=None
                self.input_2=0
                if operator_before==True:
                    self.operator=character
            else:
                self.operator=character

    def display(self):
        return str(self.input_1)
   