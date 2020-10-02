import time


start_X = 0
start_Y = 3
finish_X = 14
finish_Y = 12
maze_path = "C:/Users/matthieu/GitHub/P3_McGyver/Labyrinth/labyrinth.txt"
maze_size = 15
item_type = ["N", "E", "T"]  # N for needle, T for tube and E for ether

maze_bg_color = (244, 244, 239)
game_window_width = 1000
game_window_height = 1000
game_window_title = "Escape the maze or be DOOMED"

LINE_WIDTH = 4
VERTICAL_OFFSET = 50
HORIZONTAL_OFFSET = 120
CELL_WIDTH = 50
CELL_HEIGHT = 50
NBR_X_CELL = 15
NBR_Y_CELL = 15
WIDTH_LABYRINTH = NBR_Y_CELL*CELL_HEIGHT+(NBR_X_CELL)*LINE_WIDTH
HEIGHT_LABYRINTH = NBR_Y_CELL*CELL_HEIGHT+(NBR_Y_CELL)*LINE_WIDTH

# path_mac=
# path_guard=
# path_needle=
# path_tube=
# path_ether=


# images = {"M": "C:/Users/matthieu/GitHub/P3_McGyver/resource/MacGyver50px.png",
#           "N": "C:/Users/matthieu/GitHub/P3_McGyver/resource/aiguille50px.png",
#           "E": "C:/Users/matthieu/GitHub/P3_McGyver/resource/ether50px.png",
#           "T": "C:/Users/matthieu/GitHub/P3_McGyver/resource/tube50px.png",
#           "F": "C:/Users/matthieu/GitHub/P3_McGyver/resource/Gardien50px.png",
#           1: "C:/Users/matthieu/GitHub/P3_McGyver/resource/wall.png"
#           }


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
