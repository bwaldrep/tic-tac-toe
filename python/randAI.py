# Bill Waldrep
# July 1, 2012

import random
import player
import board

class Player(player.Player):
    """A player that makes random moves"""
    
    def __init__(self):
        self.oracle = random.Random()

    def getMove(self, board):
        options = board.getMoves()
        return self.oracle.choice(options)
