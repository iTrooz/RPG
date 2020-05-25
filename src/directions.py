import pygame


class Direction:
	id = None
	xy = (0, 0)
	key = None

	def __init__(self, ida, xy, key):
		self.id = ida
		self.xy = xy
		self.key = key

SOUTH = Direction(0, (0, 1), pygame.K_DOWN)
WEST = Direction(1, (-1, 0), pygame.K_LEFT)
EAST = Direction(2, (1, 0), pygame.K_RIGHT)
NORTH = Direction(3, (0, -1), pygame.K_UP)

directs = [SOUTH,WEST,NORTH,EAST]

def getByID(ida):
	for d in directs:
		if d.id==ida:
			return d

def getByKeyName(key_name):
	for d in directs:
		if d.key==key_name:
			return d
