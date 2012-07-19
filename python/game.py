# Bill Waldrep
# July 6, 2012

import board

class Game(object):
    """The top level class for the
    tic-tac-toe game"""
    
    def __init__(self, player1, player2):
        self.board = board.Board()
        self.p1 = player1
        self.p2 = player2
        self.p1.setMarker('X')
        self.p2.setMarker('O')

    def play(self):
        while not self.board.finished():
            print self.board
            self.doTurn()
        
        print self.board
        w = self.board.winner()
        if w:
            print w, "wins!"
        else:
            print "It's a tie"

    def doTurn(self):
        x,y = self.p1.getMove(self.board)
        try:
            self.board.move(x,y,self.p1.marker)
            self.p1, self.p2 = self.p2, self.p1
        except:
            print "Sorry, invalid move"
