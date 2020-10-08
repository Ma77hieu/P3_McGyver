import pprint
import random
import copy
import time
import pygame
import constants as CONST


class Labyrinth:

    def __init__(self):
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

# used to check if character reached the end of the maze
    def is_end_cell(self, X, Y):
        if X == self.finish_X and Y == self.finish_Y:
            return True
        return False

    def place_items(self):
        # generate a random position for each item
        for component in CONST.item_type:
            item = Item(component, random.randint(
                0, CONST.maze_size-1), random.randint(0, CONST.maze_size-1))
            # make sure that item is not at the same position as start, finish or another item:
            while self.maze[item.Yposition][item.Xposition] != 0:
                item.Xposition = random.randint(0, CONST.maze_size-1)
                item.Yposition = random.randint(0, CONST.maze_size-1)
            self.maze[item.Yposition][item.Xposition] = item.item_name


class GameWindow:
    # define the general display of the game
    def __init__(self):
        self.game_screen = pygame.display.set_mode(
            (CONST.game_window_width, CONST.game_window_height))
        pygame.display.set_caption(CONST.game_window_title)
        self.game_screen.fill(CONST.maze_bg_color)
        self.mac = pygame.image.load(CONST.mac_path).convert_alpha()
        self.guard = pygame.image.load(CONST.guard_path).convert_alpha()
        self.needle = pygame.image.load(CONST.needle_path).convert_alpha()
        self.tube = pygame.image.load(CONST.tube_path).convert_alpha()
        self.ether = pygame.image.load(CONST.ether_path).convert_alpha()
        self.wall = pygame.image.load(CONST.wall_path).convert_alpha()
        self.blank = pygame.image.load(CONST.empty_path).convert_alpha()
        self.start = pygame.image.load(CONST.start_path).convert_alpha()


class Objects_Display:
    # create the zone to display the items in Mac's pockets
    def __init__(self, game_window, pictures, pockets=[]):
        objects_screen = pygame.Surface((
            CONST.width_objects_surface, CONST.height_objects_surface))
        objects_screen.fill(CONST.maze_bg_color)
        game_window.game_screen.blit(
            objects_screen, (CONST.HORIZONTAL_OFFSET, CONST.msg_screen_Y))
        font = pygame.font.Font('ressource/bahnschrift.ttf', 16)
        objects_text = font.render(
            'You have in your pockets:', True, CONST.black)
        game_window.game_screen.blit(
            objects_text, (CONST.HORIZONTAL_OFFSET+5, CONST.txt_Y))
        if pockets != []:
            for elem in range(len(pockets)):
                if pockets[elem] == "N" or pockets[elem] == "T" or pockets[elem] == "E":
                    game_window.game_screen.blit(
                        pictures.images[pockets[elem]], (CONST.HORIZONTAL_OFFSET+elem*CONST.CELL_WIDTH, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*3))
                    pygame.display.flip()


class Messages_Display:
    # display messages to the user to know what's happening
    def __init__(self, game_window, userfeedback):
        messages_screen = pygame.Surface((
            CONST.width_objects_surface, CONST.height_objects_surface))
        game_window.game_screen.blit(
            messages_screen, (CONST.msg_screen_X, CONST.msg_screen_Y))
        font = pygame.font.Font('ressource/bahnschrift.ttf', 16)
        if userfeedback in CONST.possible_user_feedbacks:
            messages_screen.fill(CONST.bg_color_feedbacks[userfeedback])
            game_window.game_screen.blit(
                messages_screen, (CONST.msg_screen_X, CONST.msg_screen_Y))
            objects_text = font.render(
                CONST.txt_user_feedbacks[userfeedback], True, CONST.txt_color_feedbacks[userfeedback])
            game_window.game_screen.blit(
                objects_text, (CONST.txt_X, CONST.txt_Y))

        pygame.display.flip()


