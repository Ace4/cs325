from random import randrange
from time import clock

num_lines = 1000
if num_lines < 3:
	exit()								#all lines are visible in this case

slopes = []
intercepts = []
visible = []

#generate unique random lines
def genLines(n):
	for i in range(0, n):	
		rand_slope = randrange(-n,n);
		while slopes.count(rand_slope) != 0:
			rand_slope = randrange(-n,n);

		slopes.append(rand_slope)
		intercepts.append(randrange(-n, n))
		
	slopes.sort()

#For algorithm 1
def alg1(n):
	for i in range(0, n):
		visible.append(True)				#mark each line as visible

	for k in range(2, n):					#check visibility of all triplets where i<j<k
		for i in range(1, n-1):
			for j in range(0, n-2):
				if(j < i < k):
					YjYk = slopes[j]*(intercepts[j] - intercepts[k]) + intercepts[j]*(slopes[k] - slopes[j])
					YiYk = slopes[i]*(intercepts[j] - intercepts[k]) + intercepts[i]*(slopes[k] - slopes[j])
					if(YjYk > YiYk):
						visible[i] = False

genLines(num_lines)
t0 = clock()
alg1(num_lines)
t1 = clock()

print t1 - t0