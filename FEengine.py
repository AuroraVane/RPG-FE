class GameState():
    def __init__(self):
        #initialization of board
        ''' pUnit is player unit '''
        ''' eUnit is enemy unit '''
        ''' -- represent empty space'''
        self.board = [
            ["pUnit","--","--","--","--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--","--","--","--","eUnit"],
            ["pUnit","--","--","--","--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--","--","--","--","eUnit"],
            ["pUnit","--","--","--","--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--","--","--","--","eUnit"],
            ["pUnit","--","--","--","--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--","--","--","--","eUnit"]
        ]
        self.playerMoveFirst = True
        self.moveLog = []

    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.UnitMoved
        self.moveLog.append(move) #Log the move to undo it
        self.playerMoveFirst = not self.playerMoveFirst
    
class Move():
    #Mapping of keys to values
    #key : value
    ranksToRows = {"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0} #row 8 is at index 0
    rowsToRanks = {v: k for k, v in ranksToRows.items()}  #reverse of the above
    filesToCol = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11} #column l is at index 11
    colsToFiles = {v: k for k, v in filesToCol.items()} #reverse of the above

    def __init__(self,startSq, endSq,board):
        #Storing variable in the tuple
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]

        #Coordinates of units moved and captured
        self.UnitMoved = board[self.startRow][self.startCol]
        self.UnitCaptured = board[self.endRow][self.endCol]

    def getNotation(self):
        #Change Notation to a chess notation
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)
    
    def getRankFile(self,startRow,startCol):
        return self.colsToFiles[startCol] + self.rowsToRanks[startRow]