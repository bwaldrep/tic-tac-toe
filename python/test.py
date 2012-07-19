# Bill Waldrep
# July 17, 2012

import game
import randAI
import human
import minimax

r1 = randAI.Player()
r2 = randAI.Player()
h1 = human.Player()
h2 = human.Player()
m1 = minimax.Player()
m2 = minimax.Player()
g = game.Game(h1,m2)
g.play()
