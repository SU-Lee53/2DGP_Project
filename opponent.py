import game_world
import game_framework
from pico2d import *

from Strip import PIXEL_PER_METER
import car
import play_mode


class Opponent:

	def __init__(self, car_type):
		self.car = car.Car(car_type)
		self.difference = 0.0


	def update(self):
		self.car.update()
		# diffrence = 상대방의 x좌표 - 플레이어의 x좌표
		self.difference = self.car.move_distance - play_mode.player.car.move_distance

	def draw(self):
		self.car.car_type.draw(self.car.x + (self.difference * PIXEL_PER_METER), self.car.y)

	def op_drive(self):
		self.car.state_machine.cur_state = car.Drive
