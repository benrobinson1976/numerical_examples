# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>
from numpy import *
import pylab

x = [0, 0];
p = [.85, .92, .99, 1.0]

A1 = [[.85, .04],[-.04, .85]];
A2 = [[.20, -.26],[.23, .22]];
A3 = [[-.15, .28],[.26, .24]];
A4 = [[0, 0], [0, .16]];

b1 = [0, .16];
b2 = [0, .44];

for i in range(10000):
    r = random.rand()
    if r < p[0]:
        x = dot(A1,x) + b1
        #print p[0], r
    elif r < p[1]:
        x = dot(A2,x) + b1
        #print p[1], r
    elif r < p[2]:
        x = dot(A3,x) + b2
        #print p[2], r
    #elif r < p[3]:
        #print p[3], r
    else:
        x = dot(A4,x)
        #print "******"
    pylab.plot(x[0],x[1],'m.',markersize=1, color='yellow')

#pylab.show()
F = pylab.gcf()
F.set_size_inches(8, 8)
F.savefig("test.png")

# <codecell>


# <codecell>


