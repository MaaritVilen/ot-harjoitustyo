class Counting():

    def __init__(self):
           self.dummy=[]
    
    def count_x(x, width, move_left, move_right):
        if 0<=x and x+width<=500:
            if 0<=x<5:
                x=0+move_right
            elif 495-width<x<=500-width:
                x=500-width+move_left
            else:
                x+=move_left
                x+=move_right
        
        return x
    
    def count_y(y,height):
                
        if y+height<=700:
            y+=1
        
        return y