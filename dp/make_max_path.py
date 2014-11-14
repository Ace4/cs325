from table import DPtable, print_path
from make_table import make_lookup_table
from parser import create_table_from_file
def find_max_path(input_table):
	N = len(input_table)
	max_table = DPtable(N)
	max_table.max_value = "-Inf"
	for i in range(0,N):
		for j in range(0,N):
			new_table = make_lookup_table(input_table,i,j)
			if(new_table.max_value > max_table.max_value or max_table.max_value == "-Inf"):
				max_table = new_table
	return max_table

test_table1 = create_table_from_file("example-input-1.txt")
max_table1 = find_max_path(test_table1)
print max_table1.max_value
print max_table1.path_length
print_path(max_table1)

test_table2 = create_table_from_file("example-input-2.txt")
max_table2 = find_max_path(test_table2)
print max_table2.max_value
print max_table2.path_length
print_path(max_table2)

test_table3 = create_table_from_file("example-input-3.txt")
max_table3 = find_max_path(test_table3)
print max_table3.max_value
print max_table3.path_length
print_path(max_table3)
