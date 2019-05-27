from Class_Coffee import Coffee

class Coffee_Premium(Coffee):
    def __init__(self,currency):
        super(Coffee_Premium,self).__init__(currency)
        self.milk=1000

    def milk_quantity(self):
        for line in range(self.currency):
            self.total=str(input('Milk coffee'+str(line+1)+': s/n'))
            if self.total == 's':
                self.milk=self.milk-120
        if self.milk <= 0:
            return 'add more milk'
        else:
            return str(self.milk)+'ml'
