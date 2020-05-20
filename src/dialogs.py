import utils
import pygame

actual_color = (255, 255, 255)
pixels = None


def setTextColor(new_color):
	global actual_color
	if new_color!=actual_color:
		pixels = pygame.PixelArray(utils.char_set)
		pixels.replace(actual_color, new_color)
		pixels.close()
		actual_color = new_color
		del pixels

def drawText(draw_surface, text, x, y):
	screen_x = x
	screen_y = y

	i = 0

	special = ""

	# while (i<len(text)):
	# 	c = text[i]
	# 	k = ord(c)
	# 	val = 95
	#
	# 	# gestion caractere special
	# 	if special != "":
	#
	# 		if c == '/':
	# 			val = 15
	# 			special = ""
	# 		elif k > 31 and k < 127 and c.isalpha():
	# 			val = k + 32
	# 			special = ""
	#
	# 	# indication caractere special
	# 	elif c == '/':
	# 		special = "/"
	# 	# caractere normal
	# 	else:
	# 		if k > 31 and k < 127:
	# 			val = k - 32
	#
	# 	if special=="":
	# 		drawChar(draw_surface, screen_x, screen_y, val)
	# 		screen_x += utils.char_size
	#
	# 	i+=1

	while (i<len(text)):
		c = text[i]
		k = ord(c)
		val = 95

		# caractere special
		if c == '/':
			val, y = decodeSpecialChar(text[i:])
			i+=y
		# caractere normal
		else:
			if k > 31 and k < 127:
				val = k - 32

		drawChar(draw_surface, screen_x, screen_y, val)
		screen_x += utils.char_size

		i+=1

def decodeSpecialChar(text):
	val = 95

	c1 = text[1]

	y=1


	if c1 == '/':
		val = 15
	elif c1 == '!':
		val=160
	elif c1 == '?':
		val=161
	elif c1 == '-':
		y+=1
		c2 = text[2]
		k2 = ord(c2)
		if k2 > 31 and k2 < 127 and c2.isalpha():
			val = k2 + 32
	else:
		C1 = c1.upper()
		if C1 == 'A':
			val=123
			if c1.islower():
				val+=32
		elif C1 == 'O':
			val=124
			if c1.islower():
				val+=32
		elif C1 == 'C':
			val=125
			if c1.islower():
				val+=32


	return val, y

def drawChar(draw_surface, screen_x, screen_y, val):
	sheet_x = val % 16
	sheet_y = val // 16
	draw_surface.blit(utils.char_set, (screen_x, screen_y), (sheet_x * utils.char_size, sheet_y * utils.char_size, utils.char_size, utils.char_size))




