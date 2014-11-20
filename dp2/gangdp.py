from time import clock
from random import randrange
from multiprocessing import Pool

class max_path:
	def __init__(self):
		self.path = []
		self.max_value = "-Inf"
		self.last_index = ["-Inf", "-Inf"]
	def print_path(self):
		n = len(self.path)
		for x in range(0, n):
			print(repr(self.path[x][0]) + ' ' + repr(self.path[x][1]))

def is_int(f):
	try:
		int(f)
		return True
	except ValueError:
		return False

def make_blank_table(rows, cols):
	result = []
	for x in range(0, rows):
		result.append([])
		for y in range(0, cols):
			result[x].append("-Inf")
	return result

def make_random_table(N, val_range):
	result = []
	for x in range(0, N):
		result.append([])
		for y in range(0, N):
			result[x].append(randrange(-val_range, val_range))
	return result

def make_table_from_file(fn):
	result = []
	f = open(fn)

	rows = int(f.readline())
	cols = int(f.readline())

	for x in range(0, rows):
		cur_row = f.readline().split()
		for y in range(0, cols):
			cur_row[y] = int(cur_row[y])
		result.append(cur_row)
	
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

def create_max_path(input_table, j, i):
	row_length = len(input_table[0])
	col_length = len(input_table)
	rows = row_length - i
	cols = col_length - j

	path = max_path()
	value_table = make_blank_table(rows, cols)
	path_table = make_blank_table(rows, cols)
	#Build the value table
	for y in range(0, cols):
		for x in range(0, rows):
		#	print(x, y)
			if ((x == 0) and (y == 0)):
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
	pool = Pool(N)
	path = max_path()
#	for i in range(0, N):
#		for j in range(0, N):
			#print("Creating table [" + repr(i) + ', ' + repr(j) + ']')
	new_path = [pool.apply(create_max_path, args=(input_table, i,j,)) for i in range(0,N) for j in range(0,N)]

	for i in range(0, len(new_path)):
#		print new_path[i].max_value

#		if(is_int(new_path[i].max_value) and is_int(path.max_value)):
		if(new_path[i].max_value > path.max_value):
			path = new_path[i]
			print("Found new max")
		elif(path.max_value == "-Inf"):
			path = new_path[i]
			#print("change max")

	return path

def print_solution(filename):
	A = make_table_from_file(filename)
	path = find_max_path(A)
	print(path.max_value)
	print(len(path.path))
	path.print_path()

print_solution("test3.txt") 
