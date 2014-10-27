class Line:
	def __init__(self, slope, intercept, visible, domain):
		self.m = slope
		self.b = intercept
		self.visible = visible
		self.domain = domain

# x = Line(.45, 5, True, [0,0])
# x.b