import time
import pygame

# labyrinth
start_X = 0
start_Y = 3
finish_X = 14
finish_Y = 12
maze_path = "C:/Users/matthieu/GitHub/P3_McGyver/Labyrinth/labyrinth.txt"
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
mac_path = 'ressource/MacGyver50px.png'
guard_path = 'ressource/Gardien50px.png'
needle_path = 'ressource/aiguille50px.png'
tube_path = 'ressource/tube50px.png'
ether_path = 'ressource/ether50px.png'
wall_path = 'ressource/wall50px.png'
empty_path = 'ressource/blank50px.png'
start_path = 'ressource/start50px.png'


# Parameters for the objects surface
height_objects_surface = CELL_HEIGHT
width_objects_surface = 4*CELL_WIDTH

# Parameters for the messages surface
height_messages_surface = 3*CELL_HEIGHT
width_messages_surface = WIDTH_LABYRINTH-width_objects_surface-CELL_WIDTH
white = (255, 255, 255)
orange = (239, 159, 45)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
msg_screen_X = HORIZONTAL_OFFSET+width_objects_surface+CELL_WIDTH
msg_screen_Y = HEIGHT_LABYRINTH+CELL_HEIGHT*2
txt_X = msg_screen_X+5
txt_Y = msg_screen_Y+16
possible_user_feedbacks = [0, 'win', 'loose', 'collision', 'pickup', 'invalid']
txt_user_feedbacks = {0: '', 'win': 'CONGRATS YOU WON', 'loose': 'SORRY YOU LOST',
                      'collision': 'you hit a wall', 'pickup': 'You picked up an item', 'invalid': 'You pressed an invalid key'}
bg_color_feedbacks = {0: maze_bg_color, 'win': green, 'loose': red,
                      'collision': orange, 'pickup': green, 'invalid': orange}
txt_color_feedbacks = {0: maze_bg_color, 'win': black, 'loose': black,
                       'collision': white, 'pickup': black, 'invalid': black}

# Informations for the movements
pygame.init()
OK_user_inputs = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
pygame.quit()


# class messages:
#     def hit_wall():
#         print("\n you hit a wall\n")

#     def suspense():
#         print(".")
#         time.sleep(0.5)
#         print("..")
#         time.sleep(0.5)
#         print("...")
#         time.sleep(0.5)
#         print("....")

#     def win():
#         print("\nYou reach the exit of the maze")
#         messages.suspense()
#         print(
#             "Damned, this guard looks really in shape... How could you pass through him?"
#         )
#         messages.suspense()
#         print(
#             "You take the needle, the tube and the ether you previously found in the maze and assemble them to make a tranquilizer"
#         )
#         messages.suspense()
#         print(
#             "You jump on the guard, inject him the ether and wait a few seconds, he falls on the floor, this is your chance!"
#         )
#         messages.suspense()
#         print(
#             "You run towards the exit, pass the door and that's it, tyou can feel a nice warm breeze on your cheeks"
#         )
#         messages.suspense()
#         print("CONGRATULATIONS You've won")

#     def loose():
#         print(
#             "\nYou reach the exit but you do not have all the elements to craft your tranquilizer"
#         )
#         messages.suspense()
#         print("You try to tell the guard the best joke you know but...")
#         messages.suspense()
#         print("he looks at you with no pity and hits you with his tazer.")
#         messages.suspense()
#         print("you lost")
#         print("  _____")
#         print(" /     \ ")
#         print("| () () |")
#         print(" \  ^  / ")
#         print("  ||||| ")
#         print("  ||||| ")
