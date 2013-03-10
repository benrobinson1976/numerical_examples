#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     08/08/2012
# Copyright:   (c) Owner 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


from math import log

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        print labelCounts[key]
        prob = float(labelCounts[key])/numEntries
        print prob
        shannonEnt -= prob * log(prob,2)
        print shannonEnt
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1])
            retDataSet.append(reducedFeatVec)
    return retDataSet