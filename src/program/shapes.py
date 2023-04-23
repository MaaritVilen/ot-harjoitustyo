from random import randint
from random import choice

class Shapes():
    def __init__(self):
        self.w=0
        self.h=0
        self.color=0
        self.start=0

    def new_shape(self):
        shape=randint(1,3)
        if shape==1:
            self.w=50
            self.h=100
        elif shape==2:
            self.w=100
            self.h=50
        elif shape==3:
            self.w=100
            self.h=100
        
    def start_position(self):
        start=[0,50,100,150,200,250,300,350,400]
        self.start=choice(start)
        

 


