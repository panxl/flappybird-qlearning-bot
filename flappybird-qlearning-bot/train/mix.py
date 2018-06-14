import sys
import json
from itertools import chain

n = 20
qvalues = []
for i in range(n):
    with open('%02d/qvalues.json' % i, 'r') as f:
        qvalues.append(json.load(f))

qval = {}
# X -> [-40,-30...120] U [140, 210 ... 490]
# Y -> [-300, -290 ... 160] U [180, 240 ... 420]
for x in chain(list(range(-40,140,10)), list(range(140,421,70))):
    for y in chain(list(range(-300,180,10)), list(range(180,421,60))):
        for y2 in chain(list(range(-300,180,10)), list(range(180,421,60))):
            for v in range(-10,11):
                act1 = 0.0
                act2 = 0.0
                for i in range(n):
                    act1 += qvalues[i][str(x)+'_'+str(y)+'_'+str(y2)+'_'+str(v)][0]
                    act2 += qvalues[i][str(x)+'_'+str(y)+'_'+str(y2)+'_'+str(v)][1]
                qval[str(x)+'_'+str(y)+'_'+str(y2)+'_'+str(v)] = [0.0, 0.0]
                qval[str(x)+'_'+str(y)+'_'+str(y2)+'_'+str(v)][0] = act1 / n
                qval[str(x)+'_'+str(y)+'_'+str(y2)+'_'+str(v)][1] = act2 / n

with open('qvalues_%02d.json' % int(sys.argv[1]), 'w') as f:
    json.dump(qval, f)
