from pico2d import *

import car
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
		self.temperature = 50


class Simulator:
	def __init__(self, car):
		self.car = car
		self.mission = Mission(self.car.car_type.ratio, self.car.car_type.max_gear)
		self.engine = Engine(self.car.car_type.max_rpm, self.car.car_type.max_torque)
		self.nitro = False
		self.turbo = False

	def gear_up(self):
		print('gear up')
		if self.mission.gear >= self.mission.max_gear:
			return False
		self.mission.gear += 1
		self.engine.rpm = self.engine.rpm * (self.mission.ratio[self.mission.gear] / self.mission.ratio[self.mission.gear - 1])
		print('current gear:', self.mission.gear)
		return True

	def gear_down(self):
		print('gear down')
		if self.mission.gear <= 1:
			return False
		self.mission.gear -= 1
		self.engine.rpm = self.engine.rpm * (self.mission.ratio[self.mission.gear] / self.mission.ratio[self.mission.gear + 1])
		print('current gear:', self.mission.gear)
		return True

	def get_torque(self):
		self.engine.torque = self.engine.max_torque * (1 - ((self.engine.rpm / self.engine.max_rpm) ** 3))
		self.engine.torque = min(self.engine.torque, self.engine.max_torque)

	def get_aerodynamics(self):
		dragForce = -0.5 * self.car.aerodynamics * self.car.frontal_area * self.car.speed ** 2
		return dragForce


	def eval_speed(self):
		if game_framework.frame_time != 0:
			self.car.acc = (self.engine.torque * self.mission.ratio[self.mission.gear] * self.car.car_type.diff_ratio) / self.car.car_type.weight
			self.car.speed += self.car.acc * game_framework.frame_time

	def eval_wheel_rotation(self):
		if self.car.prev_speed != 0.0 and self.car.state_machine.cur_state == car.Gas:
			self.car.car_type.wheel_rotation += (self.car.speed * game_framework.frame_time) / (self.car.car_type.wheel_radius)
			# self.car_type.wheel_rotation = (self.move_distance * (2 * 3.141592) / self.car_type.wheel_radius**2 * 3.142592) * (self.speed / self.prev_speed)
		elif self.car.prev_speed != 0.0 and self.car.state_machine.cur_state == car.Idle:
			self.car.car_type.wheel_rotation -= (self.car.speed * game_framework.frame_time) / (self.car.car_type.wheel_radius)
		elif self.car.prev_speed == 0.0:
			self.car.car_type.wheel_rotation = 0.0


	def reset(self):
		self.engine.rpm = 800
		self.engine.torque = 0.0
		self.engine.temperature = 50
		self.mission.gear = 1
