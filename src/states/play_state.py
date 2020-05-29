import pygame
from others import saver, dialogs
import math
from states.state import GameState
from world import sceneInstances
from entities import entities
import utils


class PlayState(GameState):

	camera_x = 0
	camera_y = 0

	actual_entities = []

	actual_scene = None
	player = None
	actual_scene = None # set in utils

	alpha = 0

	# -------------------------------- #

	def __init__(self):
		self.player = entities.Player()
		self.player.x = 13
		self.player.y = 10

		self.actual_entities.append(entities.Snake())

	def selected(self):
		pass

	def update(self):
		utils.game_display.fill((0, 0, 0))

		# update
		handleEvents(self)
		self.player.update()
		updateCameraToPlayer(self)
		for i in self.actual_entities:
			i.update()

		# draw
		self.actual_scene.draw()
		self.player.draw()
		for i in self.actual_entities:
			i.draw()
		for i in range(self.player.max_life):
			if (i > self.player.life):
				shift = 1
			else:
				shift = 0
			utils.drawSprite(utils.ui_set, utils.ui_size, 16 + i*utils.ui_size*1.5, 16, shift, 0)

		s = pygame.Surface((utils.WIDTH, utils.HEIGHT), pygame.SRCALPHA)  # per-pixel alpha
		alpha = self.alpha
		if alpha > 255:
			alpha = 255
		s.fill((0, 0, 0, alpha))  # notice the alpha value in the color
		utils.game_display.blit(s, (0, 0))




def handleEvents(play_state):
	for event in pygame.event.get():
		# window quit
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		# key input
		elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				if event.type == pygame.KEYDOWN:
					utils.menu = True
				else:
					utils.menu = False
			elif event.key == pygame.K_o:
				saver.save()
			elif event.key == pygame.K_p:
				saver.restore()
			else:
				play_state.player.keyDetection(event)

def updateCameraToPlayer(play_state):
	# get the screen position of the tile where the player is standing on
	player_tile_x = play_state.player.x * utils.tile_size - utils.WIDTH / 2
	player_tile_y = play_state.player.y * utils.tile_size - utils.HEIGHT / 2

	# then add with the advancement of the player sliding
	play_state.camera_x = player_tile_x + play_state.player.moving_pixel * play_state.player.direction.xy[0] - utils.tile_size / 2
	play_state.camera_y = player_tile_y + play_state.player.moving_pixel * play_state.player.direction.xy[1] - utils.tile_size / 2

	# utils.camera_x = 0
	# utils.camera_y = 0








