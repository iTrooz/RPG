import utils
import pygame

class Tile:
	sheet_x = None
	sheet_y = None

	# collisions
	coll_sides = None

	def __init__(self, sheet_x, sheet_y, south = False, west = False, east = False, north = False):
		self.coll_sides = [south, west, east, north]
		self.sheet_x = sheet_x
		self.sheet_y = sheet_y

	def copy(self):
		a = object.__new__(Tile)
		a.__dict__ = self.__dict__.copy()
		return a