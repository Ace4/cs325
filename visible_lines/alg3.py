from random import randrange
from time import clock 

num_lines = 3000
#if num_lines < 3:
#	exit() 

slopes = []
intercepts = []
visible = [] 

#generate unique random lines
def genLines(n):
        for i in range(0, n):
                rand_slope = randrange(-n,n);
                while slopes.count(rand_slope) != 0:
                        rand_slope = randrange(-n,n)

                slopes.append(rand_slope)
                intercepts.append(randrange(-n, n))

        slopes.sort()


#for the one true wizard 
def alg1(n):
	for i in range(0,n):
		visible.append(True)

	for n in range(2, n): 
		j = n-2
		i = n-1
		k = n
	
		YjYk = slopes[j]*(intercepts[j] - intercepts[k]) + intercepts[j]*(slopes[k] - slopes[j])
		YiYk = slopes[i]*(intercepts[j] - intercepts[k]) + intercepts[i]*(slopes[k] - slopes[j])
	
		if(YjYk > YiYk):
			visible[i] = False 

def alg2(n):
        for k in range(2, n):                                   #check visibility of all triplets where i<j<k
                for i in range(1, n-1):
                        if visible[i]:
                                for j in range(0, n-2):
                                        if(j < i < k):
                                                YjYk = slopes[j]*(intercepts[j] - intercepts[k]) + intercepts[j]*(slopes[k] - slopes[j])
                                                YiYk = slopes[i]*(intercepts[j] - intercepts[k]) + intercepts[i]*(slopes[k] - slopes[j])
                                                if(YjYk > YiYk):
                                                        visible[i] = False


while num_lines in range(0,20001):
	genLines(num_lines)
	t0 = clock()
	alg1(num_lines)
	alg2(num_lines)
	t1 = clock()

	slopes = []
	intercepts = [] 
	visible = []
		
	print num_lines 
	print t1 - t0
	num_lines += 100
