import math
import utils
import pygame
from others import button, verse
from states.state import GameState
import states
import entities

def play_listener():
	states.states_instances.play_state = states.play_state.PlayState()
	utils.changeState(states.states_instances.play_state)


class MenuState(GameState):

	buttons_list = []
	button_size = 16

	settings_buttons_list = []

	title = None

	def __init__(self):
		# blueprint = [
		# 	"Jugar", lambda: utils.changeState(states.states_instances.play_state),
		# 	"Salir", lambda: exit(),
		# ]


		elements_pos_x = (utils.WIDTH - utils.ui_size * self.button_size) / 2

		play_button = button.Button(utils.getDialogue("play"), elements_pos_x, 128, self.button_size)
		play_button.listener = play_listener
		self.buttons_list.append(play_button)

		exit_button = button.Button(utils.getDialogue("exit"), elements_pos_x, 128+utils.ui_size*2, self.button_size)
		exit_button.listener = exit
		self.buttons_list.append(exit_button)

		settings_button = button.Button(utils.getDialogue("menu"), elements_pos_x, 128 + utils.ui_size * 2, self.button_size)
		settings_button.listener = None
		self.buttons_list.append(settings_button)


		self.title = verse.decode("Le titre :)")

	def selected(self):
		pass

	def update(self):
		utils.game_display.fill((38, 12, 38))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)

		for b in self.buttons_list:
			b.updateWithMouse()
			b.draw()

		verse.draw(self.title, (utils.WIDTH - utils.ui_size * len(self.title)) / 2, 32 + math.cos(utils.ticks*0.1)*8)

# def create_button_list(blueprint, button_size, but_pos_step, but_pos_x, but_pos_y):
# 	buttons_list = []
# 	# fill list
# 	i = 0
# 	while (i < len(blueprint)):
# 		buttons_list.append(
# 			button.Button(but_pos_x, but_pos_y + but_pos_step * i, blueprint[i], button_size, blueprint[i + 1]))
# 		i += 2
# 	return buttons_list
