import pygame
import math
from others import dialogs_instances

"""BASE"""

"""FUNCTIONS"""

def loadImage(path, scale):
	image = pygame.image.load(path)
	image = pygame.transform.scale(image, (image.get_width()*scale, image.get_height()*scale))
	return image

def drawSprite(sprite_set, sprite_size, screen_x, screen_y, sheet_x, sheet_y, sheet_w=1, sheet_h=1):
	game_display.blit(sprite_set, (math.floor(screen_x), math.floor(screen_y)), (sheet_x * sprite_size, sheet_y * sprite_size, sheet_w * sprite_size, sheet_h * sprite_size))

to_change = None

def changeState(new_state):
	global actual_state
	global to_change
	if actual_state != new_state:
		to_change = new_state

def getDialogue(dialogue_name):
	return dialogs_instances.languages[language][dialogue_name]

"""VARIABLES"""

tp_ok =  False

# time
frame_duration = 1/30
ticks = 0

# graphic resources
scale_factor = 2

tile_size = 16 * scale_factor
tile_set = loadImage("images/tile_set.png", scale_factor)

char_size = 8 * scale_factor
char_set = loadImage("images/chars_set.png", scale_factor)

ui_size = 8 * scale_factor
ui_set = loadImage("images/ui_set.png", scale_factor)

# display
WIDTH = 800
HEIGHT = 608
game_display = pygame.display.set_mode((WIDTH, HEIGHT))

language = "english"

"""IG USE"""

from world import sceneInstances
from states import states_instances


"""FUNCTIONS"""
def convertCoordinates(x, y):
	return x * tile_size - math.floor(states_instances.play_state.camera_x), y * tile_size - math.floor(states_instances.play_state.camera_y)


def searchScene(ida):
	pass
	for s in sceneInstances.scenes:
		if s.id == ida:
			return s

"""VARIABLES"""

actual_state = states_instances.menu_state