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

def print_table(input_table):
	n = len(input_table[0])
	table = []
	row = []
	for x in range(0, n):
		for y in range(0, n):
			row.append(input_table[x][y].value)
		table.append(row)
		row = []
	print(table)

def print_path(input_table):
	n = len(input_table.path)
	for x in range(0, n):
		print repr(input_table.path[x][0]) + ' ' + repr(input_table.path[x][1])
