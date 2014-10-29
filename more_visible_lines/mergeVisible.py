from random import randrange
from time import clock 
from Line import Line 
import math

num_lines = 2
def genLines(n,P):
	slopes = []
	intercepts = []
	for i in range(0,n):
		rand_slope = randrange(-n,n)
		while slopes.count(rand_slope) != 0:
			rand_slope = randrange(-n,n)
		slopes.append(rand_slope)
		intercepts.append(randrange(-n,n))
	slopes.sort() 	
	for i in range(0,n):
		x = Line()
		P.append(x) 
		P[i].m = slopes[i] 
		P[i].b = intercepts[i]
def intercept(l1,l2):
 	x = (l2.b - l1.b) 
	y = (l1.m - l2.m) 
	if y != 0:
		z = x / y
	else:
		z = 'inf'
	return z

def mergeLeft(L,R):
	for i in range(0, len(L)):
		if(len(L) == 1):
			Lx1 = 'inf'
			Lx2 = 'inf'
		else:
			Lx1 = intercept(L[i],L[i-1])
		if(i == len(L)-1):
			Lx2 = 'inf'	
		else:
			Lx2 = intercept(L[i],L[i+1]) 
		L[i].dom = [Lx1, Lx2]
		for k in range(0,len(R)):
			if(len(R) == 1):
				Rx1 = 'inf'
				Rx2 = 'inf'
			else:
				Rx1 = intercept(R[k],R[k-1])
				
			if(k == len(R)-1):
				Rx2 = 'inf'
			else:
				Rx2 = intercept(R[k],R[k+1])
			R[k].dom = [Rx1,Rx2]
			if((L[i].dom[0] <= R[k].dom[0] <= L[i].dom[1]) or (L[i].dom[0] <= R[k].dom[1] <= L[i].dom[i]) or  L[i].dom[0] == 'inf' or
			    L[i].dom[1] == 'inf' or R[k].dom[0] == 'inf' or R[k].dom[1] == 'inf' ):
				j = i -1
	                        Yjxjk = L[j].m * (L[j].b - R[k].b) + L[j].b * (R[k].m - L[j].m)
	                        Yixjk = L[i].m * (L[j].b - R[k].b) + L[i].b * (R[k].m - L[j].m)
 	       	                if(Yjxjk > Yixjk):
        	    		       	for z in range(i,len(L)):
        		                       	L[z].vis = False
					return

def mergeRight(L,R):
	for i in range(len(R)-2,-1,-1):
	
		if(len(R) <= 1):
			Rx1 = 'inf'
			Rx2 = 'inf'
		else:
			Rx1 = intercept(R[i],R[i-1])
		if(i > len(R)-1):
			Rx2 = 'inf'
		else:
	        	Rx2 = intercept(R[i],R[i+1])
	        R[i].dom = [Rx1,Rx2]	     
		for j in range(0,len(L)-1):
			if(len(L) <= 1):
				Lx1 = 'inf'
				Lx2 = 'inf'
			else:
		        	Lx1 = intercept(L[j],L[j-1])
	                if(j == len(L)):
				Lx2 = 'inf'
			else:	
				Lx2 = intercept(L[j],L[j+1])
	                L[j].dom = [Lx1,Lx2]
	                if((R[i].dom[0] <= L[j].dom[0] <= R[i].dom[1]) or (R[i].dom[0] <= L[j].dom[1] <= R[i].dom[1]) or L[j].dom[0] == 'inf' or
			    L[j].dom[1] == 'inf' or R[i].dom[0] == 'inf' or R[i].dom[1] == 'inf' ):
	                	k = i + 1
				Yjxjk = L[j].m * (L[j].b - R[k].b) + L[j].b * (R[k].m - L[j].m)
	                        Yixjk = R[i].m * (L[j].b - R[k].b) + R[i].b * (R[k].m - L[j].m)
	                        if(Yjxjk > Yixjk):
        	                	for z in range(0,i):
        	                        	R[z].vis = False
        	                        return
def mergeLines(L,R):
	mergeLeft(L,R)
	mergeRight(L,R) 
	L.extend(R)
	return L

def alg4(Y):
	L = []
	R = []
	n = len(Y)
	l = int(math.floor(n/2))
	print "n-l = " + repr(n-l) + " l= " +repr(l) 
	for i in range(0,n-l):
		#print "i = " + repr(i)
		x = Line()	
		L.append(x)
		L[i] = Y[i]
	for i in range(0,l):
		j = i + l 
		x = Line()
		R.append(x)
		R[i] = Y[j]		
		
	if(n <= 4):
	 	mergeLines(L,R)
		return L
	else: 
		for i in range(0,n-l):
			print "L[i] = " + repr(L[i].m)
		for j in range(0,l):
			print "R[j] = " + repr( R[j].m)
		mergeLines(alg4(L),alg4(R))
		L.extend(R)
		return L

def alg2(n,slopes,intercepts,visible):
	for i in range(0,n):
		visible.append(True)
        for k in range(2, n):                                   #check visibility of all triplets where j<i<k
                for i in range(1, n-1):
			for j in range(0, n-2):
                                        if(j < i < k):
						YjYk = slopes[j]*(intercepts[j] - intercepts[k]) + intercepts[j]*(slopes[k] - slopes[j])
                                               	YiYk = slopes[i]*(intercepts[j] - intercepts[k]) + intercepts[i]*(slopes[k] - slopes[j])
						if( YjYk > YiYk):
                                                        visible[i] = False

#slopesA =[-2,-1,0,1,2]
#interceptsA = [0,0,0,0,0]
#visibleA = [True, True, True, True, True] 

#slopesB = [3,4,5,6,7]
#interceptsB = [1,1,1,1,1]
#visibleB=[True, True, True, True, True] 

#a = len(slopesA) 
#b = len(slopesB) 
#mergeVisible(slopesA,intarceptsA,visibleA,slopesB,interceptsB,visibleB) 

l = []
r = []
genLines(num_lines,l)
genLines(num_lines,r)
L = []
R = [] 
#for i in range (0,num_lines):
#	print repr(l[i].m) + ',' + repr(l[i].b)
slopesN = [-1,0,1]
interceptsN = [3,0,-1]
visibleN = []
n = len(slopesN)
alg2(n,slopesN,interceptsN,visibleN)
print visibleN
print slopesN
print interceptsN
slopesX = [-1,0]
interceptsX = [3,0]
visibleX = [True]

slopesY = [1]
interceptsY = [-1]
visibleY =[True,True]

for i in range(0,len(slopesX)):
      	x = Line()
	L.append(x)
	L[i].m = slopesX[i]
        L[i].b = interceptsX[i]

for j in range(0,len(slopesY)):
	x = Line()
	R.append(x)
	R[j].m = slopesY[j]
	R[j].b = interceptsY[j]

mergeLines(L,R)
#L.extend(R)
for i in range (0,len(L)):
	print repr(L[i].m) + ' ' +  repr(L[i].b) + ' ' + repr(L[i].vis) + repr(L[i].dom)

for i in range(0,len(L)):
	L[i].vis = True
alg4(L)
print '\n'
for i in range (0,len(L)):
        print  repr(L[i].m) + ' ' +  repr(L[i].b) + ' ' + repr(L[i].vis) + repr(L[i].dom)
