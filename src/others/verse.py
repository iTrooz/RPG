import utils
import pygame

actual_color = (255, 255, 255)

def setColor(new_color):
	global actual_color
	if new_color!=actual_color:
		pixels = pygame.PixelArray(utils.char_set)
		pixels.replace(actual_color, new_color)
		pixels.close()
		actual_color = new_color
		del pixels

def getLength(text):
	i = 0
	length = 0
	while (i<len(text)):
		c = text[i]
		length += 1

		# caractere special
		if c == '/':
			val, y = decodeSpecialChar(text[i:])
			i+=y
		i+=1
	return length

def draw(decoded_array, x, y):
	screen_x = x
	screen_y = y

	for i in decoded_array:
		drawChar(utils.game_display, screen_x, screen_y, i)
		screen_x += utils.char_size

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

def decode(text):
	decoded_array = []
	i = 0

	while (i < len(text)):
		c = text[i]
		k = ord(c)
		val = 95 # not found sprite

		# special character
		if c == '/':
			val, y = decodeSpecialChar(text[i:])
			i += y
		# normal character
		else:
			if k > 31 and k < 127:
				val = k - 32

		decoded_array.append(val)
		i += 1

	return decoded_array

def drawChar(draw_surface, screen_x, screen_y, val):
	sheet_x = val % 16
	sheet_y = val // 16
	draw_surface.blit(utils.char_set, (screen_x, screen_y), (sheet_x * utils.char_size, sheet_y * utils.char_size, utils.char_size, utils.char_size))


