import pygame
import time

def tests_pygame():
    pygame.init()

    #define the useful parameters values
    LINE_WIDTH=4
    VERTICAL_OFFSET=10
    HORIZONTAL_OFFSET=10
    CELL_WIDTH=50
    CELL_HEIGHT=50
    NBR_X_CELL=15
    NBR_Y_CELL=15
    WIDTH_LABYRINTH=NBR_Y_CELL*CELL_HEIGHT+(NBR_X_CELL)*LINE_WIDTH
    HEIGHT_LABYRINTH=NBR_Y_CELL*CELL_HEIGHT+(NBR_Y_CELL)*LINE_WIDTH

    def draw_grid():
        bg = (255, 255, 200)
        grid = (50, 50, 50)
        game_screen.fill(bg)
        pygame.draw.line(game_screen, grid, (HORIZONTAL_OFFSET,VERTICAL_OFFSET), (HORIZONTAL_OFFSET,VERTICAL_OFFSET+HEIGHT_LABYRINTH), LINE_WIDTH)
        pygame.draw.line(game_screen, grid, (HORIZONTAL_OFFSET,VERTICAL_OFFSET), (HORIZONTAL_OFFSET+WIDTH_LABYRINTH,VERTICAL_OFFSET), LINE_WIDTH)
        for x in range(1,NBR_X_CELL+1):
            line_begin_pos=((x*CELL_WIDTH)+(x*LINE_WIDTH)+HORIZONTAL_OFFSET, VERTICAL_OFFSET)
            line_end_pos=((x*CELL_WIDTH)+(x*LINE_WIDTH)+HORIZONTAL_OFFSET,HEIGHT_LABYRINTH+VERTICAL_OFFSET)
            pygame.draw.line(game_screen, grid, line_begin_pos, line_end_pos, LINE_WIDTH)
            time.sleep(0.1)
            pygame.display.update()
        for y in range(1,NBR_Y_CELL+1):
            line_begin_pos=(HORIZONTAL_OFFSET,(y*CELL_HEIGHT)+(y*LINE_WIDTH)+VERTICAL_OFFSET)
            line_end_pos=(WIDTH_LABYRINTH+HORIZONTAL_OFFSET,(y*CELL_HEIGHT)+(y*LINE_WIDTH)+VERTICAL_OFFSET)
            pygame.draw.line(game_screen, grid, line_begin_pos, line_end_pos, LINE_WIDTH)
            time.sleep(0.1)
            pygame.display.update()                  
        time.sleep(3)

    draw_grid()

    
    def display_or_exit():
        #load the required images
        mac=pygame.image.load('ressource/MacGyver.png').convert_alpha()
        guard=pygame.image.load("ressource/Gardien.png").convert_alpha()
        needle=pygame.image.load("ressource/aiguille.png").convert_alpha()
        seringe=pygame.image.load("ressource/seringue.png").convert_alpha()
        ether=pygame.image.load("ressource/ether.png").convert_alpha()
        wall=pygame.image.load("ressource/wall.png").convert_alpha()
        keep=True
        i=0
        while keep:
            for event in pygame.event.get():
                if event.type==pygame.QUIT or(event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                    keep=0
                elif event.type==pygame.KEYDOWN and i<NBR_Y_CELL:
                    game_screen.blit(wall,(HORIZONTAL_OFFSET,(i*CELL_HEIGHT)+VERTICAL_OFFSET+(i+1)*LINE_WIDTH))
                    pygame.display.flip()
                    i+=1
                if i>=NBR_Y_CELL:
                    keep=0

    display_or_exit()

game_screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Find the exit or be DOOMED")

tests_pygame()
pygame.quit()   
