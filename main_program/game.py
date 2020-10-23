import random
import copy
import time
import pygame
from main_program.parameters.constants import Constants as CONST
from main_program.game_objects.objects import *
from main_program.display_objects.display_objects import *
from main_program.Labyrinth.maze import *

def main():
    """Runs the game"""
    # Creation of our labyrinth instance
    labyrinth = Labyrinth()

    # Creation of a copy of our labyrinth
    # it will be used to remember the type of the cell from which mcGyver moves
    labyrinth_copy = copy.deepcopy(labyrinth)

    # Place the items in our labyrinth
    labyrinth.place_items()

    # Creation of the overall game window
    game_window = GameWindow()

    # Loading of our images dictionnary
    # this dictionnary links maze letters to the right images for pygame
    pictures = Images()

    # creation of our character instance
    macG = Hero(labyrinth, game_window, pictures)

    # Display of our objects inside the game window
    Objects_Display(pictures, macG.pockets)

    # Creation of our labyrinth display inside the game window
    LabyrinthDisplay(labyrinth, pictures)

    # Definition of a variable to know when to end the game
    game_on_going = True

    while game_on_going:
        userfeedback = ''
        for event in pygame.event.get():
            # Setup two ways for ending the game:
            # click the red cross or escape key
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and (
                        event.key == pygame.K_ESCAPE)):
                game_on_going = 0
            elif event.type == pygame.KEYUP and (
                    event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                macG.vertical_movement(
                    labyrinth,
                    labyrinth_copy,
                    macG.Xposition,
                    macG.Yposition,
                    event,
                    pictures
                )
            elif event.type == pygame.KEYUP and (
                    event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                macG.horizontal_movement(
                    labyrinth,
                    labyrinth_copy,
                    macG.Xposition,
                    macG.Yposition,
                    event,
                    pictures
                )
            # Give feedback to the user if the key pressed is not accepted
            elif event.type == pygame.KEYDOWN and (
                    event.key not in CONST.OK_user_inputs):
                userfeedback = 'invalid'
                Messages_Display(userfeedback)
            Objects_Display(pictures, macG.pockets)

            # Check if Mac reached the end of the maze
            if labyrinth.is_end(macG.Xposition, macG.Yposition) is True:
                # Mac has all required items = player wins
                if ("N" in macG.pockets and "T" in macG.pockets and (
                        "E" in macG.pockets)):
                    userfeedback = 'win'
                    Messages_Display(userfeedback)
                    time.sleep(2)
                    game_on_going = 0
                # Mac does not have all required items = player looses
                else:
                    userfeedback = 'loose'
                    Messages_Display(userfeedback)
                    time.sleep(2)
                    game_on_going = 0


pygame.init()
main()
pygame.quit()
