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
    def __init__(self, Xposition=0, Yposition=0, sorted_maze=[]):
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
        print("maze from the txt file: ")
        print(*sorted_maze, sep="\n")
        self.maze = sorted_maze

        def place_start_finish(self):
            self.maze[3][0] = "S"
            self.maze[12][14] = "F"

        place_start_finish(self)


labyrinth2 = Labyrinth()

print("labyrinth2: ")
print(*labyrinth2.maze, sep="\n")

# start = Labyrinth_zone(0, 3, "S")
# finish = Labyrinth_zone(12, 14, "F")

row = []
Xposition = 0
Yposition = 0

# creation of a copy of our labyrinth
# it will be used to remember the type of the cell from which mcGyver moves
labyrinth3 = copy.deepcopy(labyrinth2)


""" PLACE ITEM IN THE MAZE"""

# store the coordinates of our start and end
start_X_position = 0
start_Y_position = 3
end_X_position = 14
end_Y_position = 12

# define the item class
item_type = ["N", "E", "T"]  # N for needle, T for tube and E for ether


class Item:
    def __init__(self, item_name):
        self.item_name = item_name
        self.Xposition = Xposition
        self.Yposition = Yposition


# place the items in the maze
for component in item_type:
    item = Item(component)
    item.Xposition = random.randint(0, 14)
    item.Yposition = random.randint(0, 14)
    print(
        "{} initally randomly placed in {} {} corresponding to this maze type: {}".format(
            item.item_name,
            item.Xposition,
            item.Yposition,
            labyrinth2.maze[item.Yposition][item.Xposition],
        )
    )
    # make sure that item is not at the same position as start, finish or another item
    while labyrinth2.maze[item.Yposition][item.Xposition] != 0:
        print("need to find a new place for the item")
        item.Xposition = random.randint(0, 14)
        item.Yposition = random.randint(0, 14)
    print(
        "the item {} is placed here: {} {}".format(
            item.item_name, item.Xposition, item.Yposition
        )
    )
    labyrinth2.maze[item.Yposition][item.Xposition] = item.item_name

print(*labyrinth2.maze, sep="\n")


""" MCGYVER PART"""


def wall_hit():
    print("\n you hit a wall")


class Mc_Gyver:
    def __init__(self, Xposition, Yposition, pockets=[]):
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.pockets = pockets

    def move_up(self, Yposition):
        self.Yposition = Yposition - 1

    def move_down(self, Yposition):
        self.Yposition = Yposition + 1

    def move_left(self, Xposition):
        self.Xposition = Xposition - 1

    def move_right(self, Xposition):
        self.Xposition = Xposition + 1

    def pickup(self, Xposition, Yposition, pockets=[]):
        if labyrinth2.maze[Yposition][Xposition] == "N":  # N for needle
            pockets.append("needle")
        if labyrinth2.maze[Yposition][Xposition] == "T":  # T for tube
            pockets.append("tube")
        if labyrinth2.maze[Yposition][Xposition] == "E":  # E for ether
            pockets.append("ether")
        else:
            pass

    # def vertical_move(self, move):
    #     Y_before_move = character.Yposition
    #     if move == "z":
    #         if labyrinth2[character.Yposition - 1][character.Xposition] != 1:
    #             character.move_up(character.Yposition)
    #         if labyrinth2[Y_before_move - 1][character.Xposition] == 1:
    #             wall_hit()
    #     if move == "s":
    #         if labyrinth2[character.Yposition + 1][character.Xposition] != 1:
    #             character.move_down(character.Yposition)
    #         if labyrinth2[Y_before_move + 1][character.Xposition] == 1:
    #             wall_hit()
    #     character.pickup(character.Xposition, character.Yposition)
    #     labyrinth2[character.Yposition][character.Xposition] = "M"
    #     labyrinth2[Y_before_move][character.Xposition] = labyrinth3[Y_before_move][
    #         character.Xposition
    #     ]
    #     print(*labyrinth2, sep="\n")
    #     print("Mc Gyver has in his pockets: {}".format(pockets))

    #     def horizontal_move(self, move):
    #         X_before_move = character.Xposition
    #         if move == "q":
    #             if labyrinth2[character.Yposition][character.Xposition - 1] != 1:
    #                 character.move_left(character.Yposition)
    #             if labyrinth2[character.Yposition][X_before_move - 1] == 1:
    #                 wall_hit()
    #         if move == "d":
    #             if labyrinth2[character.Yposition][character.Xposition + 1] != 1:
    #                 character.move_right(character.Yposition)
    #             if labyrinth2[character.Yposition][X_before_move + 1] == 1:
    #                 wall_hit()
    #         character.pickup(character.Xposition, character.Yposition)
    #         labyrinth2[character.Yposition][character.Xposition] = "M"
    #         labyrinth2[character.Yposition][X_before_move] = labyrinth3[
    #             character.Yposition
    #         ][X_before_move]
    #         print(*labyrinth2, sep="\n")
    #         print("Mc Gyver has in his pockets: {}".format(pockets))


