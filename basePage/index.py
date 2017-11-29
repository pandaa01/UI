import os

def readtxt():
    with open(os.path.join(os.path.dirname(__file__),'log.txt'),'r') as f:
        print f.readlines()
        print type(f.readlines())

readtxt()


