import pprint
import random

""" 1/Define the Labyrinth_zone class
2/Define the start position
3/Define the end position
4/Define the type of all the other cells:
- path
- wall
5/Three items are randomly placed on path cells
"""

zone_type = [0, 1]  # 0 means path, 1 means wall
Xposition = 0
Yposition = 0
labyrinth = []
row = []
grid_size = int(input("Veuillez saisir la taille du labyrinthe"))

# create our Labyrinth_zone class
class Labyrinth_zone:
    def __init__(self, Xposition, Yposition):
        self.Xposition = Xposition
        self.Yposition = Yposition
        self.type = random.choice(zone_type)


# generate the coordinates of our start and end
start_X_position = random.randint(0, grid_size - 1)
start_Y_position = random.randint(0, grid_size - 1)
end_X_position = random.randint(0, grid_size - 1)
end_Y_position = random.randint(0, grid_size - 1)
print(
    "the START of our maze is at position {},{}".format(
        start_X_position, start_Y_position
    )
)
print("the END of our maze is at position {},{}".format(end_X_position, end_Y_position))

# give the "start" and "end" type to the corresponding cells
start = Labyrinth_zone(start_X_position, start_Y_position)
start.type = "START"
end = Labyrinth_zone(end_X_position, end_Y_position)
end.type = "END"


# create the overall grid
for Yposition in range(grid_size):
    print("LAB:{}".format(labyrinth))
    for Xposition in range(grid_size):
        zone = Labyrinth_zone(Xposition, Yposition)
        row.append(zone.type)
        print("ligne crée: {}".format(row))
    labyrinth.append(row)
    row = []

print("LAB post boucle for: {}".format(labyrinth))

# override the type of start and end cells
labyrinth[start_Y_position][start_X_position] = "START"
labyrinth[end_Y_position][end_X_position] = "END"

# display our result
print("")
print("Labyrinthe version finale:")
pprint.pprint(labyrinth)

"""    
zone11 = Labyrinth_zone(1, 1)
print(zone11.type)"""


"""
grid_size = 15

for zone in range(grid_size):
    

print(labyrinth)"""