class LabyrinthDisplay():
    # Display the labyriinth inside the game window
    def __init__(self, labyrinth, game_window, pictures):
        self.game_window = game_window
        for row in range(0, CONST.maze_size):
            for column in range(0, CONST.maze_size):
                game_window.game_screen.blit(
                    pictures.images[labyrinth.maze[row][column]], (CONST.HORIZONTAL_OFFSET+column*CONST.CELL_HEIGHT, row*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
                pygame.display.flip()

    # Update the labyrinth when Mac moves without reloading the whole maze
    def update_Display(labyrinth, game_window, X, Y, X_before, Y_before, pictures):
        game_window.game_screen.blit(
            pictures.images[labyrinth.maze[Y_before][X_before]], (CONST.HORIZONTAL_OFFSET+X_before*CONST.CELL_HEIGHT, Y_before*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
        pygame.display.flip()
        game_window.game_screen.blit(
            pictures.images[labyrinth.maze[Y][X]], (CONST.HORIZONTAL_OFFSET+X*CONST.CELL_HEIGHT, Y*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
        pygame.display.flip()


class Images():
    # Link the images to the letters inside the labyrinth
    def __init__(self, game_window):
        self.images = {"M": game_window.mac,
                       "N": game_window.needle,
                       "E": game_window.ether,
                       "T": game_window.tube,
                       "F": game_window.guard,
                       1: game_window.wall,
                       0: game_window.blank,
                       "S": game_window.start
                       }


class Item:
    def __init__(self, item_name, Xposition, Yposition):
        self.item_name = item_name
        self.Xposition = Xposition
        self.Yposition = Yposition


class Mc_Gyver:
    def __init__(self, labyrinth, game_window, pictures):
        self.Xposition = Xposition = CONST.start_X
        self.Yposition = Yposition = CONST.start_Y
        self.pockets = pockets = []
        self.game_window = game_window
        self.pictures = pictures

    # Used to check if Maxc is on a cell with an item
    def pickup(self, labyrinth, Xposition, Yposition, pockets):
        if labyrinth.maze[self.Yposition][self.Xposition] in CONST.item_type:
            pockets.append(labyrinth.maze[self.Yposition][self.Xposition])
            userfeedback = 'pickup'
            display_message = Messages_Display(
                self.game_window, userfeedback)
        else:
            pass

    def vertical_movement(
        self,
        labyrinth,
        virgin_labyrinth,
        Xposition, Yposition,
        event,
        pictures
    ):
        # Keep the starting position of mac to reinitialize the maze's cell after he moves
        Y_before_move = self.Yposition
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            # Check if movement is possible, update  (or not) Mac's position
            if labyrinth.maze[self.Yposition - 1][self.Xposition] != 1:
                self.Yposition = self.Yposition - 1
                userfeedback = 0
            if labyrinth.maze[Y_before_move - 1][self.Xposition] == 1:
                # CONST.messages.hit_wall()
                userfeedback = 'collision'
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            if labyrinth.maze[self.Yposition + 1][self.Xposition] != 1:
                self.Yposition = self.Yposition + 1
                userfeedback = 0
            if labyrinth.maze[Y_before_move + 1][self.Xposition] == 1:
                # CONST.messages.hit_wall()
                userfeedback = 'collision'
        # Visual feedback in case of collision
        display_message = Messages_Display(self.game_window, userfeedback)
        self.pickup(labyrinth, self.Xposition, self.Yposition, self.pockets)
        # Re-initialize the cell from which Mac moved
        labyrinth.maze[Y_before_move][self.Xposition] = virgin_labyrinth.maze[
            Y_before_move
        ][self.Xposition]
        # Update Mac's position in the maze
        labyrinth.maze[self.Yposition][self.Xposition] = "M"
        # print("labyrinth after movement:")
        # print(*labyrinth.maze, sep="\n")
        # print("Mc Gyver has in his pockets: {}".format(self.pockets))

        # Update the Labyrinth display
        maze_display_update = LabyrinthDisplay.update_Display(
            labyrinth, self.game_window, self.Xposition, self.Yposition, self.Xposition, Y_before_move, pictures)

    def horizontal_movement(
        self, labyrinth, virgin_labyrinth, Xposition, Yposition, event, pictures
    ):
        X_before_move = self.Xposition

        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            if labyrinth.maze[self.Yposition][self.Xposition - 1] != 1:
                self.Xposition = self.Xposition - 1
                userfeedback = 0
            if labyrinth.maze[self.Yposition][X_before_move - 1] == 1:
                # CONST.messages.hit_wall()
                userfeedback = 'collision'
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            if labyrinth.maze[self.Yposition][self.Xposition + 1] != 1:
                self.Xposition = self.Xposition + 1
                userfeedback = 0
            if labyrinth.maze[self.Yposition][X_before_move + 1] == 1:
                # CONST.messages.hit_wall()
                userfeedback = 'collision'
        display_message = Messages_Display(self.game_window, userfeedback)
        self.pickup(labyrinth, self.Xposition, self.Yposition, self.pockets)
        labyrinth.maze[self.Yposition][X_before_move] = virgin_labyrinth.maze[
            self.Yposition
        ][X_before_move]
        labyrinth.maze[self.Yposition][self.Xposition] = "M"
        # print("labyrinth after movement:")
        # print(*labyrinth.maze, sep="\n")
        # print("Mc Gyver has in his pockets: {}".format(self.pockets))
        maze_display_update = LabyrinthDisplay.update_Display(
            labyrinth, self.game_window, self.Xposition, self.Yposition, X_before_move, self.Yposition, pictures)


def main():
    # Creation of our labyrinth instance
    labyrinth = Labyrinth()
    print("\n labyrinth without items: ")
    print(*labyrinth.maze, sep="\n")
    print("")

    # Creation of a copy of our labyrinth
    # it will be used to remember the type of the cell from which mcGyver moves
    labyrinth_copy = copy.deepcopy(labyrinth)

    # Place the items in our labyrinth
    labyrinth.place_items()

    # print("labyrinth with items:")
    # print(*labyrinth.maze, sep="\n")
    # print("")

    # Creation of the overall game window
    game_window = GameWindow()
    print(game_window.mac)

    # Loading of our dictionnary linking maze letters to the right images for pygame
    pictures = Images(game_window)

    # creation of our character instance
    character = Mc_Gyver(labyrinth, game_window, pictures)

    # Display of our objects inside the game window
    display_objects = Objects_Display(game_window, pictures, character.pockets)

    # Creation of our labyrinth display inside the game window
    maze_display = LabyrinthDisplay(labyrinth, game_window, pictures)
    # maze_display.display_maze(labyrinth)

    # Definition of a variable to know when to end the game
    game_on_going = True
    while game_on_going:

        for event in pygame.event.get():
            # Setup two ways for ending the game: click the red cross or escape key
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game_on_going = 0
            elif event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                character.vertical_movement(
                    labyrinth,
                    labyrinth_copy,
                    character.Xposition,
                    character.Yposition,
                    event,
                    pictures
                )
            elif event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                character.horizontal_movement(
                    labyrinth,
                    labyrinth_copy,
                    character.Xposition,
                    character.Yposition,
                    event,
                    pictures
                )
            # Give feedback to the user if the key pressed is not accepted
            elif event.type == pygame.KEYDOWN and event.key not in CONST.OK_user_inputs:
                userfeedback = 'invalid'
                display_message = Messages_Display(
                    game_window, userfeedback)
            pockets_display = Objects_Display(
                game_window, pictures, character.pockets)

            # Check if Mac reached the end of the maze
            if labyrinth.is_end_cell(character.Xposition, character.Yposition) == True:
                # Mac has all required items = player wins
                if ("N" in character.pockets and "T" in character.pockets and "E" in character.pockets):
                    userfeedback = 'win'
                    display_message = Messages_Display(
                        game_window, userfeedback)
                    time.sleep(2)
                    game_on_going = 0
                # Mac does not have all required items = player looses
                else:
                    userfeedback = 'loose'
                    display_message = Messages_Display(
                        game_window, userfeedback)
                    time.sleep(2)
                    game_on_going = 0


pygame.init()
main()
pygame.quit()
