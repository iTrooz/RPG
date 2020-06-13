import math
import utils
import pygame
from others import button, verse
from states import statesInstances
from states.state import GameState
import states

size_x = 104*utils.scale_factor
size_y = 64*utils.scale_factor
myscale = 1.5
new_x = round(size_x*myscale)
new_y = round(size_y*myscale)

inv = pygame.Surface((size_x, size_y))
inv.blit(utils.ui_set, (0, 0), (0 * utils.tile_size, 2 * utils.tile_size, size_x, size_y))
inv = pygame.transform.scale(inv, (new_x, new_y))

class InvState(GameState):

	buttons_list = []
	button_size = 16

	title = None

	def __init__(self):

		self.title = verse.decode("Le titre :)")

	def selected(self):
		pass

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)
			elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
							utils.changeState(statesInstances.play_state)


		utils.game_display.blit(inv, ((utils.WIDTH - new_x) / 2, ((utils.HEIGHT - new_y) / 2)))
