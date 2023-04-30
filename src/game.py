
# Need game to run: while loop?
# display a map/view
# take input from player
# process input: execute commands or inform user of invalid input
GAME_ACTIVE = True
MAP_SIZE = 5
GAME_MESSAGE = None
MAP = []


def input_handler(input_string):
    command_name, *options_string = input_string.split(" ", 1)
    return (command_name, options_string)


def chat(msg):
    print(msg)
    return True


def print_map():
    print("")
    print("DEV - inside print_map() ")
    for row in MAP:
        row_string = ""
        print(row_string, "funky stuff")
        for cell in row:
            print(cell)
            # eventually we will call a method on <Space> that returns a printable character
            row_string += cell
        print(row_string)
    return True


def quit_game():
    GAME_ACTIVE = False
    return True


COMMANDS = {
    "look": print_map,
    "quit": quit_game,
    "chat": chat,
}


def generate_map():
    for i in range(MAP_SIZE):
        row = []
        for k in range(MAP_SIZE):
            row.append("\033[0;35m ~ \033[0;0m")
        MAP.append(row)


MAP = generate_map()

# def gameLoop():
while (GAME_ACTIVE):
    if (GAME_MESSAGE):
        print("\n"+GAME_MESSAGE+"\n")
        GAME_MESSAGE = None
    # collect input from player
    command_string = input("Input: ")

    command_name, *options_string = input_handler(command_string)


    print("<DEV> command_list:: ", command_name, options_string)

    # GAME_MESSAGE = "Testing Server Notification System"

    # process player input
    if command_name == "quit":
        print("You log out.")
        GAME_ACTIVE = False

    elif command_name == 'look':
        print("DEV - command_name inside IF statement")
        print_map()

    # elif command ==

    else:
        GAME_MESSAGE = "Unrecognized Command"


# gameLoop()
