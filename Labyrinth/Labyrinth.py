import pprint
import random

zone_type = [0, 1]  # 0 means path, 1 means wall
labyrinth = []
row = []
grid_size = int(input("Veuillez saisir la taille du labyrinthe  "))

# create our Labyrinth_zone class
class Labyrinth_zone:
    def __init__(self, Xposition, Yposition):
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.type = random.choice(zone_type)


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

# fixed labyrinth

labyrinth2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    ["START", 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, "END"],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

print("")
print("Hardcoded labyrinth:")
pprint.pprint(labyrinth2)


""" ITEM PART"""


# define the item class
item_type = ["needle", "ether", "tube"]


class Item:
    def __init__(self, item_name):
        self.item_name = item_name
        self.Xposition = Xposition
        self.Yposition = Yposition


# place the items in the maze
for component in item_type:
    item = Item(component)
    item.Xposition = random.randint(0, grid_size - 1)
    item.Yposition = random.randint(0, grid_size - 1)
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
        item.Xposition = random.randint(0, grid_size - 1)
        item.Yposition = random.randint(0, grid_size - 1)
    print(
        "the item {} is placed here: {} {}".format(
            item.item_name, item.Xposition, item.Yposition
        )
    )
    labyrinth2[item.Yposition][item.Xposition] = item.item_name

print(*labyrinth2, sep="\n")


""" MCGYVER PART"""

"""
class Mc_Gyver:
    def __init__(self, Xposition, Yposition):
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.pockets = pockets

    def move_up(self):
        self.Yposition = Yposition - 1


input("utilisez les ")
"""