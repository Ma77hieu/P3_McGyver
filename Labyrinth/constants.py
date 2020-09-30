import time

start_X=0
start_Y=3
finish_X=14
finish_Y=12
maze_path="C:/Users/matthieu/GitHub/P3_McGyver/Labyrinth/labyrinth.txt"
maze_size=15
item_type = ["N", "E", "T"]  # N for needle, T for tube and E for ether

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
