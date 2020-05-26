import pygame

from entities import animation, animationInstances
import utils
from others import directions
from states import states_instances


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
	speed = 0.4

	down_keys = [None] * 4

	x = 13
	y = 10

	def preDraw(self):
		# transform coordinates
		screen_x, screen_y = utils.convertCoordinates(self.x, self.y)
		if self.moving:
			screen_x += self.moving_pixel * self.direction.xy[0]
			screen_y += self.moving_pixel * self.direction.xy[1]
		# get sprite
		sheet_x, sheet_y = self.animation_manager.getSpritePos(self.direction)
		# draw
		return (screen_x, screen_y), sheet_x, sheet_y

	def finalDraw(self, screen, sheet_x, sheet_y, ysize=utils.tile_size):
		utils.game_display.blit(utils.tile_set, screen, (sheet_x * utils.tile_size, sheet_y * utils.tile_size, utils.tile_size, ysize))


	def draw(self):
		screen, sheet_x, sheet_y = self.preDraw()
		self.finalDraw(screen, sheet_x, sheet_y)

	"""ENTITY MOVEMENT"""

	def update(self):
		super().update()
		if self.moving:
			self.moving_pixel = (self.moving_pixel + self.speed * utils.tile_size) # passage 0-1 en 0-32 pour les 32 pixels du tile_size
			if self.moving_pixel>= utils.tile_size:
				self.moving_pixel = 0
				self.x+=self.direction.xy[0]
				self.y+=self.direction.xy[1]
				self.moving = False

		if not self.moving:
			for i in range(len(self.down_keys)):
				if self.down_keys[i] is not None:
					self.direction = self.down_keys[i]
					self.moving = True
			if self.moving and self.hasCollision():
				self.moving = False

	def hasCollision(self):
		# 3- pour faire l'inverse

		# test si on peut sortir de la case actuelle
		ctile = states_instances.play_state.actual_scene.map[self.y][self.x]
		if ctile.coll_sides[self.direction.id]:
			return True

		# obtenir la position de la prochaine case
		nx, ny  = self.x + self.direction.xy[0], self.y + self.direction.xy[1]

		# test si la prochaine case est dans la carte
		if nx < 0 or nx == states_instances.play_state.actual_scene.map_width or ny < 0 or ny == states_instances.play_state.actual_scene.map_height:
			return True

		# test si on peut entrer dans la prochaine case
		ctile = states_instances.play_state.actual_scene.map[ny][nx]
		if ctile.coll_sides[3 - self.direction.id]:
			return True

		# aucune collision prévue
		return False


class Player(AliveEntity):

	anim_tp = 0
	teleporter = None

	def __init__(self):
		self.animation_manager = animation.AnimationManager(animationInstances.player_anim_set, "walk")

	def update(self):
		super().update()
		if self.moving:
			self.teleporter = None
		else:
			ctile = states_instances.play_state.actual_scene.map[self.y][self.x]
			if ctile.teleport is not None:
				self.teleporter = ctile.teleport
				self.anim_tp+=1

				if ctile.teleport["scene"] == states_instances.play_state.actual_scene:
					pass # je le ferai plus tard

				if self.anim_tp==utils.tile_size:
					self.anim_tp = 0
					self.teleporter = None
					if ctile.teleport["scene"] == states_instances.play_state.actual_scene:
						pass
					self.x = ctile.teleport["x"]
					self.y = ctile.teleport["y"]

			if self.teleporter is None and self.anim_tp > 0:
				self.anim_tp -= 3
				if self.anim_tp < 0:
					self.anim_tp = 0
		self.animation_manager.updateAnim()

	def draw(self):

		if self.anim_tp == 0:
			super().draw()
		else:
			(screen_x, screen_y), sheet_x, sheet_y = super().preDraw()

			super().finalDraw((screen_x, screen_y), sheet_x, sheet_y, utils.tile_size-self.anim_tp)
			# super().finalDraw((screen_x, screen_y+self.anim_tp), sheet_x, sheet_y, utils.tile_size-self.anim_tp)

			if self.teleporter is not None and self.teleporter["scene"] == utils.actual_state.actual_scene:
				screen_x, screen_y = utils.convertCoordinates(self.teleporter["x"], self.teleporter["y"])

				super().finalDraw((screen_x, screen_y), sheet_x, sheet_y, self.anim_tp)
				# super().finalDraw((screen_x, screen_y+(32-self.anim_tp)), sheet_x, sheet_y, self.anim_tp)

	def keyDetection(self, event):
		key = event.key
		m = directions.getByKeyName(key)
		if m is not None:
			if event.type == pygame.KEYDOWN:
				self.down_keys[m.id] = m
			else:
				self.down_keys[m.id] = None