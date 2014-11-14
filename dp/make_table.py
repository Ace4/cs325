from table import DPtable, DPentry, print_table
from parser import create_table_from_file
def make_path(input_table,x,y):
	if(input_table.table[x][y].prev == None):
		input_table.path.reverse()
		return input_table
	else:
		input_table.path.append(input_table.table[x][y].prev)
		make_path(input_table, input_table.table[x][y].prev[0], input_table.table[x][y].prev[1])

def make_lookup_table(input_table, row, col):
	table_length = len(input_table) 
	new_table = DPtable(table_length)
	for y in range(col,table_length):
		for x in range(row,table_length):

			if x == row and y == col:
				new_table.table[x][y].value = input_table[x][y]
				new_table.table[x][y].prev = None

			elif x == row:
				new_table.table[x][y].value = input_table[x][y] + new_table.table[x][y-1].value
				new_table.table[x][y].prev = [x,y-1]

			elif y == col:
				new_table.table[x][y].value = input_table[x][y] + new_table.table[x-1][y].value
				new_table.table[x][y].prev = [x-1,y] 

			elif input_table[x-1][y] > input_table[x][y-1]:
				new_table.table[x][y].value  = input_table[x][y] + new_table.table[x-1][y].value
				new_table.table[x][y].prev = [x-1,y]

			else:
				new_table.table[x][y].value = input_table[x][y] + new_table.table[x][y-1].value
				new_table.table[x][y].prev = [x,y-1]

			if (new_table.table[x][y].value > new_table.max_value or new_table.max_value == "-Inf") and (x == table_length-1 or y == table_length-1):				
				new_table.max_value = new_table.table[x][y].value
				new_table.max_index = [x,y]	

	new_table.path.append(new_table.max_index)	
	make_path(new_table, new_table.max_index[0], new_table.max_index[1])
	return new_table

x = [	[-1, 7,-8,10,-5],
	[-4,-9, 8,-6, 0],
	[ 5,-2,-6,-6, 7],
	[-7, 4, 7,-3,-3],
	[ 7, 1,-6, 4,-9]]
p = create_table_from_file("example-input-1.txt")
y = make_lookup_table(p,0,0)
