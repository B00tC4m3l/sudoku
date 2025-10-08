import sudokufactory
import copy

class Sudoku:
    def __init__(self, timeplayed, difficulty, playername, password, mapid = None, startboard = None):
        self.timeplayed = timeplayed
        self.difficulty = difficulty
        self.playername = playername
        self.password = password
        self.mapid = ""
        self.startboard = []
        if mapid == None:
            if difficulty == "EASY":
                self.mapid = sudokufactory.generateEasy()
            elif difficulty == "MEDIUM":
                self.mapid = sudokufactory.generateMedium()
            elif difficulty == "HARD":
                self.mapid = sudokufactory.generateHard()
        else:
            self.mapid = mapid
        if startboard == None:
            self.startboard = sudokufactory.mapids[self.mapid]
        else:
            self.startboard = startboard
        self.gameboard = copy.deepcopy(self.startboard)
	
    def insertCell(self, row, column, number):
        if number < 0 or 9 < number:
            return False
        if self.checkIsInmovableCell(row, column):
            return False
        if self.sudokuInsertionValid(row, column, number):
            self.gameboard[row][column] = number
            return True
        return False
    
    def getBoard(self):
        return self.gameboard
    
    def checkIsInmovableCell(self, row, column):
        if self.startboard[row][column] != 0:
            return True

    def sudokuInsertionValid(self, row, column, number):
        return self.sudokuBoxValid(row, column, number) \
            and self.sudokuColumnValid(row, column, number) \
            and self.sudokuRowValid(row, column, number)
    
    def checkGroupValidity(self, group):
        for i in range(1, 9+1):
            if group.count(i) > 1:
                return False
        return True
    
    def sudokuBoxValid(self, row, column, number):
        checkthis = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        box_row_start = (row+1) // 3
        box_column_start = (column+1) // 3
        for y in range(0, 3):
            for x in range(0, 3):
                checkthis[y][x] = self.gameboard[box_row_start*3+y][box_column_start*3+x]
        checkthis[row//3][column//3] = number
        checkthis = [item for item_list in checkthis for item in item_list]
        return self.checkGroupValidity(checkthis)

    def sudokuRowValid(self, row, column, number):
        checkthis = []
        for x in range(1, 9):
            checkthis.append(self.gameboard[row][x])
        checkthis[column] = number
        return self.checkGroupValidity(checkthis)
    
    def sudokuColumnValid(self, row, column, number):
        checkthis = []
        for y in range(1, 9):
            checkthis.append(self.gameboard[y][column])
        checkthis[row] = number
        return self.checkGroupValidity(checkthis)

    def forceinsert(self, row, column, value):
        self.gameboard[row][column] = value

if __name__ == "__main__":
    sudoku = Sudoku(0, "EASY", "Kekkonen", "shush")
    for i in range(9):
        print(sudoku.startboard[i])
    result = sudoku.insertCell(0, 0, 2)
    print(result)
    for i in range(9):
        print(sudoku.startboard[i])
    result = sudoku.insertCell(0, 0, 6)
    print(result)
    for i in range(9):
        print(sudoku.startboard[i])