#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     13/11/2011
# Copyright:   (c) Owner 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os
import math
#file_name = os.path.join("C:\\", "Users", "Owner", "My Documents","python", "huskies.txt")
#file_object = open(file_name, 'r')
#words = {}
#while file_object.readline() != "":
    #line = file_object.readline()
    #count = count + 1
#lines = file_object.readlines()
text1 = "UConn has a lot of weapons. That's the buzz. But in the first game of the season, only some of them were working.Jeremy Lamb scored 30 points, Shabazz Napier scored 21 and Tyler Olander played a solid front-court game, and that was enough for the defending national champions to beat Columbia, 70-57, before 10,167 at Gampel Pavilion.But that wasn't enough to make coach Jim Calhoun very happy."
text2 = "Human beings are members of a whole, In creation of one essence and soul. If one member is afflicted with pain,Other members uneasy will remain. If you've no sympathy for human pain, The name of human you cannot retain! "
def textEntropy(text):
    characters = {}
    count = 0
    uText = text.lower()
    uLength = len(uText)
    for s in uText:
        if s.isalpha():
            count+=count
            if characters.has_key(s):
                characters[s] += 1
            else:
                characters[s] = 1
    entropy = 0
    for key in characters:
       prob = characters[key]/float(uLength)
       #print key, int(characters[key])
       entropy += prob*math.log(prob,2)
    print("Entropy is ",-entropy)
def relativeEntropy(p, q):
    pLength = len(p)
    print ("PLength is ", pLength)
    qLength = len(q)
    divergence = 0
    #Not sure how epsilon is supposed to work- answers vary widely with any change
    epsilon = .00001
    relEntropy = 0
    charP = forText(p)
    charQ = forText(q)
    print charP
    print charQ
    #print probDist(charP, p)
    for key in charP:
        print key
        if key not in charQ:
            print key
            charQ[key] = epsilon
        pProb = charP[key]/float(pLength)
        qProb = charQ[key]/float(qLength)
        print pProb
        print qProb
        divergence += pProb*math.log(pProb/qProb, 2)
    print divergence

textEntropy(text1)
textEntropy(text2)
def probDist(pHash, pText):
    pLength = len(pText)
    for key in pHash:
       prob = pHash[key]/float(pLength)
    return prob

def forText(t):
    chars = {}
    #chars = str(chars)
    lowerCase = t.lower()
    for y in lowerCase:
        if y.isalpha():
            if chars.has_key(y):
                chars[y] += 1
            else:
                chars[y] = 1
    return chars

relativeEntropy(text1, text2)