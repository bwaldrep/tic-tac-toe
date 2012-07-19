# Bill Waldrep
# July 17, 2012

import game
import randAI
import human

r1 = randAI.Rand()
r2 = human.Player()
g = game.Game(r1,r2)
g.play()
