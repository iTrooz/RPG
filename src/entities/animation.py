class Animation:
	sheet_x = None
	sheet_y = None
	sprites_nb = None
	is_looping = None
	speed = None

	def __init__(self, sheet_x, sheet_y, speed, sprites_nb = 0, is_looping = True):
		self.sheet_x = sheet_x
		self.sheet_y = sheet_y
		self.speed = speed
		self.sprites_nb = sprites_nb
		self.is_looping = is_looping

class AnimationManager:
	anim_set = None
	anim_name = None # current animation
	anim_time = None # current advancement of the animation
	current_frame = None # index of the current frame

	def __init__(self, anim_set, anim_name):
		self.anim_set = anim_set
		self.anim_name = anim_name
		self.anim_time = 0
		self.current_frame = 0

	def ChangeAnim(self, new_anim_name):
		if self.anim_name != new_anim_name:
			self.anim_name = new_anim_name
			self.anim_time = 0

	def updateAnim(self):
		animation = self.anim_set[self.anim_name]
		self.anim_time += 1

		# update frame
		if self.anim_time % animation.speed == 0:
			self.current_frame += 1
			if self.current_frame > animation.sprites_nb:
				self.current_frame = 0

	def getSpritePos(self, direction):
		return self.anim_set[self.anim_name].sheet_x+self.current_frame, self.anim_set[self.anim_name].sheet_y+direction.id
