import curses 
import sudokuplayer
import savehandler
import sudoku
import sudokufactory

sudoku_art = [
    "   *      //   *   ||   ||      || *  ||      ||       ||  //   *  ||==//",
    "         ||     //===  //   *   ||    ||     //  *     ||  ||     //     ",
    "     ---------------------------------------------------------------  *  ",
    "=====| #######   ##    ##   ######   #######   ##    ##   ##    ## | //==",
    "   * | ##        ##    ##   ##   ##  ##   ##   ##  ###    ##    ## |// * ",
    "  ===| #######   ##    ##   ##    #  ##   ##   ####       ##    ## |     ",
    "//   |      ##   ##    ##   ##   ##  ##   ##   ##  ###    ##    ## |=====",
    " *   | #######   ########   ######   #######   ##    ##   ######## |     ",
    "     ---------------------------------------------------------------     ",
    "   //  ||  ||  *   ||     ||     ||   *  ||  *         //        \\\\  *   ",
    "==// * ||  ||     // *    || *   ||       ||       *   ||*        \\\\     "
]
difficulties = [
    "EASY",
    "MEDIUM",
    "HARD"
]
def printMainMenu(screen):
    curses.curs_set(0)
    choice = 0
    options = [
        "Start a new game",
        "Continue a saved game",
        "Show highscores",
        "Exit"
    ]
    while True:
        screen.clear()
        h, w = screen.getmaxyx()

        for index, line in enumerate(sudoku_art):
            x = w//2 - len(line)//2
            y = h//4 - len(sudoku_art)//2 + index
            screen.addstr(y, x, line)

        for index, option in enumerate(options):
            x = w//2 - len(option)//2
            y = h//2 - len(options)//2 + index + 5
            if choice == index:
                screen.attron(curses.color_pair(1))
                screen.addstr(y, x, option)
                screen.attroff(curses.color_pair(1))
            else:
                screen.addstr(y, x, option)
        screen.refresh()

        key = screen.getch()
        if key == curses.KEY_UP and choice > 0:
            choice -= 1
        elif key == curses.KEY_DOWN and choice < len(options)-1:
            choice += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            if choice == 0:
                printGameStartOptions(screen)
                pass
            elif choice == 1:
                # show a list of saved games
                pass
            elif choice == 2:
                # show highscores
                pass
            elif choice == 3:
                break

def printGameStartOptions(screen):
    curses.curs_set(0)
    choice = 0
    choice_difficulty = 0
    password = ""
    playerName = ""
    options = [
        "START GAME",
        "Set difficulty:",
        "Set game password:",
        "Set player name:",
        "Exit"
    ]
    while True:
        screen.clear()
        h, w = screen.getmaxyx()

        for index, line in enumerate(sudoku_art):
            x = w//2 - len(line)//2
            y = h//4 - len(sudoku_art)//2 + index
            screen.addstr(y, x, line)

        for index, option in enumerate(options):
            x = w//2 - len(option)//2
            y = h//2 - len(options)//2 + index + 5
            if choice == index:
                screen.attron(curses.color_pair(1))
                if index == 1:
                    screen.addstr(y, x, f"{option}  {difficulties[choice_difficulty]}")
                elif index == 2:
                    screen.addstr(y, x, f"{option} {password}")
                elif index == 3:
                    screen.addstr(y, x, f"{option}  {playerName}")
                else:
                    screen.addstr(y, x, option)
                screen.attroff(curses.color_pair(1))
            else:
                if index == 1:
                    screen.addstr(y, x, f"{option}  {difficulties[choice_difficulty]}")
                elif index == 2:
                    screen.addstr(y, x, f"{option} {password}")
                elif index == 3:
                    screen.addstr(y, x, f"{option}  {playerName}")
                else:
                    screen.addstr(y, x, option)
        screen.refresh()

        key = screen.getch()
        if key == curses.KEY_UP and choice > 0:
            choice -= 1
        elif key == curses.KEY_DOWN and choice < len(options)-1:
            choice += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            if choice == 0:
                sudokugame = None
                if choice_difficulty == 0:
                    sudokugame = sudoku.Sudoku(0, "EASY", playerName, password)
                if choice_difficulty == 1:
                    sudokugame = sudoku.Sudoku(0, "MEDIUM", playerName, password)
                if choice_difficulty == 2:
                    sudokugame = sudoku.Sudoku(0, "HARD", playerName, password)
                sudokuplayer.playGame(screen, sudokugame)
            elif choice == 1:
                choice_difficulty = printDifficultySelector(screen)
                pass
            elif choice == 2:
                password = printPasswordSelector(screen)
                pass
            elif choice == 3:
                playerName = printNameSelector(screen)
            elif choice == 4:
                break

def printNameSelector(screen):
    name = ""
    while True:
        screen.clear()
        h, w = screen.getmaxyx()

        for index, line in enumerate(sudoku_art):
            x = w//2 - len(line)//2
            y = h//4 - len(sudoku_art)//2 + index
            screen.addstr(y, x, line)

        name_field = f"Your playername: {name}"
        x = w//2 - len(name_field)//2
        y = h//2 + 5
        screen.addstr(y, x, name_field)
        screen.refresh()
        key = screen.getch()
        if key not in [curses.KEY_ENTER, 10, 13]:
            if key in (curses.KEY_BACKSPACE, 127, 8):
                name = name[:-1]
            else:
                name += chr(key)
        elif key in [curses.KEY_ENTER, 10, 13]:
            return name

def printPasswordSelector(screen):
    password = ""
    while True:
        screen.clear()
        h, w = screen.getmaxyx()

        for index, line in enumerate(sudoku_art):
            x = w//2 - len(line)//2
            y = h//4 - len(sudoku_art)//2 + index
            screen.addstr(y, x, line)

        password_field = f"Your password: {password}"
        x = w//2 - len(password_field)//2
        y = h//2 + 5
        screen.addstr(y, x, password_field)
        screen.refresh()
        key = screen.getch()
        if key not in [curses.KEY_ENTER, 10, 13]:
            if key in (curses.KEY_BACKSPACE, 127, 8):
                password = password[:-1]
            else:
                password += chr(key)
        elif key in [curses.KEY_ENTER, 10, 13]:
            return password

def printDifficultySelector(screen):
    choice = 0
    while True:
        screen.clear()
        h, w = screen.getmaxyx()

        for index, line in enumerate(sudoku_art):
            x = w//2 - len(line)//2
            y = h//4 - len(sudoku_art)//2 + index
            screen.addstr(y, x, line)

        for index, option in enumerate(difficulties):
            x = w//2 - len(option)//2
            y = h//2 - len(difficulties)//2 + index + 5
            if choice == index:
                screen.attron(curses.color_pair(1))
                screen.addstr(y, x, option)
                screen.attroff(curses.color_pair(1))
            else:
                screen.addstr(y, x, option)
        screen.refresh()
        key = screen.getch()
        if key == curses.KEY_UP and choice > 0:
            choice -= 1
        elif key == curses.KEY_DOWN and choice < len(difficulties)-1:
            choice += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            return choice

def startMenu():
    curses.wrapper(lambda screen: (
        curses.start_color(),
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN),
        printMainMenu(screen)
    ))
