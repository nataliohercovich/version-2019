from Class_Coffee import Coffee
from Class_Coffee_Premium import Coffee_Premium

def coffee_machine(currency):
    total=int(input('Coffee:\n1:common coffee\n2:premium coffee\n'))
    if total == 1:
        coffee=Coffee(currency)
        coffee.water_quantity()
        coffee.coffee_quantity()
        coffee.sugar_quantity()
        return 'ok'
    elif total == 2:
        coffee=Coffee_Premium(currency)
        coffee.water_quantity()
        coffee.coffee_quantity()
        coffee.sugar_quantity()
        coffee.milk_quantity()
        return 'ok'
    else:
        return 'wrong option'