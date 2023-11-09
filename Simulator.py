from pico2d import *
# 차량 구동계 시뮬레이션




class Mission:
	def __init__(self):
		self.gear = 1  # in game 0 == in real R
		self.ratio = (10, 10, 10, 10, 10, 10)
		self.MAX_GEAR = 6

	def gear_up(self):
		if self.gear >= self.MAX_GEAR:
			pass
		self.gear += 1

	def gear_up(self):
		if self.gear <= 0:
			pass
		self.gear -= 1

class Engine:
	def __init__(self):
		self.rpm = 0
		self.torque = 0
		self.temperature = 0


class Simulator:
	def __init__(self):
