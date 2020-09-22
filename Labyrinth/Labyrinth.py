import pprint
import random
import copy
import time

zone_type = [0, 1]  # 0 means path, 1 means wall
labyrinth = []
row = []
Xposition = 0
Yposition = 0

# create our Labyrinth_zone class
class Labyrinth_zone:
    def __init__(self, Xposition, Yposition):
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.type = random.choice(zone_type)


"""MAZE GENERATOR

#ask to our user the size of grid they want
grid_size = int(input("Veuillez saisir la taille du labyrinthe  "))

# create the overall grid without start and end
for Yposition in range(grid_size):
    print("", "Maze's creation on going:{}".format(labyrinth), "", sep="\n")
    for Xposition in range(grid_size):
        zone = Labyrinth_zone(Xposition, Yposition)
        row.append(zone.type)
        print("Line's creation on going: {}".format(row))
    labyrinth.append(row)
    row = []

print("", "Maze without start/end: {}".format(labyrinth), "", sep="\n")

# generate the coordinates of our start and end
start_X_position = random.randint(0, grid_size - 1)
start_Y_position = random.randint(0, grid_size - 1)
end_X_position = random.randint(0, grid_size - 1)
end_Y_position = random.randint(0, grid_size - 1)
print(
    "the START of our maze is at the {} line and {} column".format(
        start_Y_position + 1, start_X_position + 1
    )
)
print(
    "the END of our maze is at the {} line and {} column".format(
        end_Y_position + 1, end_X_position + 1
    )
)

# give the "start" and "end" type to the corresponding cells
start = Labyrinth_zone(start_X_position, start_Y_position)
start.type = "START"
end = Labyrinth_zone(end_X_position, end_Y_position)
end.type = "END"

# override the type of start and end cells
labyrinth[start_Y_position][start_X_position] = "START"
labyrinth[end_Y_position][end_X_position] = "END"

# display our result
print("")
print("Final version of auto generated maze:")
# pprint.pprint(labyrinth)
# print(*labyrinth, sep="],")
print(*labyrinth, sep="\n")
"""
# fixed labyrinth

labyrinth2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    ["S", 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, "F"],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

print("")
print("Hardcoded labyrinth:")
pprint.pprint(labyrinth2)

# creation of a copy of our labyrinth
# it will be used to remember the type of the cell from which mcGyver moves
labyrinth3 = copy.deepcopy(labyrinth2)

""" ITEM PART"""

# store the coordinates of our start and end
start_X_position = 0
start_Y_position = 3
end_X_position = 14
end_Y_position = 12

# define the item class
item_type = ["N", "E", "T"]


class Item:
    def __init__(self, item_name):
        self.item_name = item_name
        self.Xposition = Xposition
        self.Yposition = Yposition


# place the items in the maze
for component in item_type:
    item = Item(component)
    item.Xposition = random.randint(
        0, 14
    )  # in case of variuable grid use grid_size - 1
    item.Yposition = random.randint(
        0, 14
    )  # in case of variuable grid use grid_size - 1
    print(
        "{} initally randomly placed in {} {} corresponding to this maze type: {}".format(
            item.item_name,
            item.Xposition,
            item.Yposition,
            labyrinth2[item.Yposition][item.Xposition],
        )
    )
    while labyrinth2[item.Yposition][item.Xposition] != 0:
        print("need to find a new place for the item")
        item.Xposition = random.randint(
            0, 14
        )  # in case of variuable grid use grid_size - 1
        item.Yposition = random.randint(
            0, 14
        )  # in case of variuable grid use grid_size - 1
    print(
        "the item {} is placed here: {} {}".format(
            item.item_name, item.Xposition, item.Yposition
        )
    )
    labyrinth2[item.Yposition][item.Xposition] = item.item_name

print(*labyrinth2, sep="\n")


""" MCGYVER PART"""
pockets = []


class Mc_Gyver:
    def __init__(self, Xposition, Yposition):
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

    def pickup(self, Xposition, Yposition):
        if labyrinth2[Yposition][Xposition] == "N":  # N for needle
            pockets.append("needle")
        if labyrinth2[Yposition][Xposition] == "T":  # T for tube
            pockets.append("tube")
        if labyrinth2[Yposition][Xposition] == "E":  # E for ether
            pockets.append("ether")
        else:
            pass


