import random
import copy
import time
import pygame
from main_program.parameters.constants import Constants as CONST


class GameWindow:
    """Global window of the game"""

    def __init__(self):
        self.game_screen = pygame.display.set_mode(
            (CONST.game_window_width, CONST.game_window_height))
        pygame.display.set_caption(CONST.game_window_title)
        self.game_screen.fill(CONST.maze_bg_color)


class Objects_Display(GameWindow):
    """ Zone to display the items in Mac's pockets"""

    def __init__(self, pictures, pockets=[]):
        GameWindow.__init__(self)
        objects_screen = pygame.Surface((
            CONST.width_objects_surface, CONST.height_objects_surface))
        objects_screen.fill(CONST.maze_bg_color)
        self.game_screen.blit(
            objects_screen, (CONST.HORIZONTAL_OFFSET, CONST.msg_screen_Y))
        font = pygame.font.Font('P3_McGyver/ressource/bahnschrift.ttf', 16)
        objects_text = font.render(
            'You have in your pockets:', True, CONST.black)
        self.game_screen.blit(
            objects_text, (CONST.HORIZONTAL_OFFSET+5, CONST.txt_Y))
        pygame.display.update(CONST.HORIZONTAL_OFFSET, CONST.msg_screen_Y,
                              CONST.width_objects_surface,
                              CONST.height_objects_surface)
        if pockets != []:
            for elem in range(len(pockets)):
                if pockets[elem] in CONST.item_type:
                    self.game_screen.blit(
                        pictures.images[pockets[elem]],
                        (CONST.HORIZONTAL_OFFSET+elem*CONST.CELL_WIDTH,
                         CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*3))
                    pygame.display.update
                    (CONST.HORIZONTAL_OFFSET+elem*CONST.CELL_WIDTH,
                     CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*3,
                     CONST.CELL_WIDTH, CONST.CELL_HEIGHT)


class Messages_Display(GameWindow):
    """Zone to display messages to the user to know what's happening"""

    def __init__(self, userfeedback):
        GameWindow.__init__(self)
        messages_screen = pygame.Surface((
            CONST.width_messages_surface, CONST.height_messages_surface))
        self.game_screen.blit(
            messages_screen, (CONST.msg_screen_X, CONST.msg_screen_Y))
        font = pygame.font.Font('P3_McGyver/ressource/bahnschrift.ttf', 16)
        if userfeedback in CONST.possible_user_feedbacks:
            messages_screen.fill(CONST.bg_color_feedbacks[userfeedback])
            self.game_screen.blit(
                messages_screen, (CONST.msg_screen_X, CONST.msg_screen_Y))
            objects_text = font.render(
                CONST.txt_user_feedbacks[userfeedback],
                True,
                CONST.txt_color_feedbacks[userfeedback])
            self.game_screen.blit(
                objects_text, (CONST.txt_X, CONST.txt_Y))
            pygame.display.update(CONST.msg_screen_X,
                                  CONST.msg_screen_Y,
                                  CONST.width_messages_surface,
                                  CONST.height_messages_surface)


class LabyrinthDisplay(GameWindow):
    """Display the labyrinth inside the game window"""

    def __init__(self, labyrinth, pictures):
        GameWindow.__init__(self)
        # self.game_window = game_window
        for row in range(0, CONST.maze_size):
            for column in range(0, CONST.maze_size):
                self.game_screen.blit(
                    pictures.images[labyrinth.maze[row][column]],
                    (CONST.HORIZONTAL_OFFSET+column*CONST.CELL_HEIGHT,
                     row*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
        pygame.display.flip()

    @classmethod
    def update_Display(self, labyrinth, X, Y, X_before, Y_before, pictures):
        """Update the labyrinth when Mac moves without 
        reloading the whole maze
        """
        self.__init__(self, labyrinth, pictures)
        self.game_screen.blit(
            pictures.images[labyrinth.maze[Y_before][X_before]],
            (CONST.HORIZONTAL_OFFSET+X_before*CONST.CELL_HEIGHT,
             Y_before*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
        self.game_screen.blit(
            pictures.images[labyrinth.maze[Y][X]],
            (CONST.HORIZONTAL_OFFSET+X*CONST.CELL_HEIGHT,
             Y*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
        min_x = min(X, X_before)
        min_y = min(Y, Y_before)
        max_x = max(X, X_before)
        max_y = max(Y, Y_before)
        pygame.display.update(
            min_x, min_y, (max_x-min_x), (max_y-min_y))


class Images:
    """Link the images to the letters inside the labyrinth"""

    def __init__(self):
        self.mac = pygame.image.load(CONST.mac_path).convert_alpha()
        self.guard = pygame.image.load(CONST.guard_path).convert_alpha()
        self.needle = pygame.image.load(CONST.needle_path).convert_alpha()
        self.tube = pygame.image.load(CONST.tube_path).convert_alpha()
        self.ether = pygame.image.load(CONST.ether_path).convert_alpha()
        self.wall = pygame.image.load(CONST.wall_path).convert_alpha()
        self.blank = pygame.image.load(CONST.empty_path).convert_alpha()
        self.start = pygame.image.load(CONST.start_path).convert_alpha()
        self.images = {"M": self.mac,
                       "N": self.needle,
                       "E": self.ether,
                       "T": self.tube,
                       "F": self.guard,
                       1: self.wall,
                       0: self.blank,
                       "S": self.start
                       }
