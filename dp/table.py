class DPentry:
	def __init__(self):
		value = None
		prev = None

class DPtable:
	def __init__(self, n):
		self.table = [[DPentry() for y in range(n)] for x in range(n)]
		self.max_value = "-Inf"
		self.max_index = []
		self.path = []
