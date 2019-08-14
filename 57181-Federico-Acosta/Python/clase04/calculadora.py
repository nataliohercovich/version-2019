class Calculadora():
    def __init__(self):
        self.op1 = 0
        self.op = None
        self.op2 = 0
    def ingresar(self, character):
        try:
            num = int(character)
            if self.op == None:
                self.op1 = self.op1*10+num
                return
            self.op2 = self.op2*10+num
        except:
            op_anterior = False
            if self.op != None:
                op_anterior = True
            if character == "=" or op_anterior == True:
                if self.op == "+":
                    self.op1 +=self.op2
                if self.op == "-":
                    self.op1 -=self.op2
                if self.op == "*":
                    self.op1 = self.op1 * self.op2
                if self.op == "/":
                    self.op1 = self.op1 / self.op2

                self.op = None
                self.op2 = 0
                if op_anterior == True:
                    self.op = character
            else:
                self.op = character
    def display(self):
        return str(self.op1)