"""This module calculates movements of the shapes 
and their final position on the screen"""
from shapes import Shapes

class Counting():
    """This class calculates movements of the shapes 
    and their final position on the screen"""

    def __init__(self):
        self.new_height=0
        self.new_width=0
        self.highest_y=700
        self.final_y=0
        self.final_x=0
        self.delete_row=0
        self.scores=0

    def count_x(self, shape_x, width, move_left, move_right):
        """The function calculates the movement the player has chosen"""
        if 0<=shape_x and shape_x+width<=500:
            if 0<=shape_x<10:
                shape_x=0+move_right
            elif 490-width<shape_x<=500-width:
                shape_x=500-width+move_left
            else:
                shape_x+=move_left
                shape_x+=move_right
        return shape_x

    def count_y(self, shape_y, height):
        """The function calculates the movement of the droppping shape"""
        if shape_y+height<700:
            shape_y+=1
        return shape_y

    def turn_shape(self, height, width):
        """The function turns the shape when the player has chosen so"""
        self.new_height=width
        self.new_width=height
        return (self.new_height, self.new_width)

    def count_old_shapes(self, shape_x, width, height, pieces):
        """The function goes through the old shapes to limit the movement 
        of the new shape so that it does not cross the old shapes"""
        add=0
        self.highest_y=700
        for i in range(len(pieces)):
            if pieces[i][0]<shape_x<pieces[i][0]+pieces[i][2] or pieces[i][0]<shape_x+width<pieces[i][0]+pieces[i][2] or pieces[i][0]<(shape_x+(width/2))<pieces[i][0]+pieces[i][2]:
                if pieces[i][1]<self.highest_y:
                    self.highest_y=pieces[i][1]
        self.final_y=self.highest_y-height

        x_1=shape_x/20
        x_2=shape_x//20
        x_3=float(x_2)-x_1
        if x_3>=0.5:
            add=19
        self.final_x=(x_2*20)+add

    def check_shapes(self, pieces):
        """The function checks whether row is 'full' and needs to be deleted"""
        shapes=Shapes
        i=680
        while i>0:
            sum=0
            for j in range(len(pieces)):
                if pieces[j][1]<=i < pieces[j][1]+pieces[j][3]:
                    sum+=pieces[j][2]
                    if sum>=500:
                        pieces=shapes.reshape_pieces(pieces, i)
                        pieces=shapes.reposition_pieces(pieces, i)
                        self.scores+=10
            i-=20
        return pieces
