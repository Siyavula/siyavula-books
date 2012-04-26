from __future__ import division
from scipy import *
import pylab

N = 500
outcomes = random.randint(1, 7, size=(2,N))
sums = outcomes.sum(axis=0)
trials = arange(1, N+1)

print cumsum(sums == 8)[-10:]
print cumsum(sums == 8)[-10:]/trials[-10:]

pylab.plot(trials, cumsum(sums == 8)/trials, '-')
pylab.plot([0, len(trials)+1], [5/36,5/36], 'k--')
pylab.axis([0, len(trials)+1, -0.05, 1.05])
pylab.xlabel('t')
pylab.ylabel('f')
pylab.savefig('dice_roll_trials.pdf')

pylab.show()
