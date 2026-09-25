import random
import pygame
pygame.init()

clock = pygame.time.Clock()

Width = 800
Height = 600

spawn_time = pygame.time.get_ticks()

 
font = pygame.font.Font(None,50)
start_text = font.render("START",True,(255,255,255))

Screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Rain Is falling")

running = True

game_state = "start"# start buttonm
start_button = pygame.Rect(300,250,200,70)

gravity = 0.2 # gravity

max_rain = 200  # change how many drop will be but it will every time 10 more per creation

rain = []
rain_width = 2
rain_lenth = 10

rain_y = 0
rain_velo_y = 0

rain_x = 0




title = font.render("RAIN SIMULATION", True, (255,255,255)) 
while running:


    Screen.fill((30,30,30))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "start":
                if start_button.collidepoint(event.pos):
                    game_state = "rain"

    
    if game_state == "start":
    
        pygame.draw.rect(Screen,(100,150,255),start_button)
        Screen.blit(title,(250,100))
        Screen.blit(start_text,(345,270))

    


    
    elif game_state=="rain":
        current_time = pygame.time.get_ticks()

        if current_time - spawn_time >= 300:     # checking how much rains hould created at particular time
                if len(rain) < max_rain:
                     for i in range(1,11):
                          rain_x = random.randint(0,799)
                          rain_y = random.randint(-100,-10)
                          rain.append((rain_x,rain_y,rain_velo_y))
                    
            
                     spawn_time = current_time
        



        for pos,i in enumerate(rain):
            velo = i[2]
            velo+=gravity
            y = i[1] # y postion
            y+=velo # velocity here
            new_tup = (i[0],y,velo)
            
            
            rain[pos] = new_tup

                     
            if y>=600:
                new_y = random.randint(-100,-10)
                velo = 0
                rain[pos] = (i[0],new_y,velo)

        for i in rain:
             pygame.draw.line(Screen,(0,0,255),
                              (i[0],y),
                              (i[0],y+rain_lenth),rain_width)

                    


                                            


            
        pass



    pygame.display.update()
    clock.tick(60)
pygame.quit()



    
        
        
        

    