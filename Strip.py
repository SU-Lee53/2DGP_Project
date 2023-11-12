import game_world
import game_framework
from pico2d import *

PIXEL_PER_METER = (800.0 / 20)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
CROWD_MOVE_PER_ACTION = 1100
ANIM_MOVE_PER_ACTION = 100


class Strip:
	def __init__(self, car):
		self.strip = load_image('Strip.png')
		self.crowd = load_image('Crowd.png')
		self.animation = load_image('Run_Animation.png')
		self.crowd_frame = 0
		self.anim_frame = 0
		self.player = car				# 프레임 움직임의 기준이 되는 속도를 플레이어의 자동차가 갖고있음.
		self.start_line = load_image('Start_Line.png')
		self.start_sign = None
		self.start_time = get_time()

	def update(self):
		self.crowd_frame = ((self.player.move_distance * PIXEL_PER_METER) + 0.0 * game_framework.frame_time) % 1100
		self.anim_frame = ((self.player.move_distance * PIXEL_PER_METER) + 0.0 * game_framework.frame_time) % 100
		if get_time() - self.start_time <= 1.0:
			self.start_sign = load_image('sign1.png')
		elif get_time() - self.start_time <= 2.0:
			self.start_sign = load_image('sign2.png')
		elif get_time() - self.start_time <= 3.0:
			self.start_sign = load_image('sign3.png')
		elif get_time() - self.start_time <= 4.0:
			self.start_sign = load_image('sign4.png')

	def draw(self):
		self.strip.clip_draw(10, 0, 800, 250, 400, 150, 800, 300)
		self.crowd.clip_draw(int(self.crowd_frame), 0, 400, 300, 400, 450, 800, 300)
		self.animation.clip_draw(int(self.anim_frame), 0, 100, 100, 100, 100, 200, 100)
		self.animation.clip_draw(int(self.anim_frame + 100), 0, 100, 100, 300, 100, 200, 100)
		self.animation.clip_draw(int(self.anim_frame), 0, 100, 100, 500, 100, 200, 100)
		self.animation.clip_draw(int(self.anim_frame + 300), 0, 100, 100, 700, 100, 200, 100)
		self.start_line.draw(400 - (self.player.move_distance * PIXEL_PER_METER), 128, 212, 258)
		self.start_sign.draw(365 - (self.player.move_distance * PIXEL_PER_METER), 302, 80, 240)