import os
import sudoku

def initSaves():
    if not os.path.isdir("saves"):
        os.makedirs("./saves")

def loadSaves():
    try:
        gamesaves = []
        for gamefile in os.listdir("./saves"):
            gamefile_name= os.fsdecode(gamefile)
            sudokugame = loadSave(gamefile_name)
            gamesaves.append(sudokugame)
            return gamesaves
    except Exception:
        print("A fatal error has occured and i have no idea wtf is going on...")
        return None

def loadSave(gamefile_name):
    try:
        f = open(gamefile_name, "r")
        f.readline()
        board = []
        (timeplayed,difficulty,playername,passwordhash,mapid) = tuple(f.readline().split(","))
        for i in range(9):
            board.append(list(map(lambda x: int(x), f.readline().split(","))))
        sudoku = sudoku.sudoku(timeplayed,difficulty,playername,passwordhash,mapid,board)
        f.close()
        return sudoku
    except Exception:
        print(f"Could not read the filename {gamefile_name}")
        return None

def saveGame(sudoku):
    pass

def saveScore(sudoku):
    pass

# list all games from the saved folder.
def listAllSaves():
    try:
        for gamefile in os.listdir("./saves"):
            gamefile_name = os.fsdecode(gamefile)
            print(gamefile_name)
    except Exception:
        print("No saves were found")
