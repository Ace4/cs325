import string

#inputs: "filename.txt"
#outputs: 2d array
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