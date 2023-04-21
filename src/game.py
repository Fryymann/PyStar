
# Need game to run: while loop?
# display a map/view
# take input from player
# process input: execute commands or inform user of invalid input
GAME_ACTIVE = True
MAP_SIZE = 5
GAME_MESSAGE = None


def chat(msg):
    print(msg)
    return True


def print_map():
    print("")
    for row in MAP:
        row_string = ""
        for cell in row:
            # we color the text using Octal escape characters
            row_string += "\033[0;35m ~ \033[0;0m"
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


MAP = []
for i in range(MAP_SIZE):
    row = []
    for k in range(MAP_SIZE):
        row.append([])
    MAP.append(row)





while (GAME_ACTIVE):
    if (GAME_MESSAGE):
        print("\n"+GAME_MESSAGE+"\n")
        GAME_MESSAGE = None

    # collect input from player
    command = input("Input: ")
    # result = COMMANDS[command]

    # process player input
    if command == "quit":
        print("You log out.")
        GAME_ACTIVE = False

    elif command == 'look':
        print_map()

    else:
        GAME_MESSAGE = "Unrecognized Command"
