from pico2d import *
# 차량 구동계 시뮬레이션




class Mission:
	def __init__(self):
		self.gear = 1  # in game 0 == in real R
		self.ratio = (10, 10, 10, 10, 10, 10)	# 기어비: 바퀴1번 회전당 엔진 회전수, 앞으로 수정 예정
		self.max_gear = 6

	def gear_up(self):
		print('gear up')
		if self.gear >= self.max_gear:
			pass
		self.gear += 1

	def gear_down(self):
		print('gear down')
		if self.gear <= 1:
			pass
		self.gear -= 1

class Engine:
	def __init__(self, r = 8800, t = 365):
		self.rpm = 800			# 일반적인 차량의 기본 아이들링 RPM은 600~800
		self.max_rpm = r
		self.max_torque = t
		self.temperature = 0


class Simulator:
	def __init__(self, car):
		self.mission = Mission()
		self.engine = Engine()

	def gear_up(self):
		print('gear up')
		if self.mission.gear >= self.mission.max_gear:
			return
		self.mission.gear += 1
		print('current:', self.mission.gear)

	def gear_down(self):
		print('gear down')
		if self.mission.gear <= 1:
			return
		self.mission.gear -= 1
		print('current:', self.mission.gear)
	def get_torque(self):
		torque = self.engine.max_torque * self.mission.ratio[self.mission.gear] * (self.engine.max_torque / self.engine.rpm)
		return

