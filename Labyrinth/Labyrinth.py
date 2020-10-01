import pprint
import random
import copy
import time
import pygame
import constants as CONST


class Labyrinth_zone:
    def __init__(self):
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.type = zone_type


class Labyrinth:

    def __init__(self):
        self.Xposition = Xposition = 0
        self.Yposition = Yposition = 0
        self.sorted_maze = sorted_maze = []
        self.start_X = CONST.start_X
        self.start_Y = CONST.start_Y
        self.finish_X = CONST.finish_X
        self.finish_Y = CONST.finish_Y

        source_file = open(CONST.maze_path, "r")
        sorted_maze = []
        all_cells = source_file.read()
        all_cells = all_cells.split(",")
        for row in range(CONST.maze_size):
            line_cell = []
            for column in range(CONST.maze_size):
                line_cell.append(
                    int(all_cells[column + row * CONST.maze_size]))
            sorted_maze.append(line_cell)
        self.maze = sorted_maze
        self.maze[self.start_Y][self.start_X] = "S"
        self.maze[self.finish_Y][self.finish_X] = "F"

    def is_end_cell(self, X, Y):
        if X == self.finish_X and Y == self.finish_Y:
            return True
        return False

    def place_items(self):
        # place the items in the maze
        for component in CONST.item_type:
            item = Item(component, random.randint(
                0, CONST.maze_size-1), random.randint(0, CONST.maze_size-1))

            # make sure that item is not at the same position as start, finish or another item
            while self.maze[item.Yposition][item.Xposition] != 0:
                item.Xposition = random.randint(0, CONST.maze_size-1)
                item.Yposition = random.randint(0, CONST.maze_size-1)
            self.maze[item.Yposition][item.Xposition] = item.item_name


class GameWindow:
    def __init__(self):
        pass
    game_screen = pygame.display.set_mode(
        (CONST.game_window_width, CONST.game_window_height))
    pygame.display.set_caption(CONST.game_window_title)
    game_screen = game_screen
    game_screen.fill(CONST.maze_bg_color)
    mac = pygame.image.load(
        'ressource/MacGyver50px.png').convert_alpha()
    guard = pygame.image.load(
        "ressource/Gardien50px.png").convert_alpha()
    needle = pygame.image.load(
        "ressource/aiguille50px.png").convert_alpha()
    tube = pygame.image.load("ressource/tube50px.png").convert_alpha()
    seringe = pygame.image.load(
        "ressource/seringue.png").convert_alpha()
    ether = pygame.image.load(
        "ressource/ether50px.png").convert_alpha()
    wall = pygame.image.load("ressource/wall50px.png").convert_alpha()


