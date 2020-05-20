
class Tile:
	sheet_x = None
	sheet_y = None

	# collisions
	coll_sides = None

	def __init__(self, sheet_x, sheet_y, south = False, east = False, west = False, north = False):
		self.coll_sides = [south, east, west, north]
		self.sheet_x = sheet_x
		self.sheet_y = sheet_y