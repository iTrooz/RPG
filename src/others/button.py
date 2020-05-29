import math

import utils
import pygame
from others import verse

actual_color = (255, 255, 255)
pixels = None

class Button:
	sheet_x = None
	sheet_y = None

	x = None
	y = None
	w = None

	isPress = False
	lastPress = False
	isHover = False
	listener = None

	text = None
	decoded_text = None
	text_shadow_color = (194, 95, 9)
	text_color = (255, 255, 255)


	def __init__(self, x, y, text, w=None, listener=None, sheet_x=0, sheet_y=2):
		self.x = x
		self.y = y
		self.text = text
		self.decoded_text = verse.decode(text)
		self.sheet_x = sheet_x
		self.sheet_y = sheet_y
		self.listener = listener
		if w is None:
			self.w = len(self.decoded_text)
		else:
			self.w = w

	def updateWithMouse(self):
		m_x, m_y = pygame.mouse.get_pos()
		self.isHover = self.isMouseOver(m_x, m_y)
		self.lastPress = self.isPress
		self.isPress = pygame.mouse.get_pressed()[0]

		if (self.lastPress and not self.isPress and self.isHover):
			if (self.listener is not None):
				self.listener()

	def draw(self):
		# shift the sprite to change appearance
		if self.isHover:
			shift = 3
			if self.isPress:
				shift = 6
		else:
			shift = 0

		# draw left border
		utils.drawSprite(utils.ui_set, utils.ui_size, self.x, self.y, self.sheet_x + shift, self.sheet_y, 1, 2)
		# draw middle
		for i in range(1, self.w-1):
			utils.drawSprite(utils.ui_set, utils.ui_size, self.x + i * utils.ui_size, self.y, self.sheet_x + shift + 1, self.sheet_y, 1, 2)
		# draw right border
		utils.drawSprite(utils.ui_set, utils.ui_size, self.x + (self.w - 1) * utils.ui_size, self.y, self.sheet_x + shift + 2, self.sheet_y, 1, 2)

		# draw text
		center_draw_point = math.floor(self.x + self.w*utils.ui_size/2 - len(self.decoded_text)/2*utils.ui_size)
		verse.setColor(self.text_shadow_color)
		verse.draw(self.decoded_text, center_draw_point, self.y + 6)
		verse.setColor(self.text_color)
		verse.draw(self.decoded_text, center_draw_point, self.y + 6 + utils.scale_factor)

	def isMouseOver(self, mouse_x, mouse_y):
		return not(mouse_x >= self.x + self.w * utils.ui_size
				or mouse_x <= self.x
				or mouse_y >= self.y + utils.ui_size * 2
				or mouse_y <= self.y)








