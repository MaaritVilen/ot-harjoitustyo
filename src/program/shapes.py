"""This module creates new shapes randomly, chooses their starting position randomly and 
reshapes the shapes once a row has been deleted."""
from random import randint
from random import choice

class Shapes():
    """This module creates new shapes randomly, chooses their starting position randomly 
    and reshapes the shape once a row has been deleted."""
    def __init__(self):
        self.w=0
        self.h=0
        self.color=0
        self.start=0

    def new_shape(self):
        """The function chooses new shape randomly"""
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
        """The function chooses starting position randomly"""
        start=[0,40,100,160,200,240,300,360,400]
        self.start=choice(start)

    def reshape_pieces(pieces, row_to_be_deleted):
        """The function reshapes pieces once a row has been deleted."""
        for i in range(len(pieces)):
            if pieces[i][1]<=row_to_be_deleted<=pieces[i][1]+pieces[i][3]:
                new_y=pieces[i][1]+20
                new_h=pieces[i][3]-20
                pieces[i][1]=new_y
                pieces[i][3]=new_h
        pieces=Shapes.delete_row(pieces)
        return pieces

    def delete_row(pieces):
        """The function deletes a row."""
        to_delete=False
        for i in range(len(pieces)):
            if pieces[i][3]==0:
                to_be_deleted=i
                to_delete=True
        if to_delete:
            pieces.pop(to_be_deleted)
            Shapes.delete_row(pieces)
        return pieces

    def reposition_pieces(pieces, row_to_be_deleted):
        """The function repositions the shapes once a row has been deleted. 
        The function does not work correctly yet."""
        for i in range(len(pieces)):
            if pieces[i][1]>=row_to_be_deleted:
                new_y=pieces[i][1]+20
                pieces[i][1]=new_y
        return pieces
