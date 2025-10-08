import curses
import sudoku
import pygame

def playGame(screen, sudokugame: sudoku.Sudoku):
    pygame.mixer.init()
    pygame.mixer.music.load("./music/commit sudoku.mp3")
    pygame.mixer.music.play(loops=-1)

    curses.curs_set(0)
    currentRow, currentCol = 0, 0
    starter_board = sudokugame.getBoard()

    fixed_cells = {(r, c) for r in range(9) for c in range(9) if starter_board[r][c] != 0}
    valid_keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:
        update(screen, sudokugame.getBoard(), fixed_cells, currentRow, currentCol)

        key = screen.getch()

        if key == curses.KEY_UP and currentRow > 0:
            currentRow -= 1
        elif key == curses.KEY_DOWN and currentRow < 8:
            currentRow += 1
        elif key == curses.KEY_LEFT and currentCol > 0:
            currentCol -= 1
        elif key == curses.KEY_RIGHT and currentCol < 8:
            currentCol += 1
        elif key == 27:
            pygame.mixer.music.stop()
            break
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            isValid = sudokugame.removeCell(currentRow, currentCol)
        else:
            keyvalue = int(chr(key))
            isValid = False
            #sudokugame.forceinsert(currentRow, currentCol, int(chr(key)))
            if keyvalue in valid_keys:
                isValid = sudokugame.insertCell(currentRow, currentCol, int(chr(key)))
            else:
                isValid = False
            update(screen, sudokugame.getBoard(), fixed_cells, currentRow, currentCol, isValid)
        
    pygame.mixer.music.stop()
def getNumberKey(screen):
    pass

def update(screen, board, fixed_cells, selected_row, selected_col, isValid = True, currentColtimeString = "00:00:00", difficulty = "EASY", playername = "Kekkonen"):
    screen.clear()
    h, w = screen.getmaxyx()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Selected cell
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Fixed cell
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Highlighted row/col

    # Each cell is 3 characters wide, plus grid lines
    cell_width = 3
    cell_height = 1
    grid_width = 9 * cell_width + 4  # +4 for 3 vertical block lines + borders
    grid_height = 9 * cell_height + 4

    # Centering the board
    h, w = screen.getmaxyx()
    start_y = (h - grid_height) // 2
    start_x = (w - grid_width) // 2

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            char = str(num) if num != 0 else "."

            # Default color
            color = curses.color_pair(1)

            # Highlight fixed cells
            if (i, j) in fixed_cells:
                color = curses.color_pair(3)

            # Highlight selected cell last (overrides others)
            if i == selected_row and j == selected_col:
                color = curses.color_pair(2)

            # Compute coordinates with spacing and block lines
            y = start_y + i + (i // 3) + 1
            x = start_x + j * 3 + (j // 3) + 1

            screen.addstr(y, x, f" {char} ", color)

        # Horizontal block lines
        if i % 3 == 2 and i != 8:
            line_y = start_y + i + (i // 3) + 2
            screen.addstr(line_y, start_x, "-" * grid_width)

    # Vertical block lines
    for block in [3, 6]:
        for y in range(start_y + 1, start_y + grid_height - 1):
            screen.addstr(y, start_x + block * 3 + (block // 3), "|")

    screen.refresh()

            


        
    
