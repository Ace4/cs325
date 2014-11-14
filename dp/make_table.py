from table import DPtable, DPentry 

def make_lookup_table(input_table, row, col):
	table_length = len(input_table) 
	new_table = DPtable(table_length)
	new_table.maxvalue = "-inf"
	for y in range(col,table_length):
		for x in range(row,table_length):
			if x == row and y == col:
				new_table.table[x][y].value = input_table[x][y]
				new_table.table[x][y].prev = None
			elif x == row:
				new_table.table[x][y].value = input_table[x][y]
				new_table.table[x][y].prev = [x-1,y]
			elif y == col:
				new_table.table[x][y].value = input_table[x][y]
				new_table.table[x][y].prev = [x,y-1]
			elif input_table[x-1][y] > input_table[x][y-1]:
				new_table.table[x][y].value  = input_table[x][y] + input_table[x-1][y]
				new_table.table[x][y].prev = [x-1,y]
			else:
				new_table.table[x][y].value = input_table[x][y] + input_table[x][y-1]
				new_table.table[x][y].prev = [x,y-1]
			if new_table.table[x][y].value > new_table.max_value or new_table.max_value == "-Inf":				
				new_table.max_value = new_table.table[x][y].value
	return new_table

x = [	[-1, 7,-8,10,-5],
	[-4,-9, 8,-6, 0],
	[ 5,-2,-6,-6, 7],
	[-7, 4, 7,-3,-3],
	[ 7, 1,-6, 4,-9]]

y = make_lookup_table(x,0,0)
print y.table[0][0].value
print x[0][0]
