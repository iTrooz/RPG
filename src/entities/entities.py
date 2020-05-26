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


class AliveEntity(Entity):
	animation_manager = None

	moving = False
	stop_moving = False
	moving_pixel = 0

	# pourcentage d'avancement d'un block par frame (0-1)
	# doit être un nombre tel que 100/x = entier
	speed = 0.2

	down_keys = [None] * 4

	x = 13
	y = 10

	def draw(self):
		# transform coordinates
		screen_x, screen_y = utils.convertCoordinates(self.x, self.y)
		if self.moving:
			screen_x += self.moving_pixel * self.direction.xy[0]
			screen_y += self.moving_pixel * self.direction.xy[1]
		# get sprite
		sheet_x, sheet_y = self.animation_manager.getSpritePos(self.direction)
		# draw
		utils.game_display.blit(utils.tile_set, (screen_x, screen_y), (sheet_x * utils.tile_size, sheet_y * utils.tile_size, utils.tile_size, utils.tile_size))

	"""ENTITY MOVEMENT"""

	def update(self):
		super().update()
		if self.moving:
			self.moving_pixel = (self.moving_pixel+self.speed*utils.tile_size) # passage 0-1 en 0-32 pour les 32 pixels du tile_size
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

		# test si on peut sortir de la case actuelle
		ctile = utils.play_state.actual_scene.map[self.y][self.x]
		if ctile.coll_sides[self.direction.id]:
			return True

		# obtenir la position de la prochaine case
		nx, ny  = self.x + self.direction.xy[0], self.y + self.direction.xy[1]

		# test si la prochaine case est dans la carte
		if nx < 0 or nx == utils.play_state.actual_scene.map_width or ny < 0 or ny == utils.play_state.actual_scene.map_height:
			return True

		# test si on peut entrer dans la prochaine case
		ctile = utils.play_state.actual_scene.map[ny][nx]
		if ctile.coll_sides[3 - self.direction.id]:
			return True

		# aucune collision prévue
		return False


class Player(AliveEntity):

	def __init__(self):
		self.animation_manager = animation.AnimationManager(animationInstances.player_anim_set, "walk")

	def update(self):
		super().update()
		self.animation_manager.updateAnim()

	def draw(self):
		super().draw()

	def keyDetection(self, event):
		key = event.key
		m = directions.getByKeyName(key)
		if m is not None:
			if event.type == pygame.KEYDOWN:
				self.down_keys[m.id] = m
			else:
				self.down_keys[m.id] = None