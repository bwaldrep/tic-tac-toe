# Bill Waldrep
# July 1, 2012

import player
import board

class Player(player.Player):
    """A player that finds a move using a
    basic minimax search"""
    
    def getMove(self, board):
        return self.pickMax(board, self.marker)[0]

    def pickMax(self, board, marker):
        moves = board.getMoves()
        pairs = []
        for (x,y) in moves:
            temp = board.clone()
            temp.move(x,y,marker)
            if temp.finished():
                score = self.evalBoard(temp)
            else:
                pick = self.pickMin(temp, self.flip(marker))
                score = pick[1]
            pairs.append(((x,y),score))
        pairs.sort(key=lambda x:x[1])
        return pairs[-1]

    def pickMin(self, board, marker):
        moves = board.getMoves()
        pairs = []
        for (x,y) in moves:
            temp = board.clone()
            temp.move(x,y, marker)
            if temp.finished():
                score = self.evalBoard(temp)
            else:
                pick = self.pickMax(temp, self.flip(marker))
                score = pick[1]
            pairs.append(((x,y),score))
        pairs.sort(key=lambda x:x[1])
        return pairs[0]

    def evalBoard(self, board):
        """Evaluate a finished board"""
        w = board.winner()
        if w == self.marker:
            return 1
        elif w == False:
            return 0
        else:
            return -1

    def flip(self, marker):
        if marker == 'X':
            return 'O'
        return 'X'
