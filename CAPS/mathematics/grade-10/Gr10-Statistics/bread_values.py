from __future__ import division
from scipy import *

data = """
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
802.39
787.78
815.74
807.41
801.48
786.59
799.01
796.76
798.93
809.68
798.72
818.26
789.08
805.99
802.5
793.63
785.37
809.3
787.65
801.45
799.35
819.59
812.62
809.05
791.13
805.28
817.76
801.01
801.21
795.86
795.21
820.39
806.64
819.54
796.67
789
796.33
787.87
799.84
789.45
802.05
802.2
788.99
797.72
776.71
790.69
803.16
801.24
807.32
808.8
780.38
812.61
801.82
784.68
792.19
809.8
802.37
790.83
792.43
789.24
815.63
799.35
791.23
796.2
817.57
799.05
825.96
807.89
806.65
780.23
""".strip().split('\n')

print 'TABLE'
print len(data)
for row in range(11):
    for col in range(7):
        value = data[row*7+col]
        try:
            value = float(value)
            value = int(round(value*10))
            integerPart = value // 10
            fracPart = value % 10
            print ('$%i,%i$'%(integerPart, fracPart)),
        except ValueError:
            print value,
        if col < 6:
            print '&',
        else:
            print '\\\\'

print

print 'MEAN'
for col in range(7):
    output = '\\item[] ' + data[col] + ': $\\frac{'
    total = 0
    for row in range(1, 11):
        value = round(float(data[row*7+col]), 1)
        total += value

        value = int(round(value*10))
        integerPart = value // 10
        fracPart = value % 10
        value = '%i,%i'%(integerPart, fracPart)

        #output += value

        if row < 10:
            pass#output += ' + '
        else:
            value = int(round(total*10))
            integerPart = value // 10
            fracPart = value % 10
            value = '%i,%i'%(integerPart, fracPart)
            output += value + '}{10} = '

            value = int(round(total))
            integerPart = value // 10
            fracPart = value % 10
            value = '%i,%i'%(integerPart, fracPart)
            output += value + '\\textrm{ g}$'
    print output

print
print 'MEDIAN'
for col in range(7):
    output = '\\item[] ' + data[col] + ': $'
    values = []
    for row in range(1, 11):
        value = round(float(data[row*7+col]), 1)
        values.append(value)

    values.sort()
    print output + '; '.join([str(int(x)) + ',' + str(int((x%1)*10)) for x in values]) + '$'
    print median(values)
