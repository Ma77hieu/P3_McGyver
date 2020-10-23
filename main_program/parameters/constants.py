import time
import pygame


class Constants:
    def __init__(self):
        pass

    # labyrinth
    start_X = 0
    start_Y = 3
    finish_X = 14
    finish_Y = 12
    maze_path = "C:/Users/matthieu/GitHub/Project3/P3_McGyver/Labyrinth/labyrinth.txt"
    maze_size = 15
    item_type = ["N", "E", "T"]  # N for needle, T for tube and E for ether

    # Parameters for the game window
    game_window_width = 1000
    game_window_height = 1000
    game_window_title = "Escape the maze or be DOOMED"

    # Parameters for the maze surface
    VERTICAL_OFFSET = 50
    HORIZONTAL_OFFSET = 120
    CELL_WIDTH = 50
    CELL_HEIGHT = 50
    NBR_X_CELL = 15
    NBR_Y_CELL = 15
    WIDTH_LABYRINTH = NBR_Y_CELL*CELL_HEIGHT
    HEIGHT_LABYRINTH = NBR_Y_CELL*CELL_HEIGHT
    maze_bg_color = (244, 244, 239)

    # load the images for the maze
    mac_path = 'P3_McGyver/ressource/MacGyver50px.png'
    guard_path = 'P3_McGyver/ressource/Gardien50px.png'
    needle_path = 'P3_McGyver/ressource/aiguille50px.png'
    tube_path = 'P3_McGyver/ressource/tube50px.png'
    ether_path = 'P3_McGyver/ressource/ether50px.png'
    wall_path = 'P3_McGyver/ressource/wall50px.png'
    empty_path = 'P3_McGyver/ressource/blank50px.png'
    start_path = 'P3_McGyver/ressource/start50px.png'

    # Parameters for the objects surface
    height_objects_surface = CELL_HEIGHT
    width_objects_surface = 4*CELL_WIDTH

    # Parameters for the messages surface
    height_messages_surface = CELL_HEIGHT
    width_messages_surface = 5*CELL_WIDTH
    white = (255, 255, 255)
    orange = (239, 159, 45)
    green = (0, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)
    msg_screen_X = HORIZONTAL_OFFSET+width_objects_surface+5*CELL_WIDTH
    msg_screen_Y = HEIGHT_LABYRINTH+CELL_HEIGHT*2
    txt_X = msg_screen_X+5
    txt_Y = msg_screen_Y+16
    possible_user_feedbacks = [
        0, 'win', 'loose', 'collision', 'pickup', 'invalid']
    txt_user_feedbacks = {0: '', 'win': 'CONGRATS YOU WON', 'loose': 'SORRY YOU LOST',
                          'collision': 'you hit a wall', 'pickup': 'You pick up an item', 'invalid': 'You pressed an invalid key'}
    bg_color_feedbacks = {0: maze_bg_color, 'win': green, 'loose': red,
                          'collision': orange, 'pickup': green, 'invalid': orange}
    txt_color_feedbacks = {0: maze_bg_color, 'win': black, 'loose': black,
                           'collision': black, 'pickup': black, 'invalid': black}

    # Informations for the movements
    pygame.init()
    OK_user_inputs = [pygame.K_LEFT,
                      pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    pygame.quit()
