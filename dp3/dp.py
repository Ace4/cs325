import numpy as np
from time import clock

rows = 10000
cols = 10000

def make_blank_table(rows, cols):
	result = []
	for x in range(0, rows):
		result.append([])
		for y in range(0, cols):
			result[x].append(0)
	return result

t0 = clock()
x = np.zeros((rows, cols))
t1 = clock()
print('numpy: ' + repr(t1-t0))