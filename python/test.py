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
"""
rwins = 0
mwins = 0
ties = 0
for i in range(100):
    g1 = game.Game(r1,m1)
    w = g1.play()
    if w == 'X':
        rwins = rwins + 1
    elif w == 'O':
        mwins = mwins + 1
    else:
        ties = ties + 1
    print "game", i

print '#' * 40
print "Final Results:"
print "Random wins:", rwins
print "Minimax wins:", mwins
print "Ties:", ties
"""
