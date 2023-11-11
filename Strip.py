import game_world
import game_framework
from pico2d import *


class Strip:
	def __init__(self):
		self.strip = load_image('Strip.png')
		self.crowd = load_image('Crowd.png')
		self.animation = load_image('Run_Animation.png')
		self.crowd_frame = 0
		self.anim_frame = 0
	def update(self):
		self.crowd_frame = (self.crowd_frame + 1) % 1100
		self.anim_frame = (self.anim_frame + 1) % 100
	def draw(self):
		self.strip.clip_draw(10, 0, 800, 250, 400, 150, 800, 300)
		self.crowd.clip_draw(self.crowd_frame, 0, 400, 300, 400, 450, 800, 300)
		self.animation.clip_draw(self.anim_frame, 0, 100, 100, 100, 100, 200, 100)
		self.animation.clip_draw(self.anim_frame + 100, 0, 100, 100, 300, 100, 200, 100)
		self.animation.clip_draw(self.anim_frame + 200, 0, 100, 100, 500, 100, 200, 100)
		self.animation.clip_draw(self.anim_frame + 300, 0, 100, 100, 700, 100, 200, 100)
		# draw_rectangle(0, 100 - 100, 800, 100 + 100)