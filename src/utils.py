import pygame
import math
from world import sceneInstances
from pygame.locals import *
# functions

def convertCoordinates(x, y):
	return x * tile_size - math.floor(camera_x), y * tile_size - math.floor(camera_y)

def searchScene(ida):
	pass
	for s in sceneInstances.scenes:
		if s.id == ida:
			return s

def loadImage(path, scale):
	image = pygame.image.load(path)
	image = pygame.transform.scale(image, (image.get_width()*scale, image.get_height()*scale))
	return image

def drawSprite(draw_surface, set, size, screen_x, screen_y, sheet_x, sheet_y):
	draw_surface.blit(set, (screen_x, screen_y), (sheet_x * size, sheet_y * size, size, size))


# time
frame_duration = 1/30
ticks = 0
menu = False

# graphics
scale_factor = 2

tile_size = 16 * scale_factor
tile_set = loadImage("images/rpg_tileset.png", scale_factor)

char_size = 8 * scale_factor
char_set = loadImage("images/chars.png", scale_factor)

buffer = pygame.Surface((200, 200))







# general variables
actual_scene = None # set in main
player = None # set in main

WIDTH = 800
HEIGHT = 608

game_display = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF)

camera_x = 0
camera_y = 0
