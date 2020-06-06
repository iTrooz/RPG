import installer

import time
from datetime import datetime
import pygame
import utils
from states import states_instances

"""
main -> constructeurs -> instances ->  -> utils
"""


# initializing

# game updating
def gameUpdate():
	if utils.to_change is not None:
		utils.actual_state = utils.to_change
		utils.to_change = None
	utils.actual_state.update()

# main loop logic
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

	# if utils.ticks%1==0:
	# 	if delta == 0:
	# 		print("max fps : infinity")
	# 	else:
	# 		print("max fps :", int(1 / delta))


