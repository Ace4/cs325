lines = [-980, -979, -891, -887, -858, -845, -782, -759, -757, -731, -711, -700, -678, -671, -650, -569, -553, -549, -538, -528, -519, -490, -460, -455, -447, -446, -442, -409, -398, -354, -348, -338, -278, -273, -272, -237, -227, -209, -196, -188, -138, -120, -119, -103, -70, -56, -53, -37, -29, -22, -17, 16, 20, 43, 80, 97, 112, 134, 171, 204, 219, 222, 245, 277, 295, 332, 341, 407, 433, 435, 468, 472, 478, 481, 509, 519, 520, 521, 544, 555, 562, 596, 600, 603, 611, 632, 642, 648, 667, 697, 709, 770, 789, 827, 852, 899, 912, 913, 965, 993], [177, -667, -222, -22, 916, 568, -9, 40, 83, -728, -345, 834, 386, -565, 735, -229, -974, 373, 951, 959, -578, 799, -280, 819, 96, -935, 285, -482, -814, 9, 306, -88, 903, -719, 365, -755, -976, 751, 472, -94, -623, 645, -677, 815, 877, 635, -439, -129, -697, -429, 695, -903, -947, -406, -56, 237, 879, 3, 183, 472, 567, -397, -577, 524, -81, 992, 671, -277, -686, 978, 268, 224, 838, 691, 729, 234, 411, 942, 356, -271, 545, 604, -488, -824, -111, 837, -110, -876, 43, -120, 856, -857, 10, 61, 720, 140, 270, 995, -796, -5]
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

for k in range(2, num_lines):			#check visibility of all triplets where i<j<k
	for i in range(1, num_lines-1):
		if visible[i]:					#stop testing if line has already been marked not visible
			for j in range(0, num_lines-2):
				if(j < i < k):
					YjYk = slopes[j]*(intercepts[j] - intercepts[k]) + intercepts[j]*(slopes[k] - slopes[j])
					YiYk = slopes[i]*(intercepts[j] - intercepts[k]) + intercepts[i]*(slopes[k] - slopes[j])
					if(YjYk > YiYk):
						visible[i] = False

print visible