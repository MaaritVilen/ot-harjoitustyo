class Counting():

    def __init__(self):
        self.dummy=[]
        self.new_hight=0
        self.new_width=0
        self.highest_y=700
        self.final_y=0

    def count_x(self, x, width, move_left, move_right):
        if 0<=x and x+width<=500:
            if 0<=x<5:
                x=0+move_right
            elif 495-width<x<=500-width:
                x=500-width+move_left
            else:
                x+=move_left
                x+=move_right
        return x
    
    def count_y(self, y,height):        
        if y+height<700:
            y+=1
        return y
    
    def turn_shape(self, height, width):
        self.new_height=width
        self.new_width=height
        return (self.new_height, self.new_width)

    def count_old_shapes(self, x, width, height, palikat):
        self.highest_y=700
        for i in range(len(palikat)):
            if x<=palikat[i][0]<=x+width or x<=palikat[i][0]+palikat[i][2]<=x+width:
                if palikat[i][1]<self.highest_y:
                    self.highest_y=palikat[i][1]
        self.final_y=self.highest_y-height
    
     

