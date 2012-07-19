# Bill Waldrep
# July 1, 2012

import player
import board

class Player(player.Player):
    """A player that accepts user input
    to make moves"""
    
    def getMove(self, board):
      print "Please enter your move:"
      x,y = input()
      return (x,y)
