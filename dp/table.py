class DPentry:
	value = None
	prev = None

class DPtable:
	def __init__(self, n):
		self.table = [[DPentry for x in xrange(n)] for x in xrange(n)]
		self.max_value = "-Inf"
		self.max_index = []
		self.path = []