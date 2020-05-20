import time
from datetime import datetime
import pygame
import dialogs
import utils
import saver
import math
from world import sceneInstances
from entities import entities

utils.actual_scene = sceneInstances.forest
utils.player = entities.Player()


actual_entities = []


def gameUpdate():
	utils.game_display.fill((0, 0, 0))

	# manage events
	for event in pygame.event.get():
		# window quit
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		# key input
		elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE: # stv modifie
				if event.type == pygame.KEYDOWN:
					utils.menu = True
				else:
					utils.menu = False
			elif event.key == pygame.K_o:
				saver.save()
			elif event.key == pygame.K_p:
				saver.restore()

			else:
				utils.player.keyDetection(event)

	# draw map
	utils.actual_scene.draw(utils.game_display)

	# entities
	for i in actual_entities:
		i.update()
		i.draw(utils.game_display)

	# player
	utils.player.update()
	utils.player.draw(utils.game_display)

	text_x, text_y = utils.convertCoordinates(math.cos(utils.ticks / 20) + 2, math.sin(utils.ticks / 20) + 2)

	dialogs.setTextColor((255, 255, 255))
	dialogs.drawText(utils.game_display, "Salut Thomas! /?C/-omo est/-as?", text_x-utils.scale_factor, text_y)
	dialogs.drawText(utils.game_display, "Salut Thomas! /?C/-omo est/-as?", text_x+utils.scale_factor, text_y)
	dialogs.drawText(utils.game_display, "Salut Thomas! /?C/-omo est/-as?", text_x, text_y-utils.scale_factor)
	dialogs.drawText(utils.game_display, "Salut Thomas! /?C/-omo est/-as?", text_x, text_y+utils.scale_factor)
	dialogs.setTextColor((0, 0, 0))
	dialogs.drawText(utils.game_display, "Salut Thomas! /?C/-omo est/-as?", text_x, text_y)

	# camera movement
	if utils.player.moving:
		utils.camera_x += utils.player.speed * utils.player.direction.xy[0]
		utils.camera_y += utils.player.speed * utils.player.direction.xy[1]
	else:
		utils.camera_x = utils.player.x * utils.tile_size - utils.WIDTH / 2
		utils.camera_y = utils.player.y * utils.tile_size - utils.HEIGHT / 2

	# print(utils.ticks)

pygame.init()
while True:
	time_before = datetime.now()

	# update game
	utils.ticks += 1
	gameUpdate()
	pygame.display.update()

	time_after = datetime.now()

	# obtenir intervalle
	delta = (time_after-time_before).total_seconds()

	# calculer le temps à attendre et attendre si possible
	sleep_time = utils.frame_duration - delta
	if sleep_time>0:
		time.sleep(sleep_time)

	if utils.ticks%1==0:
		if delta == 0:
			print("max fps : infinity")
		else:
			print("max fps :", int(1 / delta))


