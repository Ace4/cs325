import numpy as np
from time import clock
from random import randrange

class max_path:
	def __init__(self):
		self.path = []
		self.max_value = "-Inf"
		self.last_index =["-Inf", "-Inf"]

def print_path(self):
	n = len(self.path)
	for x in range(0,n):
		print(repr(self.path[x][0]) + ' ' + repr(self.path[x][1]))

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
def make_random_table(N, val_range):
        result = []
        for x in range(0, N):
                result.append([])
                for y in range(0, N):
                        result[x].append(randrange(-val_range, val_range))
        return result

def get_timing(table):
        t0 = clock()
        find_max_path(table)
        t1 = clock()
        print(repr(len(table)) + ', ' + repr(t1-t0))

def get_running_times(start, end, step):
        for N in range(start, end, step):
                A = make_random_table(N, 100)
                get_timing(A)


def make_blank_table(rows, cols):
        result = []
        for x in range(0, rows):
                result.append([])
                for y in range(0, cols):
                        result[x].append("-Inf")
        return result


def is_int(f):
	try:	
		int(f)
		return True
	except ValueError:
		return False

def create_max_path(input_table, i,j):
	row_length = len(input_table[0])
	col_length = len(input_table)
	rows = row_length - i
	cols = col_length - j
	path = max_path()
	value_table = np.zeros((rows, cols), dtype=object)
	path_table = np.zeros((rows,cols), dtype=object)
	#Build the value table
	for y in range(0, cols):
		for x in range(0,rows):
			if((x == 0) and (y == 0)):
				value_table[x][y] = input_table[i+x][j+y]
				path_table[x][y] = None
			elif(x == 0):
                                value_table[x][y] = input_table[i+x][j+y] + value_table[x][y-1]
                                path_table[x][y] = [x,y-1]
                        elif(y == 0):
                                value_table[x][y] = input_table[i+x][j+y] + value_table[x-1][y]
                                path_table[x][y] = [x-1,y]
                        elif(value_table[x][y-1] > value_table[x-1][y]):
                                value_table[x][y] = input_table[i+x][j+y] + value_table[x][y-1]
                                path_table[x][y] = [x,y-1]
                        else:
                                value_table[x][y] = input_table[i+x][j+y] + value_table[x-1][y]
			        path_table[x][y] = [x-1,y]
                        if((x == rows-1) or (y == cols-1)):
                                if(is_int(value_table[x][y]) and is_int(path.max_value)):
                                        if(value_table[x][y] >= path.max_value):
                                                path.max_value = value_table[x][y]
                                                path.last_index = [x, y]
                                elif(path.max_value == "-Inf"):
                                        path.max_value = value_table[x][y]
                                        path.last_index = [x, y]

        #Retrieve the path
        path.path.append([path.last_index[0]+i, path.last_index[1]+j])
        index = path_table[path.last_index[0]][path.last_index[1]]
        while(index != None):
                path.path.insert(0, [index[0]+i, index[1]+j])
                index = path_table[index[0]][index[1]]
        return path

def find_max_path(input_table):
        N = len(input_table)
        path = max_path()
        for i in range(0, N):
                for j in range(0, N):
                        #print("Creating table [" + repr(i) + ', ' + repr(j) + ']')
                        new_path = create_max_path(input_table, i, j)
                        if(is_int(new_path.max_value) and is_int(path.max_value)):
                                if(new_path.max_value > path.max_value):
                                        path = new_path
                                        #print("Found new max")
                        elif(path.max_value == "-Inf"):
                                path = new_path

        return path


#A = make_table_from_file('example-input-2.txt')
#B = find_max_path(A)
get_running_times(5, 100, 5)
#print(B.max_value)
