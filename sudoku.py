class Sudoku:
    def __init__(self, timeplayed, difficulty, playername, passwordhash, mapid, board):
        self.timeplayer = timeplayed
        self.difficulty = difficulty
        self.playername = playername
        self.passwordhash = passwordhash
        self.mapid = mapid
        self.board = board

	

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
        box_row_start = row // 3
        box_column_start = column // 3
        for y in range(0, 3+1):
            for x in range(0, 3+1):
                checkthis[y][x] = self.board[box_row_start+y][box_column_start+x]
        checkthis[row][column] = number
        checkthis = [item for item_list in checkthis for item in item_list]
        return self.checkGroupValidity(checkthis)

    def sudokuRowValid(self, row, column, number):
        checkthis = []
        for x in range(1, 9):
            checkthis.append(self.board[row][x])
        checkthis[column] = number
        return self.checkGroupValidity(checkthis)
    
    def sudokuColumnValid(self, row, column, number):
        checkthis = []
        for y in range(1, 9):
            checkthis.append(self.board[y][column])
        checkthis[row] = number
        return self.checkGroupValidity(checkthis)

    