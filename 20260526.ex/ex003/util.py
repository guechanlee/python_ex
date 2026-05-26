import time

def getDay():
    return time.strftime('%Y-%m-%d', time.localtime())

def getTime():
    return time.strftime('%H:%M:%S', time.localtime())