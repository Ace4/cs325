import string

class DPentry:
	def __init__(self):
		self.value = "-Inf"
		self.prev = "-Inf"

class DPtable:
	def __init__(self, n):
		self.table = [[DPentry() for y in range(n)] for x in range(n)]
		self.max_value = "-Inf"
		self.max_index = []
		self.path = []
		self.path_length = 0

def is_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def make_path(input_table,x,y):
	if(input_table.table[x][y].prev == None):
		input_table.path.reverse()
		input_table.path_length = len(input_table.path)
		return input_table
	else:
		input_table.path.append(input_table.table[x][y].prev)
		make_path(input_table, input_table.table[x][y].prev[0], input_table.table[x][y].prev[1])

def make_lookup_table(input_table, row, col):
	table_length = len(input_table) 
	new_table = DPtable(table_length)
	for y in range(col, table_length):
		for x in range(row, table_length):

			if x == row and y == col:
				new_table.table[x][y].value = input_table[x][y]
				new_table.table[x][y].prev = None

			elif x == row:
				new_table.table[x][y].value = input_table[x][y] + new_table.table[x][y-1].value
				new_table.table[x][y].prev = [x,y-1]

			elif y == col:
				new_table.table[x][y].value = input_table[x][y] + new_table.table[x-1][y].value
				new_table.table[x][y].prev = [x-1,y] 

			elif new_table.table[x][y-1].value > new_table.table[x-1][y].value:
				new_table.table[x][y].value  = input_table[x][y] + new_table.table[x][y-1].value
				new_table.table[x][y].prev = [x,y-1]

			else:
				new_table.table[x][y].value = input_table[x][y] + new_table.table[x-1][y].value
				new_table.table[x][y].prev = [x-1,y]

			if (x == table_length-1 or y == table_length-1):
				if(is_int(new_table.table[x][y].value) and is_int(new_table.max_value)):
					if(new_table.table[x][y].value >= new_table.max_value):	
						new_table.max_value = new_table.table[x][y].value
						new_table.max_index = [x,y]
				elif(new_table.max_value == "-Inf"):
					new_table.max_value = new_table.table[x][y].value
					new_table.max_index = [x,y]

	new_table.path.append(new_table.max_index)	
	make_path(new_table, new_table.max_index[0], new_table.max_index[1])
	return new_table

def find_max_path(input_table):
	N = len(input_table)
	max_table = DPtable(N)
	max_table.max_value = "-Inf"
	for i in range(0,N):
		for j in range(0,N):
			new_table = make_lookup_table(input_table,i,j)
			if(is_int(new_table.max_value) and is_int(max_table.max_value)):
				if(new_table.max_value > max_table.max_value):
					max_table = new_table
			elif(max_table.max_value == "-Inf"):
				max_table = new_table
	return max_table

#input: "filename.txt"
#output: 2d array
def create_table_from_file(fn):
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

def print_path(input_table):
	n = len(input_table.path)
	for x in range(0, n):
		print(repr(input_table.path[x][0]) + ' ' + repr(input_table.path[x][1]))

#inputs: "filename.txt"
#output: answer in correct format
def print_solution(fn):
	table = create_table_from_file(fn)
	max_table = find_max_path(table)
	print(max_table.max_value)
	print(max_table.path_length)
	print_path(max_table)

print_solution('test1.txt')
#print_solution('test2.txt')
#print_solution('test3.txt')