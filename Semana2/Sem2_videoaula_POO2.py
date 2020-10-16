import random
# usando herança
class Mylist(list):
    def choice(self):
        return random.choice(self)
        
