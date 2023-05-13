"""Program game loop, screen display and players actions are coded in this file."""
import pygame
from gaimsettings import GaimSettings
from shapes import Shapes
from counting import Counting

class MainBody():
    """This class includes game loop, sreen display and players actions."""
    def __init__(self):
        self.gamestatus=0
        self.new_shape=True
        self.event=""

    def main(self):
        """Game loop is, sreen display and reading players actions are in this function"""
        shape=Shapes()
        count=Counting()
        gaimsettings=GaimSettings()
        shape.new_shape()
        shape.start_position()
        self.x=shape.start
        self.y=0
        move_right=0
        move_left=0
        string=""
        pieces=[]
        pygame.init()
        screen = pygame.display.set_mode((500, 700))
        clock=pygame.time.Clock()
        font = pygame.font.SysFont("Arial", 24)

        def draw_screen(self):
            """This function draws screen in different game status"""
            gaimsettings=GaimSettings()
            screen.fill((0,0,0))
            if self.gamestatus==0:
                text = font.render("Please insert your name and then hit enter.", True, (0, 200, 255))
                screen.blit(text, (50, 50))
                teksti_2 = font.render(string, True, (0, 100, 255))
                screen.blit(teksti_2, (100,100))
            elif self.gamestatus==1:
                text_3=font.render(f"Hello {string} your all time high scores are {gaimsettings.previous_results(string)}", True, (0,200,200))
                text_4=font.render(f"Hit enter to start game", True, (0,200,200))
                screen.blit(text_3, (100,150))
                screen.blit(text_4,(100,500))
            elif self.gamestatus==2:
                pygame.draw.rect(screen, (0, 255, 200), (self.x, self.y, shape.w, shape.h))
                for i in range(len(pieces)):
                    pygame.draw.rect(screen, (0, 255, 200), (pieces[i][0], pieces[i][1], pieces[i][2], pieces[i][3]))
                text_5=font.render(f"Socers: {count.scores}", True, (0,255,200))
                screen.blit(text_5, (400,30))
            elif self.gamestatus==3:
                text_5=font.render(f"Game over. Your total scores were {count.scores}", True, (0,255,200))
                text_6=font.render(f"Do you want to play new game? Yes(y)/No(n)", True, (0,255,200))
                screen.blit(text_5, (100,150))
                screen.blit(text_6, (100,150))
            elif self.gamestatus==4:
                text_7=font.render("Thank you for playing with us!", True, (0,255,200))
                screen.blit(text_7, (100,150))
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
                            move_right=10
                        elif event.key==pygame.K_LEFT:
                            move_left=-10
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
                            if count.final_y<=0:
                                self.gamestatus=3
                            self.y=count.final_y
                            self.x=count.final_x
                            pieces.append([self.x, self.y, shape.w, shape.h])
                            new_pieces=count.check_shapes(pieces)
                            pieces=new_pieces
                            shape.new_shape()
                            shape.start_position()
                            self.x=shape.start
                            self.y=0
                    elif self.gamestatus==3:
                        if event.key==pygame.K_y:
                            self.gamestatus==2
                        elif event.key==pygame.K_n:
                            self.gamestatus==4

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
                if count.final_y<=0:
                    self.gamestatus=4
                if self.y==count.final_y:
                    self.x=count.final_x
                    pieces.append([self.x, self.y, shape.w, shape.h])
                    new_pieces=count.check_shapes(pieces)
                    pieces=new_pieces
                    shape.new_shape()
                    shape.start_position()
                    self.x=shape.start
                    self.y=0

            if event.type == pygame.QUIT:
                print(pieces)
                exit()
     
            draw_screen(self)              
            clock.tick(gaimsettings.speed_of_the_shape(count.scores))      

new_game=MainBody()
new_game.main()