character = Mc_Gyver(0, 3)
print(
    "let's make sure Mc Gyver is at the entrance: {} {}".format(
        character.Xposition, character.Yposition
    )
)


def is_end_cell(X, Y):
    if X == end_X_position:
        if Y == end_Y_position:
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
    if move == "z":
        Y_before_move = character.Yposition
        if labyrinth2[character.Yposition - 1][character.Xposition] != 1:
            character.move_up(character.Yposition)
            character.pickup(character.Xposition, character.Yposition)
            labyrinth2[character.Yposition][
                character.Xposition
            ] = "M"  # M indicates Mc_Gyver position
            if labyrinth3[Y_before_move][character.Xposition] == "T" or "E" or "N":
                labyrinth2[Y_before_move][character.Xposition] = 0
            else:
                labyrinth2[Y_before_move][character.Xposition] = labyrinth3[
                    Y_before_move
                ][character.Xposition]
            print(*labyrinth2, sep="\n")
            print("Mc Gyver has in his pockets: {}".format(pockets))

        if labyrinth2[Y_before_move - 1][character.Xposition] == 1:
            print("")
            print("you hit a wall")
            print("")

    if move == "s":
        Y_before_move = character.Yposition
        if labyrinth2[character.Yposition + 1][character.Xposition] != 1:
            character.move_down(character.Yposition)
            character.pickup(character.Xposition, character.Yposition)
            labyrinth2[character.Yposition][character.Xposition] = "M"
            labyrinth2[Y_before_move][character.Xposition] = labyrinth3[Y_before_move][
                character.Xposition
            ]
            print(*labyrinth2, sep="\n")
            print("Mc Gyver has in his pockets: {}".format(pockets))

        if labyrinth2[Y_before_move + 1][character.Xposition] == 1:
            print("")
            print("you hit a wall")
            print("")

    if move == "q":
        X_before_move = character.Xposition
        if labyrinth2[character.Yposition][character.Xposition - 1] != 1:
            character.move_left(character.Xposition)
            character.pickup(character.Xposition, character.Yposition)
            labyrinth2[character.Yposition][character.Xposition] = "M"
            labyrinth2[character.Yposition][X_before_move] = labyrinth3[
                character.Yposition
            ][X_before_move]
            print(*labyrinth2, sep="\n")
            print("Mc Gyver has in his pockets: {}".format(pockets))

        if labyrinth2[character.Yposition][X_before_move - 1] == 1:
            print("")
            print("you hit a wall")
            print("")

    if move == "d":
        X_before_move = character.Xposition
        if labyrinth2[character.Yposition][character.Xposition + 1] != 1:
            # print("X_before_move:{}".format(X_before_move))
            # print(
            #     "you are trying to move to a cell with the following type: {}".format(
            #         labyrinth2[character.Yposition][character.Xposition + 1]
            #     )
            # )
            character.move_right(character.Xposition)
            character.pickup(character.Xposition, character.Yposition)
            labyrinth2[character.Yposition][character.Xposition] = "M"
            labyrinth2[character.Yposition][X_before_move] = labyrinth3[
                character.Yposition
            ][X_before_move]

            # print(
            #     "labyrinth3 position depart {}".format(
            #         labyrinth3[character.Yposition][X_before_move]
            #     )
            # )
            print(*labyrinth2, sep="\n")
            print("Mc Gyver has in his pockets: {}".format(pockets))

        if labyrinth2[character.Yposition][X_before_move + 1] == 1:
            print("")
            print("you hit a wall")
            print("")

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
    time.sleep(0.3)
    print("..")
    time.sleep(0.3)
    print("...")
    time.sleep(0.3)
    print("....")
    time.sleep(0.3)
    print(".....")


print("you reach the exit and have iun your pockets: {}".format(pockets))
if "needle" in pockets:
    print("you have a needle")
if "tube" in pockets:
    print("you have a tube")
if "ether" in pockets:
    print("you have ether")

if "needle" in pockets and "tube" in pockets and "ether" in pockets:
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
