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
    # game_screen = game_screen
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
    blank = pygame.image.load("ressource/blank50px.png").convert_alpha()
    start = pygame.image.load("ressource/start50px.png").convert_alpha()


class Objects_Display:
    def __init__(self, game_window, pictures, pockets=[]):
        objects_screen = pygame.Surface((
            CONST.width_objects_surface, CONST.height_objects_surface))
        game_window.game_screen.blit(
            objects_screen, (CONST.HORIZONTAL_OFFSET, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2))
        font = pygame.font.Font('ressource/bahnschrift.ttf', 16)
        objects_text = font.render(
            'You have in your pockets:', True, CONST.white)
        game_window.game_screen.blit(
            objects_text, (CONST.HORIZONTAL_OFFSET+5, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2+16))
        if pockets != []:
            for elem in range(len(pockets)):
                if pockets[elem] == "N" or pockets[elem] == "T" or pockets[elem] == "E":
                    game_window.game_screen.blit(
                        pictures.images[pockets[elem]], (CONST.HORIZONTAL_OFFSET+elem*CONST.CELL_WIDTH, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*3))
                    pygame.display.flip()


class Messages_Display:
    def __init__(self, game_window, userfeedback):
        messages_screen = pygame.Surface((
            CONST.width_objects_surface, CONST.height_objects_surface))
        game_window.game_screen.blit(
            messages_screen, (CONST.HORIZONTAL_OFFSET+CONST.width_objects_surface+CONST.CELL_WIDTH, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2))
        font = pygame.font.Font('ressource/bahnschrift.ttf', 16)
        if userfeedback == 'win':
            messages_screen.fill(CONST.green)
            game_window.game_screen.blit(
                messages_screen, (CONST.HORIZONTAL_OFFSET+CONST.width_objects_surface+CONST.CELL_WIDTH, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2))
            objects_text = font.render(
                'CONGRATS YOU WON!', True, CONST.black)
            game_window.game_screen.blit(
                objects_text, (CONST.HORIZONTAL_OFFSET+CONST.width_objects_surface+CONST.CELL_WIDTH+5, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2+16))
        elif userfeedback == 'loose':
            messages_screen.fill(CONST.red)
            game_window.game_screen.blit(
                messages_screen, (CONST.HORIZONTAL_OFFSET+CONST.width_objects_surface+CONST.CELL_WIDTH, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2))
            objects_text = font.render(
                'SORRY, YOU LOST', True, CONST.white)
            game_window.game_screen.blit(
                objects_text, (CONST.HORIZONTAL_OFFSET+CONST.width_objects_surface+CONST.CELL_WIDTH+5, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2+16))
        elif userfeedback == 'collision':
            messages_screen.fill(CONST.orange)
            game_window.game_screen.blit(
                messages_screen, (CONST.HORIZONTAL_OFFSET+CONST.width_objects_surface+CONST.CELL_WIDTH, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2))
            objects_text = font.render(
                "You hit a wall", True, CONST.white)
            game_window.game_screen.blit(
                objects_text, (CONST.HORIZONTAL_OFFSET+CONST.width_objects_surface+CONST.CELL_WIDTH+5, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2+16))
        elif userfeedback == 0:
            messages_screen.fill(CONST.maze_bg_color)
            game_window.game_screen.blit(
                messages_screen, (CONST.HORIZONTAL_OFFSET+CONST.width_objects_surface+CONST.CELL_WIDTH, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2))
        else:
            messages_screen.fill(CONST.orange)
            game_window.game_screen.blit(
                messages_screen, (CONST.HORIZONTAL_OFFSET+CONST.width_objects_surface+CONST.CELL_WIDTH, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2))
            objects_text = font.render(
                "You pressed an invalid key", True, CONST.black)
            game_window.game_screen.blit(
                objects_text, (CONST.HORIZONTAL_OFFSET+CONST.width_objects_surface+CONST.CELL_WIDTH+5, CONST.HEIGHT_LABYRINTH+CONST.CELL_HEIGHT*2+16))
        pygame.display.flip()