class LabyrinthDisplay():
    def __init__(self, labyrinth, game_window):
        self.game_window = game_window
        self.labyrinth = labyrinth
        for row in range(0, CONST.maze_size):
            for column in range(0, CONST.maze_size):
                if self.labyrinth.maze[row][column] in self.pictures.images:
                    game_window.game_screen.blit(
                        self.pictures.images[labyrinth.maze[row][column]], (CONST.HORIZONTAL_OFFSET+column*CONST.CELL_HEIGHT, row*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
                    pygame.display.flip()
                elif self.labyrinth.maze[row][column] == 0:
                    pass
                elif any(self.labyrinth.maze[row][column] == items for items in CONST.item_type):
                    game_window.game_screen.blit(
                        mac, (CONST.HORIZONTAL_OFFSET+column*CONST.CELL_HEIGHT, row*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
                    pygame.display.flip()
        time.sleep(5)

    class Images():
        def __init__(self):
            pass

        images = {"M": GameWindow.mac,
                  "N": GameWindow.needle,
                  "E": GameWindow.ether,
                  "T": GameWindow.tube,
                  "F": GameWindow.guard,
                  1: GameWindow.wall
                  }
    pictures = Images()


class Item:
    def __init__(self, item_name, Xposition, Yposition):
        self.item_name = item_name
        self.Xposition = Xposition
        self.Yposition = Yposition


class Mc_Gyver:
    def __init__(self, labyrinth):
        self.Xposition = Xposition = CONST.start_X
        self.Yposition = Yposition = CONST.start_Y
        self.pockets = pockets = []

    def pickup(self, labyrinth, Xposition, Yposition, pockets):
        if labyrinth.maze[self.Yposition][self.Xposition] == "N":  # N for needle
            pockets.append("needle")
        if labyrinth.maze[self.Yposition][self.Xposition] == "T":  # T for tube
            pockets.append("tube")
        if labyrinth.maze[self.Yposition][self.Xposition] == "E":  # E for ether
            pockets.append("ether")
        else:
            pass

    def vertical_movement(
        self,
        labyrinth,
        virgin_labyrinth,
        Xposition, Yposition,
        move,
    ):
        Y_before_move = self.Yposition
        if move == "z":
            if labyrinth.maze[self.Yposition - 1][self.Xposition] != 1:
                self.Yposition = self.Yposition - 1
            if labyrinth.maze[Y_before_move - 1][self.Xposition] == 1:
                CONST.messages.hit_wall()
        if move == "s":
            if labyrinth.maze[self.Yposition + 1][self.Xposition] != 1:
                self.Yposition = self.Yposition + 1
            if labyrinth.maze[Y_before_move + 1][self.Xposition] == 1:
                CONST.messages.hit_wall()
        self.pickup(labyrinth, self.Xposition, self.Yposition, self.pockets)
        labyrinth.maze[Y_before_move][self.Xposition] = virgin_labyrinth.maze[
            Y_before_move
        ][self.Xposition]
        labyrinth.maze[self.Yposition][self.Xposition] = "M"
        print(*labyrinth.maze, sep="\n")
        print("Mc Gyver has in his pockets: {}".format(self.pockets))

    def horizontal_movement(
        self, labyrinth, virgin_labyrinth, Xposition, Yposition, move
    ):
        X_before_move = self.Xposition
        if move == "q":
            if labyrinth.maze[self.Yposition][self.Xposition - 1] != 1:
                self.Xposition = self.Xposition - 1
            if labyrinth.maze[self.Yposition][X_before_move - 1] == 1:
                CONST.messages.hit_wall()
        if move == "d":
            if labyrinth.maze[self.Yposition][self.Xposition + 1] != 1:
                self.Xposition = self.Xposition + 1
            if labyrinth.maze[self.Yposition][X_before_move + 1] == 1:
                CONST.messages.hit_wall()
        self.pickup(labyrinth, self.Xposition, self.Yposition, self.pockets)
        labyrinth.maze[self.Yposition][X_before_move] = virgin_labyrinth.maze[
            self.Yposition
        ][X_before_move]
        labyrinth.maze[self.Yposition][self.Xposition] = "M"
        print(*labyrinth.maze, sep="\n")
        print("Mc Gyver has in his pockets: {}".format(self.pockets))


def main():
    # creation of our labyrinth instance
    labyrinth = Labyrinth()
    print("\n labyrinth without items: ")
    print(*labyrinth.maze, sep="\n")
    print("")

    # creation of a copy of our labyrinth
    # it will be used to remember the type of the cell from which mcGyver moves
    labyrinth_copy = copy.deepcopy(labyrinth)

    # place the items in our labyrinth
    labyrinth.place_items()

    print("labyrinth with items:")
    print(*labyrinth.maze, sep="\n")
    print("")

    # creation of our character instance
    character = Mc_Gyver(labyrinth)

    # creation of our game window
    game_window = GameWindow()

    # creation of our labyrinth display
    maze_display = LabyrinthDisplay(labyrinth, game_window)
    # maze_display.display_maze(labyrinth)

    # get user input while the end of the maze is not reached
    while labyrinth.is_end_cell(character.Xposition, character.Yposition) != True:
        move = input(
            "please use the z,q,s,d keys of your keyboard to move Mc_Gyver ")
        print(
            "Mc Gyver comes from this position: {},{}".format(
                character.Xposition, character.Yposition
            )
        )

        if move == "z" or move == "s":
            character.vertical_movement(
                labyrinth,
                labyrinth_copy,
                character.Xposition,
                character.Yposition,
                move,
            )

        if move == "q" or move == "d":
            character.horizontal_movement(
                labyrinth,
                labyrinth_copy,
                character.Xposition,
                character.Yposition,
                move,
            )

        # in case user input is not one of the key allowed
        else:
            if move != "z" and move != "q" and move != "s" and move != "d":
                print("")
                print("\n you pressed the following invalid key: {} \n".format(move))
                print("")

        # feedback for the user
        print(
            "Mc Gyver arrived at this position: {},{}".format(
                character.Xposition, character.Yposition
            )
        )

    # chracter has reached the end of the maze, check the pockets to know if he won or loose
    if (
        "needle" in character.pockets
        and "tube" in character.pockets
        and "ether" in character.pockets
    ):
        CONST.messages.win()

    else:
        CONST.messages.loose()


pygame.init()
main()
pygame.quit()
