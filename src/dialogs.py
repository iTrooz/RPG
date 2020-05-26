import utils
import pygame

actual_color = (255, 255, 255)
pixels = None

class Button:
	sheet_x = None
	sheet_y = None

	x = None
	y = None
	w = None

	isPress = False
	isHover = False

	text = None
	text_shadow_color = (190, 100, 20)
	text_color = (255, 255, 255)


	def __init__(self, x, y, text, sheet_x=0, sheet_y=2):
		self.x = x
		self.y = y
		self.text = text
		self.sheet_x = sheet_x
		self.sheet_y = sheet_y
		self.w = getTextLength(self.text)+1

	def update(self):
		m_x, m_y = pygame.mouse.get_pos()
		self.isHover = self.isMouseOver(m_x, m_y)
		self.isPress = pygame.mouse.get_pressed()[0]

	def draw(self):
		if self.isHover:
			shift = 3
			if self.isPress:
				shift = 6
		else:
			shift = 0

		# draw left border
		utils.game_display.blit(utils.ui_set, (self.x, self.y), ((self.sheet_x+shift) * utils.ui_size, self.sheet_y * utils.ui_size, utils.ui_size, utils.ui_size * 2))
		# draw middle
		if self.w>2:
			for i in range(1, self.w-1):
				utils.game_display.blit(utils.ui_set, (self.x + i * utils.ui_size, self.y), ((self.sheet_x+shift+1) * utils.ui_size, self.sheet_y * utils.ui_size, utils.ui_size, utils.ui_size * 2))
		# draw right border
		utils.game_display.blit(utils.ui_set, (self.x + (self.w-1) * utils.ui_size, self.y), ((self.sheet_x+shift+2) * utils.ui_size, self.sheet_y * utils.ui_size, utils.ui_size, utils.ui_size * 2))

		# draw text
		setTextColor(self.text_shadow_color)
		drawText(self.text, self.x + 8, self.y + 6)
		setTextColor(self.text_color)
		drawText(self.text, self.x + 8, self.y + 8)

	def isMouseOver(self, mouse_x, mouse_y):
		return not(mouse_x >= self.x+self.w*utils.ui_size
				or mouse_x <= self.x
				or mouse_y >= self.y+utils.ui_size*2
				or mouse_y <= self.y)







def setTextColor(new_color):
	global actual_color
	if new_color!=actual_color:
		pixels = pygame.PixelArray(utils.char_set)
		pixels.replace(actual_color, new_color)
		pixels.close()
		actual_color = new_color
		del pixels

def getTextLength(text):
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

def drawText(text, x, y):
	screen_x = x
	screen_y = y

	i = 0

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

		drawChar(utils.game_display, screen_x, screen_y, val)
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




