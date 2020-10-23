import random
import copy
import time
import pygame
from main_program.parameters.constants import Constants as CONST
from main_program.display_objects.display_objects import *


class Item:
    """The items Mac need to pickup to escape"""

    def __init__(self, item_name, Xposition, Yposition):
        self.item_name = item_name
        self.Xposition = Xposition
        self.Yposition = Yposition


class Hero:
    """Main character of the game: Mac Gyver"""

    def __init__(self, labyrinth, game_window, pictures):
        self.Xposition = CONST.start_X
        self.Yposition = CONST.start_Y
        self.pockets = []
        self.game_window = game_window
        self.pictures = pictures

    def pickup(self, labyrinth, Xposition, Yposition, pockets):
        """add items in Mac's pocket when he moves on it"""
        if labyrinth.maze[self.Yposition][self.Xposition] in CONST.item_type:
            pockets.append(labyrinth.maze[self.Yposition][self.Xposition])
            userfeedback = 'pickup'
            Messages_Display(userfeedback)
            time.sleep(0.5)
        else:
            pass

    def vertical_movement(
        self,
        labyrinth,
        virgin_labyrinth,
        Xposition, Yposition,
        event,
        pictures
    ):
        """Move Mac Gyver vertically"""
        Y_before_move = self.Yposition
        # Save the starting position of mac
        # in roder to reinitialize the maze's cell after he moves
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            # Check if movement is possible, update  (or not) Mac's position
            if labyrinth.maze[self.Yposition - 1][self.Xposition] != 1:
                self.Yposition = self.Yposition - 1
                userfeedback = 0
            if labyrinth.maze[Y_before_move - 1][self.Xposition] == 1:
                userfeedback = 'collision'

        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            if labyrinth.maze[self.Yposition + 1][self.Xposition] != 1:
                self.Yposition = self.Yposition + 1
                userfeedback = 0
            if labyrinth.maze[Y_before_move + 1][self.Xposition] == 1:
                userfeedback = 'collision'

        self.pickup(labyrinth, self.Xposition, self.Yposition, self.pockets)
        # Re-initialize the cell from which Mac moved
        labyrinth.maze[Y_before_move][self.Xposition] = virgin_labyrinth.maze[
            Y_before_move
        ][self.Xposition]
        # Update Mac's position in the maze
        labyrinth.maze[self.Yposition][self.Xposition] = "M"
        # Update the Labyrinth display
        LabyrinthDisplay.update_Display(
            labyrinth,
            self.Xposition, self.Yposition,
            self.Xposition, Y_before_move,
            pictures)
        # Visual feedback in case of collision
        Messages_Display(userfeedback)

    def horizontal_movement(
        self,
        labyrinth,
        virgin_labyrinth,
        Xposition, Yposition,
        event,
        pictures
    ):
        """Move Mac Gyver horizontally"""
        X_before_move = self.Xposition

        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            if labyrinth.maze[self.Yposition][self.Xposition - 1] != 1:
                self.Xposition = self.Xposition - 1
                userfeedback = 0
            if labyrinth.maze[self.Yposition][X_before_move - 1] == 1:
                userfeedback = 'collision'

        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            if labyrinth.maze[self.Yposition][self.Xposition + 1] != 1:
                self.Xposition = self.Xposition + 1
                userfeedback = 0
            if labyrinth.maze[self.Yposition][X_before_move + 1] == 1:
                userfeedback = 'collision'

        self.pickup(labyrinth, self.Xposition, self.Yposition, self.pockets)
        labyrinth.maze[self.Yposition][X_before_move] = virgin_labyrinth.maze[
            self.Yposition
        ][X_before_move]
        labyrinth.maze[self.Yposition][self.Xposition] = "M"
        LabyrinthDisplay.update_Display(
            labyrinth,
            self.Xposition, self.Yposition,
            X_before_move, self.Yposition,
            pictures)
        Messages_Display(userfeedback)
