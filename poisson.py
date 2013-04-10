# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import SimPy
from SimPy.Simulation import *
from random import expovariate, seed

class Source(Process):
    
    def generate(self, number, interval, resource, mon):
        for i in range(number):
            s = Story(name = "Story%3d"%(i,))
            activate(s, s.play(b=resource, M=mon))
            t = expovariate(1.0/float(interval))
            #print "t %6.2f"% t
            yield hold, self, t
            
class Story(Process):
    
    def play(self, b,M):
        #print "%8.4f %s: story played     "%(now(),self.name)
        arrive = now()
        yield request, self, b
        wait = now() - arrive
        M.observe(wait)
        ttt = expovariate(1.0/float(timeToTest))
        #print "ttt %6.2f %s "% (ttt, self.name)
        yield hold,self,ttt
        yield release,self,b

maxNumber = 50
maxTime=4000.00                                   
timeToTest = 180.0  # mean, minutes                          
ARRint = 90.0    # mean, minutes                          
Nc = 2         # number of counters
theSeed = 12345 
numberOfRuns = 15

for i in range(numberOfRuns):
    #print theseeds[i]
    #seed(theseeds[i])
    k = Resource(capacity=Nc,name="QA")
    wM = Monitor()                
    initialize()
    so = Source("Source")
    activate(so,so.generate(number=maxNumber,interval=ARRint,resource=k,mon=wM),at=0.0)
    simulate(until=maxTime)
    result = wM.count(),wM.mean()
    print "Average time to test %3d stories was %6.2f minutes"% result

print "Number of QA testers %3d"% Nc
#theseeds = [393939,31555999,777999555,319999771]         
#for Sd in theseeds:
#    result = model(Sd)
#    print result
#print "Average wait for %3d completions was %6.2f minutes."% result

# <codecell>

1.0/

# <codecell>

expovariate(1.0/37)

# <codecell>


