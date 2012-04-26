from __future__ import division
from scipy import *
import pylab

outcomes = array([1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1])[:30]
trials = arange(1, len(outcomes)+1)

"""
print
print "COLUMNS"
print r"\begin{tabular}"
cols = 3
rows = len(trials)//cols
for i in range(rows):
    print ' & '.join(['%2i & '%(trials[i+col*rows]) + ['T','H'][outcomes[i+col*rows]] + ' & %i'%cumsum(outcomes)[i+col*rows] + ' & %.2f'%(cumsum(outcomes)[i+col*rows]/trials[i+col*rows]) for col in range(cols)]) + r'\\'
print r"\end{tabular}"
"""

print
print "OUTCOMES"
rows = 3
cols = len(trials)//rows
print r"\begin{center}\begin{tabular}{l" + r'c@{\hspace{0.25cm}}'*(cols-1) + 'c}'
print r"  \toprule"
for i in range(rows):
    if i != 0:
        print r'  \midrule'
    print '  trial   & ' + ' & '.join(["%2i"%j for j in range(i*cols+1, (i+1)*cols+1)]) + r' \\'
    print '  outcome & ' + ' & '.join([[" T", " H"][j] for j in outcomes[i*cols:(i+1)*cols]]) + r' \\'
print r'  \bottomrule'
print r'\end{tabular}\end{center}'

print
print "POSITIVE TRIALS"
rows = 3
cols = len(trials)//rows
print r"\begin{center}\begin{tabular}{c" + r'c@{\hspace{0.25cm}}'*(cols-1) + 'c}'
print r"  \toprule"
for i in range(rows):
    if i != 0:
        print r'  \midrule'
    print '  $t$ & ' + ' & '.join(["%2i"%j for j in range(i*cols+1, (i+1)*cols+1)]) + r' \\'
    print '  $p$ & ' + ' & '.join(["%2i"%j for j in cumsum(outcomes)[i*cols:(i+1)*cols]]) + r' \\'
print r'  \bottomrule'
print r'\end{tabular}\end{center}'

print
print "RELATIVE FREQUENCY"
rows = 3
cols = len(trials)//rows
print r"\begin{center}\begin{tabular}{c" + r'c@{\hspace{0.25cm}}'*(cols-1) + 'c}'
print r"  \toprule"
for i in range(rows):
    if i != 0:
        print r'  \midrule'
    print '  $t$ & ' + ' & '.join(["%2i"%j for j in range(i*cols+1, (i+1)*cols+1)]) + r' \\'
    print '  $f$ & ' + ' & '.join(["%.2f"%j for j in (cumsum(outcomes)/trials)[i*cols:(i+1)*cols]]) + r' \\'
print r'  \bottomrule'
print r'\end{tabular}\end{center}'

pylab.plot(trials, cumsum(outcomes)/trials, 'o-')
pylab.plot([0, len(trials)+1], [0.5,0.5], 'k--')
pylab.axis([0, len(trials)+1, -0.05, 1.05])
pylab.xlabel('t')
pylab.ylabel('f')
pylab.savefig('coin_toss_trials.pdf')

pylab.show()
