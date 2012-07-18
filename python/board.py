# Bill Waldrep
# July 1, 2012

class Board:
    """A simple tic tac toe board"""

    def __init__(self):
        self.board = [list('   ') for i in range(3)]

    def __str__(self):
        """Draw the board nicely for
        printing"""
        middle = "-+-+-\n"
        pboard = map(lambda(row) : '|'.join(row) + '\n', self.board)
        return middle.join(pboard)

    def empty(self, x, y):
        """Returns true if position (x,y) is empty"""
        if self.board[x][y] == ' ':
            return True
        return False

    def move(self, x, y, marker):
        """Attempt to place marker on position
        (x,y). If the position is not empty
        raise an exception"""
        if self.empty(x,y):
            self.board[x][y] = marker
        else:
            raise Exception("ERROR INVALID MOVE")

    def winner(self):
        """Returns true if either player has
        won the game"""
        rows = self.board
        cols = [map(lambda(row):row[i],rows) for i in range(3)]
        total = rows + cols
        for item in total:
            if item[0] == item[1] == item[2] != ' ':
                return True
        return False

    def finished(self):
        """Returns true if there is a winner or 
        if there are no more valid moves"""
        if self.winner():
            return True

        for i, j in 

        return True

    def getMoves(self, marker):
        """Returns a list of the boards resulting
        from making every possible valid move"""
        res = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    temp = Board()
                    # avoid a shallow copy
                    temp.board = [list(row) for row in self.board]
                    temp.move(i,j,marker)
                    res.append(temp)
        return res
