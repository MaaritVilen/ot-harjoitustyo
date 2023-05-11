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
            self.w=20
            self.h=100
        elif shape==2:
            self.w=100
            self.h=20
        elif shape==3:
            self.w=100
            self.h=100
        
    def start_position(self):
        start=[0,40,100,160,200,240,300,360,400]
        self.start=choice(start)
    
    def delete_row(pieces, row_to_be_deleted):
        delete_row=False
        delete_row_number=0
        for i in range(len(pieces)):
            if pieces[i][1]<=row_to_be_deleted<=pieces[i][1]+pieces[i][3]:
                new_y=pieces[i][1]+20
                new_h=pieces[i][3]-20
                pieces[i][1]=new_y
                pieces[i][3]=new_h
            
            #elif pieces[i][1]<row_to_be_deleted<=pieces[i][1]+pieces[i][3]:
                #new_h=pieces[i][3]-20
                #pieces[i][3]=new_h
            
        
        #if delete_row:
            #pieces.pop(delete_row_number)

        return pieces
    
    def reposition_pieces(pieces, row_to_be_deleted):
        for i in range(len(pieces)):
            if pieces[i][1]>=row_to_be_deleted:
                new_y=pieces[i][1]+20
                pieces[i][1]=new_y
            
        return pieces

 


