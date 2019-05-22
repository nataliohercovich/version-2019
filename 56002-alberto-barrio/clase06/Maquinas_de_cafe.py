class Maquina_de_Cafe_Basica(object):
    def __init__(self):
        self.cafe=1000
        self.water=5000
        self.is_prepare = True
        
    def coins(self,coin):
        if int(coin) == 1:
            return "Start"
            
        else:
            return "No coin incerted"
    
    
    
