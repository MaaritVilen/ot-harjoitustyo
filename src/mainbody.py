#Pelirungon koodia pitää vielä jäsennellä paremmin. Tarkoitus oli ensin saada looppi toimimaan...

import pygame
#from sprites.box import Box

#The shapes that are droping out from the sky are created in this class.
class Shapes:
    def __inint__():
        pass

    def flatt_vertical():
        pass

    def flatt_horisontal():
        pass

#gaim settings like speed of the game are defined here
class GaimSettings():
    def __init__(self):
        pass

    def create_game():
        pass

    def ask_name():
        pass

    def drop_speed_of_the_shape():
        pass

    # When shape stops the function checks whether the row should be deleted.
    def check_row():
        pass

    def save_result(self, name, result):
        new_name="yes"
        new_result="no"
        with open("results.csv") as results:
            new_list=[]
            for line in results:
                sub_list=[]
                line=line.replace("\n","")
                parts=line.split(";")
                for part in parts:
                    sub_list.append(part)
                if sub_list[0]==name:
                    new_name="no"
                    if int(sub_list[1])<result:
                        new_result="yes"
                        sub_list[1]=result
                new_list.append(sub_list)
        
        if new_name=="yes":
            with open("results.csv","a") as updated_results:
                updated_results.write(f"{name};{result}\n")
        elif new_result=="yes":
            with open("results.csv", "w") as updated_results:
                for line in new_list:
                    updated_results.write(f"{line[0]};{line[1]}\n")
        
    def previous_results(self,name):
        result=0
        with open("results.csv") as results:
            for line in results:
                line=line.replace("\n","")
                parts=line.split(";")
                if parts[0]==name:
                    result=parts[1]
        return result

#The game is run in this function
class MainBody():
    def __init__(self):
        self.gamestatus=0

    def main(self):
        #gaimsettings=GaimSettings()
        #create scene
        #gamestatus=0
        string=""
        pygame.init()
        screen = pygame.display.set_mode((800, 560))
        
        #clock=pygame.time.Clock()
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
                screen.blit(text_3, (100,150))
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

            if event.type == pygame.QUIT:
                exit()

        
            draw_screen(self)
        
                            
            #clock.tick(60)      

gaim=MainBody()
gaim.main()
#create=GaimSettings()
#create.save_result("jaakko",14)
#print(create.previous_results("jaakko"))