import utils
import math

class Scene:
	map_width = 16
	map_height = 16
	map = []

	def __init__(self, ida):
		self.id = ida


	def draw(self, draw_surface):

		# définir la zone que la caméra voit
		box_x = math.floor(utils.camera_x / utils.tile_size)
		box_y = math.floor(utils.camera_y / utils.tile_size)
		box_w = math.floor(utils.WIDTH / utils.tile_size)+1
		box_h = math.floor(utils.HEIGHT / utils.tile_size)+1


		# pour chaque coordonnée visible par la caméra
		for i in range(box_w):
			for j in range(box_h):
				x = box_x + i
				y = box_y + j

				# passer si il ne contient pas une case de la carte
				if y<0 or y>=len(self.map):
					continue
				if x<0 or x>=len(self.map[y]):
					continue

				# sinon dessiner la tuile
				tile_type = self.map[y][x]
				screen_x, screen_y = utils.convertCoordinates(x, y)
				utils.drawSprite(draw_surface, utils.tile_set, utils.tile_size, screen_x, screen_y, tile_type.sheet_x, tile_type.sheet_y)









