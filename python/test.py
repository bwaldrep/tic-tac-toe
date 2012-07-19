# Bill Waldrep
# July 17, 2012

import game
import randAI
import human

r1 = randAI.Player()
r2 = randAI.Player()
h1 = human.Player()
h2 = human.Player()
g = game.Game(r1,r2)
g.play()
