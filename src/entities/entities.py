import pygame

from entities import animation, animationInstances
import utils
from others import directions
from states import statesInstances
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

	player = False

	animation_manager = None
	moving = False
	stop_moving = False
	moving_pixel = 0

	life = 3
	max_life = 3
	damageCounter = 0

	# pourcentage d'avancement d'un block par frame (0-1)
	# doit être un nombre tel que 100/x = entier
	speed = 0.2

	x = 0
	y = 0

	def draw(self):
		# transform coordinates
		if self.damageCounter % 2 == 0:
			screen_x, screen_y = utils.convertCoordinates(self.x, self.y)
			if self.moving:
				screen_x += self.moving_pixel * self.direction.x
				screen_y += self.moving_pixel * self.direction.y
			# get sprite
			sheet_x, sheet_y = self.animation_manager.getSpritePos(self.direction)
			# draw
			utils.game_display.blit(utils.tile_set, (screen_x, screen_y), (sheet_x * utils.tile_size, sheet_y * utils.tile_size, utils.tile_size, utils.tile_size))

	"""ENTITY MOVEMENT"""

	def update(self):
		super().update()

		if self.damageCounter != 0:
			self.damageCounter += 1
			if self.damageCounter == 40:
				self.damageCounter = 0

		self.animation_manager.updateAnim()
		if self.moving:
			self.moving_pixel = (self.moving_pixel + self.speed * utils.tile_size) # passage 0-1 en 0-32 pour les 32 pixels du tile_size
			if self.moving_pixel>= utils.tile_size:
				self.moving_pixel = 0
				self.x+=self.direction.x
				self.y+=self.direction.y
				self.moving = False

	def hasCollision(self):
		# 3-x pour faire l'inverse

		# test si on peut sortir de la case actuelle
		ctile = statesInstances.play_state.actual_scene.map[self.y][self.x]
		if ctile.coll_sides[self.direction.id]:
			return True

		# obtenir la position de la prochaine case
		nx, ny  = self.x + self.direction.x, self.y + self.direction.y

		# test si la prochaine case est dans la carte
		if nx < 0 or nx == statesInstances.play_state.actual_scene.map_width or ny < 0 or ny == statesInstances.play_state.actual_scene.map_height:
			return True

		# test si on peut entrer dans la prochaine case
		ctile = statesInstances.play_state.actual_scene.map[ny][nx]
		if ctile.coll_sides[3 - self.direction.id]:
			return True

		# aucune collision prévue
		return False

	def hit(self):
		self.life -= 1
		if self.life==0:
			if self.player :
				utils.actual_state = statesInstances.menu_state
			else:
				statesInstances.play_state.actual_scene.actual_entities.remove(self)
		else:
			self.damageCounter = 1


class Player(AliveEntity):

	player = True

	anim_tp = 0

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
			for ent in statesInstances.play_state.actual_scene.actual_entities:
				if ent.x == self.x and ent.y == self.y:
					self.hit()


		super().update()

		if self.moving:
			self.teleporter = None
		else:
			ctile = statesInstances.play_state.actual_scene.map[self.y][self.x]
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
		super().draw()

	def keyDetection(self, event):
		key = event.key
		m = directions.getByKeyName(key)
		if m is not None:
			if event.type == pygame.KEYDOWN:
				self.down_keys[m.id] = m
			else:
				self.down_keys[m.id] = None
		elif event.type == pygame.KEYDOWN:
			if key == pygame.K_SPACE:
					nx, ny = (self.x+self.direction.x, self.y+self.direction.y)
					ctile = statesInstances.play_state.actual_scene.map[ny][nx]
					if ctile.content is not None:
						statesInstances.inv_state.othercontent = ctile.content
						utils.changeState(statesInstances.inv_state)
					else:
						for ent in statesInstances.play_state.actual_scene.actual_entities:
							if ent.x == nx and ent.y == ny:
								ent.hit()








class Snake(AliveEntity):

	def __init__(self):
		self.animation_manager = animation.AnimationManager(animationInstances.player_snake_set, "walk")

	def draw(self):
		super().draw()

	def update(self):
		if not self.moving:
			if randint(0, 10)==0:
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