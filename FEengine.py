import FEstack as stack

class GameState():
    def __init__(self):
        #initialization of board
        ''' pUnit is player unit '''
        ''' eUnit is enemy unit '''
        ''' -- represent empty space'''
        self.board = [
            ["--","pSword","--","--","--","--","--","--","--","--","eKnight","--"],
            ["--","--","--","--","--","--","--","--","--","--","--","--"],
            ["pCleric","pUnit","--","--","--","--","--","--","--","--","eUnit","eMage"],
            ["pVIP","--","--","--","--","--","--","--","--","--","--","eLord"],
            ["pLord","--","--","--","--","--","--","--","--","--","--","eVIP"],
            ["pMage","pUnit","--","--","--","--","--","--","--","--","eUnit","eCleric"],
            ["--","--","--","--","--","--","--","--","--","--","--","--"],
            ["--","pKnight","--","--","--","--","--","--","--","--","eSword","--"]
        ]
        self.playerMoveFirst = True
        self.moveLog = stack.Stack()

    #Function to make a move to the board takes in a move object
    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.UnitMoved
        self.moveLog.push([(move.startRow,move.startCol),(move.endRow,move.endCol),(move.UnitMoved,move.UnitCaptured)]) #Log the move to undo it
        self.playerMoveFirst = not self.playerMoveFirst

    def undoMove(self):
        if not self.moveLog.isEmpty():
            move = self.moveLog.pop()
            self.board[move[0][0]][move[0][1]] = move[2][0] #unit moved
            self.board[move[1][0]][move[1][1]] = move[2][1] #unit captured
            self.playerMoveFirst = not self.playerMoveFirst

    #All legal moves
    def getValidMoves(self):
        return self.getAllMoves()
    
    #All moves
    def getAllMoves(self):
        moves = [Move((0,1),(0,2),self.board)]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0] #Check if its p or e
                if (turn == 'p' and self.playerMoveFirst) or (turn == 'e' and not self.playerMoveFirst):
                    piece = self.board[r][c][1:]
                    if piece == 'Unit':
                        self.getUnitMoves(r,c,moves)
                    elif piece == 'Cleric':
                        self.getClericMoves(r,c,moves)
                    elif piece == 'Mage':
                        self.getMageMoves(r,c,moves)
                    elif piece == 'Knight':
                        self.getKnightMoves(r,c,moves)
                    elif piece == 'Lord':
                        self.getLordMoves(r,c,moves)
                    elif piece == 'Sword':
                        self.getSwordMoves(r,c,moves)
                    elif piece == 'VIP':
                        self.getVIPMoves(r,c,moves)
        return moves

    #Get all moves for Basic Unit 
    def getUnitMoves(self,r,c,moves):
        pass

    #Get all moves for Cleric
    def getClericMoves(self,r,c,moves):
        pass

    #Get all moves for Mage
    def getMageMoves(self,r,c,moves):
        pass   

    #Get all moves for Knight
    def getKnightMoves(self,r,c,moves):
        pass

    #Get all moves for Lord
    def getLordMoves(self,r,c,moves):
        pass

    #Get all moves for Sword
    def getSwordMoves(self,r,c,moves):
        pass

    #Get all moves for VIP
    def getVIPMoves(self,r,c,moves):
        pass


    
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
        self.moveID = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol

    #Overriding the equals method
    def __eq__(self,other):
        if isinstance(other,Move): return self.moveID == other.moveID
        return False
    
    def getNotation(self):
        #Change Notation to a chess notation
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)
    
    def getRankFile(self,startRow,startCol):
        return self.colsToFiles[startCol] + self.rowsToRanks[startRow]