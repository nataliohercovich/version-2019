class Coffee():
    def __init__(self,currency):
        self.water=1000
        self.coffee=50
        self.sugar=600
        self.total=0
        self.currency=currency


    def water_quantity(self):
        self.water=self.water-250*self.currency
        if self.water <= 0:
            return 'add more water'
        else:
            return str(self.water)+'ml'

    def coffee_quantity(self):
        self.coffee=self.coffee-10*self.currency
        if self.coffee <= 0:
            return 'add more coffee'
        else:
            return str(self.coffee)+'g'

    def sugar_quantity(self):
        for line in range(self.currency):
            self.total=str(input('Sugar coffee'+str(line+1)+': s/n'))
            if self.total == 's':
                self.sugar=self.sugar-8
        if self.sugar <= 0:
            return 'add more sugar'
        else:
            return str(self.sugar)+'g'

