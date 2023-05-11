from shapes import Shapes

class Counting():

    def __init__(self):
        self.dummy=[]
        self.new_hight=0
        self.new_width=0
        self.highest_y=700
        self.final_y=0
        self.final_x=0
        self.rows={}
        self.delete_row=0
        self.scores=0

    def count_x(self, x, width, move_left, move_right):
        if 0<=x and x+width<=500:
            if 0<=x<20:
                x=0+move_right
            elif 480-width<x<=500-width:
                x=500-width+move_left
            else:
                x+=move_left
                x+=move_right
        return x
    
    def count_y(self, y, height):        
        if y+height<700:
            y+=1
        return y
    
    def turn_shape(self, height, width):
        self.new_height=width
        self.new_width=height
        return (self.new_height, self.new_width)

    def count_old_shapes(self, x, width, height, pieces):
        add=0
        self.highest_y=700
        for i in range(len(pieces)):
            if pieces[i][0]<x<pieces[i][0]+pieces[i][2] or pieces[i][0]<x+width<pieces[i][0]+pieces[i][2] or pieces[i][0]<(x+(width/2))<pieces[i][0]+pieces[i][2]:
            #if x<pieces[i][0]<x+width or x<pieces[i][0]+pieces[i][2]<x+width:
                if pieces[i][1]<self.highest_y:
                    self.highest_y=pieces[i][1]
        self.final_y=self.highest_y-height

        x_1=x/20
        x_2=x//20
        x_3=float(x_2)-x_1
        if x_3>=0.5:
            add=19
        self.final_x=(x_2*20)+add



    def check_shapes(self, pieces):
        shapes=Shapes
        i=680
        while i>0:
            sum=0
            for j in range(len(pieces)):
                if pieces[j][1]<=i < pieces[j][1]+pieces[j][3]:
                    sum+=pieces[j][2]
                    if sum>=500:
                        #row_to_be_deleted=i
                        pieces=shapes.delete_row(pieces, i)
                        pieces=shapes.reposition_pieces(pieces, i)
                        self.scores+=10
                        
            
            i-=20
        return pieces

    #Alla vanhoja
    
    def add_shape_on_row(self, shape):
        sum=0
        if shape[1] not in self.rows:
            self.rows[shape[1]]=shape[0]
        else:
            sum=self.rows[1]+shape[0]
            if sum>=500:
                self.delete_row=shape[1]
            else:
                self.rows[shape[1]]=sum
    
    def count_rows(self, pieces):
        new_row=[]
        for row in range(len(pieces)):
            if pieces[row][1]==self.delete_row:
                for j in range(len(row)):
                    if j==1:
                        new_row.append(row[j]+20)
                    elif j==3:
                        new_row.append(row[j]-20)
                    else:
                        new_row.append(row[j])
                pieces.pop(row)
                pieces.append(new_row)
        return pieces

    
    def count_rows_1(self, pieces):
        i=680
        
        while i>0:
            delete_row=0
            check=[]
            sum=0
            for j in range(len(pieces)):
                if pieces[j][1]<i<pieces[j][1]+pieces[j][2]:
                    sum+=pieces[j][0]
                    check.append(pieces[j])
                    if sum>=500:
                        delete_row=j
                        new_row=[]
                        for y in range(len(check)):
                            if y==1:
                                new_row.append(check[1]-20)
                            else:
                                new_row.append(check[1])
            
            if delete_row!=0:
                pieces.pop(j)
                pieces.append(new_row)
                
            else:
                i-=20
        return(pieces)


    
     

