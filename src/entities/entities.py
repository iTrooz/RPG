import pygame

from entities import animation, animationInstances
import utils
import directions


class Entity:

	x = 0
	y = 0

	direction = directions.SOUTH

	def update(self):
		pass


# Player / Monster / NPC / ...
class AliveEntity(Entity):
	movement_speed = 10
	animation_manager = None

	moving = False
	stop_moving = False
	moving_pixel = 0
	# pixels par frame
	speed = utils.tile_size / 10

	down_keys = [None] * 4

	x = 12
	y = 9

	def draw(self, draw_surface):
		# transform coordinates
		screen_x, screen_y = utils.convertCoordinates(self.x, self.y)
		if self.moving:
			screen_x += self.moving_pixel * self.direction.xy[0]
			screen_y += self.moving_pixel * self.direction.xy[1]
		# get sprite
		sheet_x, sheet_y = self.animation_manager.getSpritePos(self.direction)
		# draw
		draw_surface.blit(utils.tile_set, (screen_x, screen_y), (sheet_x * utils.tile_size, sheet_y * utils.tile_size, utils.tile_size, utils.tile_size))




	"""ENTITY MOVEMENT"""

	def update(self):
		super().update()
		if self.moving:
			self.moving_pixel+=self.speed
			if self.moving_pixel>= utils.tile_size:
				self.moving_pixel = 0
				self.x+=self.direction.xy[0]
				self.y+=self.direction.xy[1]

				self.moving = False

		else:
			for i in range(len(self.down_keys)):
				if self.down_keys[i] is not None:
					self.direction = self.down_keys[i]
					self.moving = True
			if self.moving and self.hasCollision():
				self.moving = False

	def hasCollision(self):
		# 3- pour faire l'inverse

		ctile = utils.actual_scene.map[self.y][self.x]
		if ctile.coll_sides[self.direction.id]:
			return True

		ny, nx = self.y + self.direction.xy[1], self.x + self.direction.xy[0]

		if nx < 0 or nx == utils.actual_scene.map_width or ny < 0 or ny == utils.actual_scene.map_height:
			return True

		ctile = utils.actual_scene.map[ny][nx]
		if ctile.coll_sides[3 - self.direction.id]:
			return True

		return False

	# def move(self):
	# 	if not self.moving:
	# 		if not self.hasCollision():
	# 			self.moving = True




class Player(AliveEntity):

	def __init__(self):
		self.animation_manager = animation.AnimationManager(animationInstances.player_anim_set, "walk")

	def update(self):
		super().update()
		self.animation_manager.updateAnim()

	def draw(self, draw_surface):
		super().draw(draw_surface)

	def keyDetection(self, event):
		key = event.key
		m = directions.getByKeyName(key)
		if m is not None:
			if event.type == pygame.KEYDOWN:
				self.down_keys[m.id] = m
			else:
				self.down_keys[m.id] = None