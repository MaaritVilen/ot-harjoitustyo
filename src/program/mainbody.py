import pygame
from gaimsettings import GaimSettings
from shapes import Shapes
from counting import Counting
#from sprites.box import Box

class MainBody():
    def __init__(self):
        self.gamestatus=0
        self.new_shape=True
    
    def main(self):
        shape=Shapes()
        count=Counting()
        shape.new_shape()
        shape.start_position()
        self.x=shape.start
        self.y=0
        move_right=0
        move_left=0
        turn=False
        string=""
        pieces=[]
        pygame.init()
        screen = pygame.display.set_mode((500, 700))
        
        clock=pygame.time.Clock()
        fontti = pygame.font.SysFont("Arial", 24)
        
        def draw_screen(self):
            gaimsettings=GaimSettings()
            screen.fill((0,0,0))
            if self.gamestatus==0:
                teksti = fontti.render("Please insert your name and then hit enter.", True, (255, 255, 255))
                screen.blit(teksti, (100, 50))
                teksti_2 = fontti.render(string, True, (255, 0, 0))
                screen.blit(teksti_2, (100,100))
            if self.gamestatus==1:
                text_3=fontti.render(f"Hello {string} your all time high scores are {gaimsettings.previous_results(string)}", True, (0,255,0))
                text_4=fontti.render(f"Hit enter to start game", True, (0,255,0))
                screen.blit(text_3, (100,150))
                screen.blit(text_4,(100,500))
            if self.gamestatus==2:
                pygame.draw.rect(screen, (0, 255, 200), (self.x, self.y, shape.w, shape.h))
                for i in range(len(pieces)):
                    pygame.draw.rect(screen, (0, 255, 200), (pieces[i][0], pieces[i][1], pieces[i][2], pieces[i][3]))

            pygame.display.flip()
        
    
        while True:

            for event in pygame.event.get(): 
                if event.type==pygame.KEYDOWN:
                    if self.gamestatus==0:                
                        if event.key==pygame.K_a:
                            string+="a"
                        elif event.key==pygame.K_b:
                            string+="b"
                        elif event.key==pygame.K_c:
                            string+="c"
                        elif event.key==pygame.K_d:
                            string+="d"
                        elif event.key==pygame.K_e:
                            string+="e"
                        elif event.key==pygame.K_f:
                            string+="f"
                        elif event.key==pygame.K_g:
                            string+="g"
                        elif event.key==pygame.K_h:
                            string+="h"
                        elif event.key==pygame.K_i:
                            string+="i"
                        elif event.key==pygame.K_j:
                            string+="j"
                        elif event.key==pygame.K_k:
                            string+="k"
                        elif event.key==pygame.K_l:
                            string+="l"
                        elif event.key==pygame.K_m:
                            string+="m"
                        elif event.key==pygame.K_n:
                            string+="n"
                        elif event.key==pygame.K_o:
                            string+="o"
                        elif event.key==pygame.K_p:
                            string+="p"
                        elif event.key==pygame.K_q:
                            string+="q"
                        elif event.key==pygame.K_r:
                            string+="r"
                        elif event.key==pygame.K_s:
                            string+="s"
                        elif event.key==pygame.K_t:
                            string+="t"
                        elif event.key==pygame.K_u:
                            string+="u"
                        elif event.key==pygame.K_v:
                            string+="v"
                        elif event.key==pygame.K_x:
                            string+="x"
                        elif event.key==pygame.K_y:
                            string+="y"
                        elif event.key==pygame.K_z:
                            string+="z"    
                        elif event.key==pygame.K_RETURN:
                            self.gamestatus=1
                    elif self.gamestatus==1:
                        if event.key==pygame.K_RETURN:
                            self.gamestatus=2
                            shape.new_shape()
                    elif self.gamestatus==2:
                        if event.key==pygame.K_RIGHT:
                            move_right=20
                        elif event.key==pygame.K_LEFT:
                            move_left=-20
                        elif event.key==pygame.K_UP:
                            count.turn_shape(shape.h, shape.w)
                            shape.h=count.new_height
                            shape.w=count.new_width    
                        elif event.key==pygame.K_DOWN:
                            count.turn_shape(shape.h, shape.w)
                            shape.h=count.new_height
                            shape.w=count.new_width
                        elif event.key==pygame.K_RETURN:
                            count.count_old_shapes(self.x, shape.w, shape.h, pieces)
                            self.y=count.final_y
                            pieces.append([self.x, self.y, shape.w, shape.h])
                            shape.new_shape()
                            shape.start_position()
                            self.x=shape.start
                            self.y=0
                            
                if event.type==pygame.KEYUP:
                    if self.gamestatus==2:
                        if event.key==pygame.K_RIGHT:
                            move_right=0
                        elif event.key==pygame.K_LEFT:
                            move_left=0
                        elif event.key==pygame.K_UP:
                            pass
                        elif event.key==pygame.K_DOWN:
                            pass
                        elif event.key==pygame.K_RETURN:
                            pass
            
            
            self.x=count.count_x(self.x, shape.w, move_left, move_right)
                       
            if self.gamestatus==2:
                self.y=count.count_y(self.y, shape.h)
                count.count_old_shapes(self.x, shape.w, shape.h, pieces)
                if self.y==count.final_y:
                    pieces.append([self.x, self.y, shape.w, shape.h])
                    shape.new_shape()
                    shape.start_position()
                    self.x=shape.start
                    self.y=0
               
            if event.type == pygame.QUIT:
                exit()
     
            draw_screen(self)              
            clock.tick(30)      

new_game=MainBody()
new_game.main()