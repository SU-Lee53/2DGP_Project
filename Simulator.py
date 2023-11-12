from pico2d import *
# 차량 구동계 시뮬레이션
import game_framework



class Mission:
	def __init__(self, ratio, max_gear):
		self.gear = 1  # in game 0 == in real R
		self.ratio = ratio	# 기어비: 바퀴1번 회전당 엔진 회전수, 앞으로 수정 예정
		self.max_gear = max_gear

class Engine:
	def __init__(self, max_rpm, max_torque):
		self.rpm = 800			# 일반적인 차량의 기본 아이들링 RPM은 600~800
		self.torque = 0.0
		self.max_rpm = max_rpm
		self.max_torque = max_torque
		self.temperature = 0.0


class Simulator:
	def __init__(self, car):
		self.car = car
		self.mission = Mission(self.car.car_type.ratio, self.car.car_type.max_gear)
		self.engine = Engine(self.car.car_type.max_rpm, self.car.car_type.max_torque)

	def gear_up(self):
		print('gear up')
		if self.mission.gear >= self.mission.max_gear:
			return
		self.mission.gear += 1
		self.engine.rpm = self.engine.rpm * (self.mission.ratio[self.mission.gear] / self.mission.ratio[self.mission.gear - 1])
		print('current gear:', self.mission.gear)

	def gear_down(self):
		print('gear down')
		if self.mission.gear <= 1:
			return
		self.mission.gear -= 1
		self.engine.rpm = self.engine.rpm * (self.mission.ratio[self.mission.gear] / self.mission.ratio[self.mission.gear + 1])
		print('current gear:', self.mission.gear)

	def get_torque(self):
		self.engine.torque = self.engine.max_torque * (1 - ((self.engine.rpm / self.engine.max_rpm) ** 3))
		self.engine.torque = min(self.engine.torque, self.engine.max_torque)

	def get_aerodynamics(self):
		dragForce = -0.5 * self.car.aerodynamics * self.car.frontal_area * self.car.speed ** 2
		return dragForce

