import pygame

from entities import animation, animationInstances
import utils
from others import directions
from states import states_instances
from random import randint


class Entity:
	x = 0
	y = 0

	direction = directions.SOUTH

	def draw(self):
		pass

	def update(self):
		pass


class AliveEntity(Entity):
	animation_manager = None

	moving = False
	stop_moving = False
	moving_pixel = 0

	life = 3
	max_life = 3

	# pourcentage d'avancement d'un block par frame (0-1)
	# doit être un nombre tel que 100/x = entier
	speed = 0.2

	x = 0
	y = 0

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
		self.animation_manager.updateAnim()
		if self.moving:
			self.moving_pixel = (self.moving_pixel + self.speed * utils.tile_size) # passage 0-1 en 0-32 pour les 32 pixels du tile_size
			if self.moving_pixel>= utils.tile_size:
				self.moving_pixel = 0
				self.x+=self.direction.xy[0]
				self.y+=self.direction.xy[1]
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

	damageCounter = 0

	down_keys = [None] * 4

	def __init__(self):
		self.animation_manager = animation.AnimationManager(animationInstances.player_anim_set, "walk")

	def update(self):
		if not self.moving:
			for i in range(len(self.down_keys)):
				if self.down_keys[i] is not None:
					self.direction = self.down_keys[i]
					self.moving = True
			if self.hasCollision():
				self.moving = False
		if self.damageCounter == 0:
			for ent in utils.actual_state.actual_entities:
				if ent.x == self.x and ent.y == self.y:
					self.life -= 1
					self.damageCounter = 1
		else:
			self.damageCounter+=1
			if self.damageCounter==40:
				self.damageCounter = 0


		super().update()

		if self.moving:
			self.teleporter = None
		else:
			ctile = states_instances.play_state.actual_scene.map[self.y][self.x]
			if ctile.teleport is None:
				if utils.actual_state.alpha > 0:
					utils.actual_state.alpha -= 5
					if not utils.tp_ok:
						utils.actual_state.alpha -= 10
					if utils.actual_state.alpha < 0:
						utils.actual_state.alpha = 0
						utils.tp_ok = False
			else:
				utils.actual_state.alpha+= 5
				if utils.actual_state.alpha > 300:
					utils.actual_state.actual_scene = ctile.teleport["scene"]
					utils.tp_ok = True
					self.x = ctile.teleport["x"]
					self.y = ctile.teleport["y"]
					# CHANGE SCENE

	def draw(self):

		if self.damageCounter % 2 == 0:
			super().draw()
		# if self.anim_tp == 0:
		# 	super().draw()
		# else:
		# 	(screen_x, screen_y), sheet_x, sheet_y = super().preDraw()
		#
		# 	# super().finalDraw((screen_x, screen_y), sheet_x, sheet_y, utils.tile_size-self.anim_tp)
		# 	# super().finalDraw((screen_x, screen_y+self.anim_tp), sheet_x, sheet_y, utils.tile_size-self.anim_tp)
		#
		# 	if self.teleporter is not None and self.teleporter["scene"] == utils.actual_state.actual_scene:
		# 		screen_x, screen_y = utils.convertCoordinates(self.teleporter["x"], self.teleporter["y"])
		#
		# 		# super().finalDraw((screen_x, screen_y), sheet_x, sheet_y, self.anim_tp)
		# 		# super().finalDraw((screen_x, screen_y+(32-self.anim_tp)), sheet_x, sheet_y, self.anim_tp)

	def keyDetection(self, event):
		key = event.key
		m = directions.getByKeyName(key)
		if m is not None:
			if event.type == pygame.KEYDOWN:
				self.down_keys[m.id] = m
			else:
				self.down_keys[m.id] = None





class Snake(AliveEntity):

	def __init__(self):
		self.animation_manager = animation.AnimationManager(animationInstances.player_snake_set, "walk")

	def draw(self):
		super().draw()

	def update(self):
		if not self.moving:
			if randint(0, 3)==0:
				d = directions.getByID(randint(0, 3))
				self.direction = d
				if not self.hasCollision():
					self.moving = True

		super().update()


"""
# super().finalDraw((screen_x, screen_y), sheet_x, sheet_y, utils.tile_size-self.anim_tp)
# super().finalDraw((screen_x, screen_y+self.anim_tp), sheet_x, sheet_y, utils.tile_size-self.anim_tp)

# super().finalDraw((screen_x, screen_y), sheet_x, sheet_y, self.anim_tp)
# super().finalDraw((screen_x, screen_y+(32-self.anim_tp)), sheet_x, sheet_y, self.anim_tp)
"""