class LabyrinthDisplay():
    def __init__(self, labyrinth, game_window, pictures):
        self.game_window = game_window
        # self.labyrinth = labyrinth
        for row in range(0, CONST.maze_size):
            for column in range(0, CONST.maze_size):
                # if labyrinth.maze[row][column] in self.pictures.images:
                game_window.game_screen.blit(
                    pictures.images[labyrinth.maze[row][column]], (CONST.HORIZONTAL_OFFSET+column*CONST.CELL_HEIGHT, row*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
                pygame.display.flip()
                # elif labyrinth.maze[row][column] == 0:
                #     game_window.game_screen.blit(
                #         game_window.blank, (CONST.HORIZONTAL_OFFSET+column*CONST.CELL_HEIGHT, row*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
                #     pygame.display.flip()

        # elif any(labyrinth.maze[row][column] == items for items in CONST.item_type):
        #     game_window.game_screen.blit(
        #         mac, (CONST.HORIZONTAL_OFFSET+column*CONST.CELL_HEIGHT, row*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
        #     pygame.display.flip()
        # time.sleep(5)

    def update_Display(labyrinth, game_window, X, Y, X_before, Y_before, pictures):

        game_window.game_screen.blit(
            pictures.images[labyrinth.maze[Y_before][X_before]], (CONST.HORIZONTAL_OFFSET+X_before*CONST.CELL_HEIGHT, Y_before*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
        pygame.display.flip()
        game_window.game_screen.blit(
            pictures.images[labyrinth.maze[Y][X]], (CONST.HORIZONTAL_OFFSET+X*CONST.CELL_HEIGHT, Y*CONST.CELL_HEIGHT+CONST.VERTICAL_OFFSET))
        pygame.display.flip()


class Images():
    def __init__(self):
        pass
    images = {"M": GameWindow.mac,
              "N": GameWindow.needle,
              "E": GameWindow.ether,
              "T": GameWindow.tube,
              "F": GameWindow.guard,
              1: GameWindow.wall,
              0: GameWindow.blank,
              "S": GameWindow.start
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

    def pickup(self, labyrinth, Xposition, Yposition, pockets):
        if labyrinth.maze[self.Yposition][self.Xposition] == "N":  # N for needle
            pockets.append("N")
        if labyrinth.maze[self.Yposition][self.Xposition] == "T":  # T for tube
            pockets.append("T")
        if labyrinth.maze[self.Yposition][self.Xposition] == "E":  # E for ether
            pockets.append("E")
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
        Y_before_move = self.Yposition
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            if labyrinth.maze[self.Yposition - 1][self.Xposition] != 1:
                self.Yposition = self.Yposition - 1
                display_message = Messages_Display(
                    self.game_window, 0)
            if labyrinth.maze[Y_before_move - 1][self.Xposition] == 1:
                CONST.messages.hit_wall()
                userfeedback = 'collision'
                display_message = Messages_Display(
                    self.game_window, userfeedback)
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            if labyrinth.maze[self.Yposition + 1][self.Xposition] != 1:
                self.Yposition = self.Yposition + 1
                display_message = Messages_Display(
                    self.game_window, 0)
            if labyrinth.maze[Y_before_move + 1][self.Xposition] == 1:
                CONST.messages.hit_wall()
                userfeedback = 'collision'
                display_message = Messages_Display(
                    self.game_window, userfeedback)
        self.pickup(labyrinth, self.Xposition, self.Yposition, self.pockets)

        labyrinth.maze[Y_before_move][self.Xposition] = virgin_labyrinth.maze[
            Y_before_move
        ][self.Xposition]
        labyrinth.maze[self.Yposition][self.Xposition] = "M"
        # print("labyrinth after movement:")
        print(*labyrinth.maze, sep="\n")
        print("Mc Gyver has in his pockets: {}".format(self.pockets))
        maze_display_update = LabyrinthDisplay.update_Display(
            labyrinth, self.game_window, self.Xposition, self.Yposition, self.Xposition, Y_before_move, pictures)

    def horizontal_movement(
        self, labyrinth, virgin_labyrinth, Xposition, Yposition, event, pictures
    ):
        X_before_move = self.Xposition

        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            if labyrinth.maze[self.Yposition][self.Xposition - 1] != 1:
                self.Xposition = self.Xposition - 1
                display_message = Messages_Display(
                    self.game_window, 0)
            if labyrinth.maze[self.Yposition][X_before_move - 1] == 1:
                CONST.messages.hit_wall()
                userfeedback = 'collision'
                display_message = Messages_Display(
                    self.game_window, userfeedback)
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            if labyrinth.maze[self.Yposition][self.Xposition + 1] != 1:
                self.Xposition = self.Xposition + 1
                display_message = Messages_Display(
                    self.game_window, 0)
            if labyrinth.maze[self.Yposition][X_before_move + 1] == 1:
                CONST.messages.hit_wall()
                userfeedback = 'collision'
                display_message = Messages_Display(
                    self.game_window, userfeedback)
        self.pickup(labyrinth, self.Xposition, self.Yposition, self.pockets)
        labyrinth.maze[self.Yposition][X_before_move] = virgin_labyrinth.maze[
            self.Yposition
        ][X_before_move]
        labyrinth.maze[self.Yposition][self.Xposition] = "M"
        # print("labyrinth after movement:")
        print(*labyrinth.maze, sep="\n")
        print("Mc Gyver has in his pockets: {}".format(self.pockets))
        maze_display_update = LabyrinthDisplay.update_Display(
            labyrinth, self.game_window, self.Xposition, self.Yposition, X_before_move, self.Yposition, pictures)


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

    # creation of our game window
    game_window = GameWindow()

    # loading of our dictionnary linking maze letters to the right images for pygame
    pictures = Images()

    # creation of our character instance
    character = Mc_Gyver(labyrinth, game_window, pictures)

    # display of our objects
    display_objects = Objects_Display(game_window, pictures, character.pockets)

    # creation of our labyrinth display
    maze_display = LabyrinthDisplay(labyrinth, game_window, pictures)
    # maze_display.display_maze(labyrinth)

    game_on_going = True
    while game_on_going:
        OK_user_inputs = [pygame.K_LEFT,
                          pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        # print("please use the z,q,s,d keys of your keyboard to move Mc_Gyver")
        for event in pygame.event.get():
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
            elif event.type == pygame.KEYDOWN and (event.key not in OK_user_inputs):
                userfeedback = 'invalid'
                display_message = Messages_Display(game_window, userfeedback)
                # print("\n you pressed the following invalid key: {} \n".format(pygame.event.key))
            # print("labyrinth used by pygame:")
            # print(*labyrinth.maze, sep="\n")
            pockets_display = Objects_Display(
                game_window, pictures, character.pockets)

            if labyrinth.is_end_cell(character.Xposition, character.Yposition) == True:
                if ("N" in character.pockets and "T" in character.pockets and "E" in character.pockets):
                    # CONST.messages.win()
                    userfeedback = 'win'
                    display_message = Messages_Display(
                        game_window, userfeedback)
                    time.sleep(2)
                    game_on_going = 0
                else:
                    # CONST.messages.loose()
                    userfeedback = 'loose'
                    display_message = Messages_Display(
                        game_window, userfeedback)
                    time.sleep(2)
                    game_on_going = 0


pygame.init()
main()
pygame.quit()
