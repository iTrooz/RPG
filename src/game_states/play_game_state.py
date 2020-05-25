import utils
import dialogs
import pygame
import saver
import math
from game_states.game_state import GameState
from world import sceneInstances
from entities import entities


class PlayGameState(GameState):

	camera_x = 0
	camera_y = 0

	actual_entities = []

	actual_scene = None
	player = None

	world_ticks = 0

	but = dialogs.Button(20, 20, 7, 0, 2)

	# -------------------------------- #

	def __init__(self):
		self.actual_scene = sceneInstances.forest
		self.player = entities.Player()

	def selected(self):
		pass

	def update(self):
		self.world_ticks += 1

		# updating
		handleEvents(self)
		self.player.update()
		for i in self.actual_entities:
			i.update()
		updateCameraToPlayer(self)

		# drawing
		utils.game_display.fill((0, 0, 0))
		self.actual_scene.draw(self)
		for i in self.actual_entities:
			i.draw()
		self.player.draw()

		# text example
		text_x, text_y = utils.convertCoordinates(math.cos(self.world_ticks / 20) + 2, math.sin(self.world_ticks / 20) + 2)
		dialogs.setTextColor((255, 255, 255))
		dialogs.drawText("Salut Thomas! /?C/-omo est/-as?", text_x - utils.scale_factor, text_y)
		dialogs.drawText("Salut Thomas! /?C/-omo est/-as?", text_x + utils.scale_factor, text_y)
		dialogs.drawText("Salut Thomas! /?C/-omo est/-as?", text_x, text_y - utils.scale_factor)
		dialogs.drawText("Salut Thomas! /?C/-omo est/-as?", text_x, text_y + utils.scale_factor)
		dialogs.setTextColor((0, 0, 0))
		dialogs.drawText("Salut Thomas! /?C/-omo est/-as?", text_x, text_y)

		# button example
		self.but.update()

		self.but.draw()
		dialogs.setTextColor((190, 100, 20))
		dialogs.drawText("Bouton", self.but.x+8, self.but.y+6)
		dialogs.setTextColor((255, 255, 255))
		dialogs.drawText("Bouton", self.but.x+8, self.but.y+8)




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
	play_state.camera_x = player_tile_x + play_state.player.moving_pixel*play_state.player.direction.xy[0] - utils.tile_size/2
	play_state.camera_y = player_tile_y + play_state.player.moving_pixel*play_state.player.direction.xy[1] - utils.tile_size/2

	# utils.camera_x = 0
	# utils.camera_y = 0








