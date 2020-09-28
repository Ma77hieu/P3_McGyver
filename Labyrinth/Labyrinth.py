import pprint
import random
import copy
import time


class Labyrinth_zone:
    def __init__(self, Xposition, Yposition, zone_type):
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.type = zone_type


class Labyrinth:
    start_X = 0
    start_Y = 3
    finish_X = 14
    finish_Y = 12

    def __init__(
        self,
        Xposition=0,
        Yposition=0,
        sorted_maze=[],
        start_X=0,
        start_Y=3,
        finish_X=14,
        finish_Y=12,
    ):
        self.Xposition = Xposition
        self.Yposition = Yposition

        source_file = open(
            "C:/Users/matthieu/GitHub/P3_McGyver/Labyrinth/labyrinth.txt", "r"
        )
        sorted_maze = []
        all_cells = source_file.read()
        all_cells = all_cells.split(",")
        for row in range(15):
            line_cell = []
            for column in range(15):
                line_cell.append(int(all_cells[column + row * 15]))
            sorted_maze.append(line_cell)
        # print("maze from the txt file: ")
        # print(*sorted_maze, sep="\n")
        self.maze = sorted_maze

        def place_start_finish(self, start_X, start_Y, finish_X, finish_Y):
            self.maze[start_Y][start_X] = "S"
            self.maze[finish_Y][finish_X] = "F"

        place_start_finish(self, start_X, start_Y, finish_X, finish_Y)

    def is_end_cell(self, X, Y, finish_X=14, finish_Y=12):
        if X == finish_X and Y == finish_Y:
            return True
        return False

    def place_items(self):
        item_type = ["N", "E", "T"]  # N for needle, T for tube and E for ether
        # place the items in the maze
        for component in item_type:
            item = Item(component, random.randint(0, 14), random.randint(0, 14))
            # print(
            #     "{} initally randomly placed in {} {} corresponding to this maze type: {}".format(
            #         item.item_name,
            #         item.Xposition,
            #         item.Yposition,
            #         labyrinth.maze[item.Yposition][item.Xposition],
            #     )
            # )
            # make sure that item is not at the same position as start, finish or another item
            while self.maze[item.Yposition][item.Xposition] != 0:
                # print("need to find a new place for the item")
                item.Xposition = random.randint(0, 14)
                item.Yposition = random.randint(0, 14)
            # print(
            #     "the item {} is placed here: {} {}".format(
            #         item.item_name, item.Xposition, item.Yposition
            #     )
            # )
            self.maze[item.Yposition][item.Xposition] = item.item_name


class messages:
    def hit_wall():
        print("\n you hit a wall\n")

    def suspense():
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("....")

    def win():
        print("\nYou reach the exit of the maze")
        messages.suspense()
        print(
            "Damned, this guard looks really in shape... How could you pass through him?"
        )
        messages.suspense()
        print(
            "You take the needle, the tube and the ether you previously found in the maze and assemble them to make a tranquilizer"
        )
        messages.suspense()
        print(
            "You jump on the guard, inject him the ether and wait a few seconds, he falls on the floor, this is your chance!"
        )
        messages.suspense()
        print(
            "You run towards the exit, pass the door and that's it, tyou can feel a nice warm breeze on your cheeks"
        )
        messages.suspense()
        print("CONGRATULATIONS You've won")

    def loose():
        print(
            "\nYou reach the exit but you do not have all the elements to craft your tranquilizer"
        )
        messages.suspense()
        print("You try to tell the guard the best joke you know but...")
        messages.suspense()
        print("he looks at you with no pity and hits you with his tazer.")
        messages.suspense()
        print("you lost")
        print("  _____")
        print(" /     \ ")
        print("| () () |")
        print(" \  ^  / ")
        print("  ||||| ")
        print("  ||||| ")


class Item:
    def __init__(self, item_name, Xposition, Yposition):
        self.item_name = item_name
        self.Xposition = Xposition
        self.Yposition = Yposition


class Mc_Gyver:
    def __init__(self, labyrinth, Xposition=0, Yposition=3, pockets=[]):
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.pockets = pockets

    def pickup(self, labyrinth, Xposition, Yposition, pockets=[]):
        if labyrinth.maze[Yposition][Xposition] == "N":  # N for needle
            pockets.append("needle")
        if labyrinth.maze[Yposition][Xposition] == "T":  # T for tube
            pockets.append("tube")
        if labyrinth.maze[Yposition][Xposition] == "E":  # E for ether
            pockets.append("ether")
        else:
            pass

    def vertical_movement(
        self,
        labyrinth,
        virgin_labyrinth,
        Xposition,
        Yposition,
        move,
    ):
        Y_before_move = self.Yposition
        if move == "z":
            if labyrinth.maze[self.Yposition - 1][self.Xposition] != 1:
                self.Yposition = self.Yposition - 1
            if labyrinth.maze[Y_before_move - 1][self.Xposition] == 1:
                messages.hit_wall()
        if move == "s":
            if labyrinth.maze[self.Yposition + 1][self.Xposition] != 1:
                self.Yposition = self.Yposition + 1
            if labyrinth.maze[Y_before_move + 1][self.Xposition] == 1:
                messages.hit_wall()
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
                messages.hit_wall()
        if move == "d":
            if labyrinth.maze[self.Yposition][self.Xposition + 1] != 1:
                self.Xposition = self.Xposition + 1
            if labyrinth.maze[self.Yposition][X_before_move + 1] == 1:
                messages.hit_wall()
        self.pickup(labyrinth, self.Xposition, self.Yposition, self.pockets)
        labyrinth.maze[self.Yposition][X_before_move] = virgin_labyrinth.maze[
            self.Yposition
        ][X_before_move]
        labyrinth.maze[self.Yposition][self.Xposition] = "M"
        print(*labyrinth.maze, sep="\n")
        print("Mc Gyver has in his pockets: {}".format(self.pockets))

    # def move_up(self, Yposition):
    #     self.Yposition = Yposition - 1

    # def move_down(self, Yposition):
    #     self.Yposition = Yposition + 1

    # def move_left(self, Xposition):
    #     self.Xposition = Xposition - 1

    # def move_right(self, Xposition):
    #     self.Xposition = Xposition + 1


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

    # get user inpuut while the end of the maze is not reached
    while labyrinth.is_end_cell(character.Xposition, character.Yposition) != True:
        move = input("please use the z,q,s,d keys of your keyboard to move Mc_Gyver ")
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
        messages.win()

    else:
        messages.loose()


main()