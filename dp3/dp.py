import numpy as np
from time import clock

def make_table_from_file(fn):
	f = open(fn)
	rows = int(f.readline())
	cols = int(f.readline())

	result = np.array([f.readline().split()], dtype=np.int32)
	for x in range(1, rows):
		row = f.readline().split()
		nprow = np.array([row], dtype=np.int32)
		result = np.concatenate((result, nprow), axis=0)
	return result

A = make_table_from_file('example-input-2.txt')
print(A)