character = Mc_Gyver(0, 3)
"""for debug purposes
print(
    "let's make sure Mc Gyver is at the entrance: {} {}".format(
        character.Xposition, character.Yposition
    )
)"""


def is_end_cell(X, Y):
    if X == end_X_position and Y == end_Y_position:
        return True
    return False


# while character.Xposition != end_X_position and character.Yposition != end_Y_position:
while is_end_cell(character.Xposition, character.Yposition) != True:
    move = input("please use the z,q,s,d keys of your keyboard to move Mc_Gyver ")
    print(
        "Mc Gyver comes from this position: {},{}".format(
            character.Xposition, character.Yposition
        )
    )
    # if move == "z" or move == "s":
    #     if move == "z":
    #         Y_before_move = character.Yposition
    #         if labyrinth2[character.Yposition - 1][character.Xposition] != 1:
    #             character.move_up(character.Yposition)
    #         if labyrinth2[Y_before_move - 1][character.Xposition] == 1:
    #             wall_hit()
    #     if move == "s":
    #         if labyrinth2[character.Yposition + 1][character.Xposition] != 1:
    #             character.move_down(character.Yposition)
    #         if labyrinth2[Y_before_move + 1][character.Xposition] == 1:
    #             wall_hit()
    #         character.pickup(character.Xposition, character.Yposition)
    #         labyrinth2[character.Yposition][character.Xposition] = "M"
    #         labyrinth2[Y_before_move][character.Xposition] = labyrinth3[Y_before_move][character.Xposition]
    #         print(*labyrinth2, sep="\n")
    #         print("Mc Gyver has in his pockets: {}".format(pockets))
    # if move == "q" or move == "d":
    #         X_before_move = character.Xposition
    #         if move == "q":
    #             if labyrinth2[character.Yposition][character.Xposition - 1] != 1:
    #                 character.move_left(character.Yposition)
    #             if labyrinth2[character.Yposition][X_before_move - 1] == 1:
    #                 wall_hit()
    #         if move == "d":
    #             if labyrinth2[character.Yposition][character.Xposition + 1] != 1:
    #                 character.move_right(character.Yposition)
    #             if labyrinth2[character.Yposition][X_before_move + 1] == 1:
    #                 wall_hit()
    #         character.pickup(character.Xposition, character.Yposition)
    #         labyrinth2[character.Yposition][character.Xposition] = "M"
    #         labyrinth2[character.Yposition][X_before_move] = labyrinth3[character.Yposition][X_before_move]
    #         print(*labyrinth2, sep="\n")
    #         print("Mc Gyver has in his pockets: {}".format(pockets)

    # # beginning of working code, commented to try alternative code, do not erase
    if move == "z":
        Y_before_move = character.Yposition
        if labyrinth2.maze[character.Yposition - 1][character.Xposition] != 1:
            character.move_up(character.Yposition)
            character.pickup(
                character.Xposition, character.Yposition, character.pockets
            )
            labyrinth2.maze[character.Yposition][
                character.Xposition
            ] = "M"  # M indicates Mc_Gyver position
            labyrinth2.maze[Y_before_move][character.Xposition] = labyrinth3.maze[
                Y_before_move
            ][character.Xposition]
            print(*labyrinth2.maze, sep="\n")
            print("Mc Gyver has in his pockets: {}".format(character.pockets))

        else:
            wall_hit()

    if move == "s":
        Y_before_move = character.Yposition
        if labyrinth2.maze[character.Yposition + 1][character.Xposition] != 1:
            character.move_down(character.Yposition)
            character.pickup(
                character.Xposition, character.Yposition, character.pockets
            )
            labyrinth2.maze[character.Yposition][character.Xposition] = "M"
            labyrinth2.maze[Y_before_move][character.Xposition] = labyrinth3.maze[
                Y_before_move
            ][character.Xposition]
            print(*labyrinth2.maze, sep="\n")
            print("Mc Gyver has in his pockets: {}".format(character.pockets))

        else:
            wall_hit()

    if move == "q":
        X_before_move = character.Xposition
        if labyrinth2.maze[character.Yposition][character.Xposition - 1] != 1:
            character.move_left(character.Xposition)
            character.pickup(
                character.Xposition, character.Yposition, character.pockets
            )
            labyrinth2.maze[character.Yposition][character.Xposition] = "M"
            labyrinth2.maze[character.Yposition][X_before_move] = labyrinth3.maze[
                character.Yposition
            ][X_before_move]
            print(*labyrinth2.maze, sep="\n")
            print("Mc Gyver has in his pockets: {}".format(character.pockets))

        else:
            wall_hit()

    if move == "d":
        X_before_move = character.Xposition
        if labyrinth2.maze[character.Yposition][character.Xposition + 1] != 1:
            # print("X_before_move:{}".format(X_before_move))
            # print(
            #     "you are trying to move to a cell with the following type: {}".format(
            #         labyrinth2[character.Yposition][character.Xposition + 1]
            #     )
            # )
            character.move_right(character.Xposition)
            character.pickup(
                character.Xposition, character.Yposition, character.pockets
            )
            labyrinth2.maze[character.Yposition][character.Xposition] = "M"
            labyrinth2.maze[character.Yposition][X_before_move] = labyrinth3.maze[
                character.Yposition
            ][X_before_move]

            # print(
            #     "labyrinth3 position depart {}".format(
            #         labyrinth3[character.Yposition][X_before_move]
            #     )
            # )
            print(*labyrinth2.maze, sep="\n")
            print("Mc Gyver has in his pockets: {}".format(character.pockets))

        else:
            wall_hit()
            # end of working code, commented to try alternative code, do not erase

    else:
        if move != "z" and move != "q" and move != "s" and move != "d":
            print("")
            print("you pressed the following invalid key: {}".format(move))
            print("")

    print(
        "Mc Gyver arrived at this position: {},{}".format(
            character.Xposition, character.Yposition
        )
    )


def suspense():
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("....")


if (
    "needle" in character.pockets
    and "tube" in character.pockets
    and "ether" in character.pockets
):
    print("")
    print("You reach the exit of the maze")
    suspense()
    print("Damned, this guard looks really in shape... How could you pass through him?")
    suspense()
    print(
        "You take the needle, the tube and the ether you previously found in the maze and assemble them to make a tranquilizer"
    )
    suspense()
    print(
        "You jump on the guard, inject him the ether and wait a few seconds, he falls on the floor, this is your chance!"
    )
    suspense()
    print(
        "You run towards the exit, pass the door and that's it, tyou can feel a nice warm breeze on your cheeks"
    )
    suspense()
    print("CONGRATULATIONS You've won")
else:
    print(
        "You reach the exit but you do not have all the elements to craft your tranquilizer"
    )
    suspense()
    print("You try to tell the guard the best joke you know but...")
    suspense()
    print("he looks at you with no pity and hits you with his tazer.")
    suspense()
    print("you lost")
    print("  _____")
    print(" /     \ ")
    print("| () () |")
    print(" \  ^  / ")
    print("  ||||| ")
    print("  ||||| ")
