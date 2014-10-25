from random import randrange
from time import clock 
def alg2(n,slopes,intercepts,visible):
	for i in range(0,n):
		visible.append(True)
        for k in range(2, n):                                   #check visibility of all triplets where i<j<k
                for i in range(1, n-1):
			for j in range(0, n-2):
                                        if(j < i < k):
                                                YjYk = slopes[j]*(intercepts[j] - intercepts[k]) + intercepts[j]*(slopes[k] - slopes[j])
                                                YiYk = slopes[i]*(intercepts[j] - intercepts[k]) + intercepts[i]*(slopes[k] - slopes[j])
                                                if(YjYk > YiYk):
                                                        visible[i] = False



def mergeVisible(slopesA,interceptsA,visibleA,slopesB,interceptsB,visibleB):
	a = len(slopesA)
	b = len(slopesB)
	slopesA.extend(slopesB)
	interceptsA.extend(interceptsB)
	visibleA.extend(visibleB)	

	for i in range(1,a): 
		j = i - 1
		k = i + 1
		YjYk = slopesA[j]*(interceptsA[j] - interceptsA[k]) + interceptsA[j]*(slopesA[k] - slopesA[j])
		YiYk = slopesA[i]*(interceptsA[j] - interceptsA[k]) + interceptsA[i]*(slopesA[k] - slopesA[j])
		if(YjYk > YiYk):
			visibleA[i] = False
			for n in range(a,i):
				visibleA[n] = False

	for i in range(b,a,-1):
		j = i-1
		k = i+1
		YjYk = slopesA[j]*(interceptsA[j] - interceptsA[k]) + interceptsA[j]*(slopesA[k] - slopesA[j])
		YiYk = slopesA[i]*(interceptsA[j] - interceptsA[k]) + interceptsA[i]*(slopesA[k] - slopesA[j])
		if(YjYk > YiYk):
			for n in range(a,i):
				visibleA[n] = False
				break
	
def mergeVisibleRecursive(slopesLeft, interceptsLeft,visibleLeft,slopesRight,interceptsRight,visibleRight, i):
	a = len(slopesLeft)
	b = len(slopesRight) - 1
	if(i < a): 
		if (visibleLeft[i-1] == False):
			visibleLeft[i] = False
			z = i +1 
			mergeVisibleRecursive(slopesLeft,interceptsLeft,visibleLeft,slopesRight,interceptsRight,visibleRight,z)
		else:
			for k in range (0, b):
				j = i-1  
				YjYk = slopesLeft[j]*(interceptsLeft[j] - interceptsRight[k]) + interceptsLeft[j]*(slopesRight[k] - slopesLeft[j])
				YiYk = slopesLeft[i]*(interceptsLeft[j] - interceptsRight[k]) + interceptsLeft[i]*(slopesRight[k] - slopesLeft[j])
				if(YjYk > YiYk):
					visibleLeft[i] = False
					break
			z = i+1
			mergeVisibleRecursive(slopesLeft,interceptsLeft,visibleLeft,slopesRight,interceptsRight,visibleRight,z)		
	if(i <= b):
		bi = b - i 
		if(visibleRight[bi+1] == False):
			visibleRight[bi] = False
			z = i + 1
			mergeVisibleRecursive(slopesLeft,interceptsLeft,visibleLeft,slopesRight,interceptsRight,visibleRight,z)
		else:
			for k in range(0,a):
				j = bi +1 
				YjYk = slopesRight[j]*(interceptsRight[j] - interceptsLeft[k]) + interceptsRight[j]*(slopesLeft[k] - slopesRight[j])
				YiYk = slopesRight[bi]*(interceptsRight[j] - interceptsLeft[k]) + interceptsRight[bi]*(slopesLeft[k] - slopesRight[j])
				if(YjYk > YiYk):
					visibleRight[bi] = False
					break
			z = i +1
			mergeVisibleRecursive(slopesLeft, interceptsLeft,visibleLeft, slopesRight,interceptsRight,visibleRight,z)
	else:
		return

slopesA =[-2,-1,0,1,2]
interceptsA = [0,0,0,0,0]
visibleA = [True, True, True, True, True] 

slopesB = [3,4,5,6,7]
interceptsB = [1,1,1,1,1]
visibleB=[True, True, True, True, True] 

a = len(slopesA) 
b = len(slopesB) 
mergeVisible(slopesA,interceptsA,visibleA,slopesB,interceptsB,visibleB) 

print visibleA

slopesN = [-2,-1,0,1,2,3,4,5,6,7]
interceptsN = [0,0,0,0,0,1,1,1,1,1]
visibleN = []
alg2(a+b,slopesN,interceptsN,visibleN)
print visibleA

slopesX = [-2,-1,0,1,2]
interceptsX = [0,0,0,0,0]
visibleX = [True, True, True, True, True]

slopesY = [3,4,5,6,7]
interceptsY = [1,1,1,1,1]
visibleY =[True, True, True, True, True]

mergeVisibleRecursive(slopesX,interceptsX,visibleX,slopesY,interceptsY,visibleY,1)
print visibleX, visibleY
