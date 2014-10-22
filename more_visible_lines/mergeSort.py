from random import randrange
from time import clock 
import alg3

slopesA = [-1,0]
interceptsA = [1,2]
visibleA = [True, True] 

slopesB = [1,2]
interceptsB = [3,4]
visibleB=[False,True] 

a = len(slopesA) 
b = len(slopesB) 
slopesA.extend(slopesB) 
interceptsA.extend(interceptsB)
visibleA.extend(visibleB)

print slopesA 
print interceptsA
print visibleA
