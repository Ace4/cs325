import string

#inputs: "filename.txt"
#outputs: 2d array
def create_table_from_file(fn):
	result = []
	f = open(fn)

	rows = int(f.readline())
	cols = int(f.readline())

	for x in range(0, rows):
		result.append(f.readline().split())

	return result