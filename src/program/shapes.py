from random import randint
from random import choice

class Shapes():
    def __init__(self):
        self.width=0
        self.height=0
        self.color=0
        self.start_x=0

    def new_shape(self):
        shape=randint(1,3)
        if shape==1:
            self.width=50
            self.height=100
        elif shape==2:
            self.width=100
            self.height=50
        elif shape==3:
            self.width=100
            self.height=100
        
    def start_position(self):
        start=[50,100,150,200]
        self.start=choice(start)
        

 


