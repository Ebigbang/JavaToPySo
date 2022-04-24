from ent_elect_model import *
import os
import sys

argName=sys.argv[0]
argValue=sys.argv[1]
argValue = [ x.strip() for x in argValue.strip('[]').split(',') ]
print(argName)
print(argValue)
a=elect_model(argValue[0],argValue[1],argValue[2],argValue[3],argValue[4],argValue[5],argValue[6],argValue[7])
a.ent_elect()
print(a)