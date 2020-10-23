from main_program.parameters.constants import Constants as CONST
from main_program.game_objects.objects import Item as Item
import random


class Labyrinth:
    """This is the maze imported from the Labyrinth.txt file"""

    def __init__(self):
        source_file = open(CONST.maze_path, "r")
        sorted_maze = []
        all_cells = source_file.read()
        all_cells = all_cells.split(",\n")
        for row in range(CONST.maze_size):
            maze_line = []
            new_line = all_cells[row].split(",")
            for i in range(len(new_line)):
                new_line[i] = int(new_line[i])
            maze_line.append(new_line)
            sorted_maze.extend(maze_line)
        self.maze = sorted_maze
        self.maze[CONST.start_Y][CONST.start_X] = "S"
        self.maze[CONST.finish_Y][CONST.finish_X] = "F"

    def is_end(self, X, Y):
        """Used to check if the character reached the end of the maze"""
        if X == CONST.finish_X and Y == CONST.finish_Y:
            return True
        return False

    def place_items(self):
        """ Generates a random position for each item"""
        for component in CONST.item_type:
            item = Item(component, random.randint(
                0, CONST.maze_size-1), random.randint(0, CONST.maze_size-1))
            # make sure that item is not at the same position as :
            # start, finish or another item
            while self.maze[item.Yposition][item.Xposition] != 0:
                item.Xposition = random.randint(0, CONST.maze_size-1)
                item.Yposition = random.randint(0, CONST.maze_size-1)
            self.maze[item.Yposition][item.Xposition] = item.item_name
