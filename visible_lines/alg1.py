lines = [-2, -1, 0, 1, 2], [2, 1, 0, 1, 2]
num_lines = len(lines[0])

slopes = []
intercepts = []
visible = []

#For Claim 1
for i in range(0, num_lines):
	slopes.append(lines[0][i])
	intercepts.append(lines[1][i])
	visible.append(True)				#mark each line as visible

if len(slopes) < 3:
	exit()								#all lines are visible in this case

for m in range(2, num_lines):
	j = m-2
	i = m-1
	k = m 
	YjYk = slopes[j]*(intercepts[j] - intercepts[k]) 
	YiYk = slopes[i]*(intercepts[j] - intercepts[k])
	if(YjYk > YiYk):
		visible[i] = False 

print visible








	#print "y = " + repr(slopes[i]) + "x + " + repr(intercepts[i])