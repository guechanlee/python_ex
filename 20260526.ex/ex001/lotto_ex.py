import random

userNums = []
randNums = []
collect = []

def setUNumbers(ns):     # setter = 어떠한 데이터를 세팅  set + UNumbers
    global userNums
    userNums = ns

def getUNumbers():       # getter   get + UNumbers
    return userNums

def setRNumbers():
    global randNums
    randNums = random.sample(range(1,46), 6)

def getRNumbers():
    return randNums

def compareNumbers():
    global userNums
    global randNums
    global collect

    collect = []
    for item in userNums:
        if randNums.count(item) != 0:
            collect.append(item)

    return collect
