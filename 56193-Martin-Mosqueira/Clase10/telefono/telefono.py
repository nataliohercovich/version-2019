
class Telefono():
    def __init__(self):
        self.cont=0
        self.credito=0

    def dial(self,digitos):
        if len(digitos) == 3 and (digitos[0] == '9' or digitos[0] == '8'):
            return True

        if len(digitos) == 7:
            if self.credito > 10:
                return True
            else:
                return False

        if digitos[0] == '0' and digitos[1] == '0':
            if self.credito > 100:
                return True
            else:
                return False

    def agregar_credito(self, digitos):
        self.credito=self.credito-10
        self.credito += int(digitos)

