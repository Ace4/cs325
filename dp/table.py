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
