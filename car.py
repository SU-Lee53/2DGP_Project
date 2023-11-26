import game_world
import game_framework
from pico2d import *

import result_mode
from simulator import Simulator
import car_types

from car_types import *
# 필요한 차량의 상태 -> 정지 or 달림
def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP
def down_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN
def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE
def space_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE
def shift_down(e):
	return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LSHIFT
def shift_up(e):
	return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LSHIFT
def ctrl_down(e):
	return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LCTRL
def ctrl_up(e):
	return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LCTRL


class Idle:
	@staticmethod
	def enter(car, e):
		print('Idle')
		car.sim.engine.torque = 0.0
		car.acc = 0.0
		pass

	@staticmethod
	def exit(car, e):
		if up_down(e):
			car.sim.gear_up()
		elif down_down(e):
			car.sim.gear_down()

	@staticmethod
	def do(car):
		car.sim.engine.rpm -= 1000 * car.sim.mission.ratio[car.sim.mission.gear] * game_framework.frame_time
		car.sim.engine.rpm = max(car.sim.engine.rpm, 850)
		if car.sim.engine.rpm >= car.sim.engine.max_rpm - 1000:
			car.sim.engine.temperature += 10 * game_framework.frame_time
		else:
			car.sim.engine.temperature -= 10 * game_framework.frame_time
			car.sim.engine.temperature = max(car.sim.engine.temperature, 50)
		car.prev_speed = car.speed
		car.speed -= 10 * game_framework.frame_time
		car.speed = max(car.speed, 0)
		car.sim.eval_wheel_rotation()
		car.move_distance += car.speed * game_framework.frame_time

	@staticmethod
	def draw(car):
		car.car_type.draw(car.x, car.y, False)

class Gas:
	@staticmethod
	def enter(car, e):
		print('drive')

	@staticmethod
	def exit(car, e):
		if up_down(e):
			car.sim.gear_up()
		elif down_down(e):
			car.sim.gear_down()

	@staticmethod
	def do(car):
		car.sim.engine.rpm += car.car_type.rpm_raise * car.sim.mission.ratio[car.sim.mission.gear] * game_framework.frame_time							# 차량 업그레이드시 이 rpm 가중치를 올려주면 좋을듯함
		car.sim.engine.rpm = min(car.sim.engine.rpm, car.sim.engine.max_rpm)
		if car.sim.engine.rpm >= car.sim.engine.max_rpm - 1000:
			car.sim.engine.temperature += 10 * game_framework.frame_time
		else:
			car.sim.engine.temperature -= 10 * game_framework.frame_time
			car.sim.engine.temperature = max(car.sim.engine.temperature, 50)
		car.sim.get_torque()
		car.prev_speed = car.speed
		car.sim.eval_speed()
		car.sim.eval_wheel_rotation()
		car.move_distance += car.speed * game_framework.frame_time

	@staticmethod
	def draw(car):
		car.car_type.draw(car.x, car.y, False)

class Nitro:
	@staticmethod
	def enter(car, e):
		if car.nitro == False or car.nitro_gage <= 0:
			car.state_machine.cur_state = Gas
		print('Nitro')

	@staticmethod
	def exit(car, e):
		if up_down(e):
			car.sim.gear_up()
		elif down_down(e):
			car.sim.gear_down()

	@staticmethod
	def do(car):
		car.sim.engine.rpm += car.car_type.rpm_raise * 1.5 * car.sim.mission.ratio[car.sim.mission.gear] * game_framework.frame_time							# 차량 업그레이드시 이 rpm 가중치를 올려주면 좋을듯함
		car.sim.engine.rpm = min(car.sim.engine.rpm, car.sim.engine.max_rpm)
		if car.sim.engine.rpm >= car.sim.engine.max_rpm - 1000:
			car.sim.engine.temperature += 20 * game_framework.frame_time
		else:
			car.sim.engine.temperature -= 10 * game_framework.frame_time
			car.sim.engine.temperature = max(car.sim.engine.temperature, 50)
		car.sim.get_torque()
		car.prev_speed = car.speed
		car.sim.eval_speed()
		car.speed += 0.5
		car.sim.eval_wheel_rotation()
		car.move_distance += car.speed * game_framework.frame_time
		car.nitro_gage -= 80 * game_framework.frame_time
		if car.nitro_gage <= 0:
			car.state_machine.cur_state = Gas

	@staticmethod
	def draw(car):
		car.car_type.draw(car.x, car.y, True)

class Brake:
	@staticmethod
	def enter(car, e):
		print('brake')

	@staticmethod
	def exit(car, e):
		if up_down(e):
			car.sim.gear_up()
		elif down_down(e):
			car.sim.gear_down()

	@staticmethod
	def do(car):
		car.sim.engine.rpm -= 3000 * car.sim.mission.ratio[car.sim.mission.gear] * game_framework.frame_time
		car.sim.engine.rpm = max(car.sim.engine.rpm, 850)
		if car.sim.engine.rpm >= car.sim.engine.max_rpm - 1000:
			car.sim.engine.temperature += 10 * game_framework.frame_time
		else:
			car.sim.engine.temperature -= 10 * game_framework.frame_time
			car.sim.engine.temperature = max(car.sim.engine.temperature, 50)
		car.prev_speed = car.speed
		car.speed -= 50 * game_framework.frame_time
		car.speed = max(car.speed, 0)
		car.sim.eval_wheel_rotation()
		car.move_distance += car.speed * game_framework.frame_time

	@staticmethod
	def draw(car):
		car.car_type.draw(car.x, car.y, False)


class StateMachine:
	def __init__(self, car):
		self.car = car
		self.cur_state = Idle
		self.transitions = {
			Idle: {space_down: Gas, shift_down: Brake, up_down: Idle, down_down: Idle},	# up_down시 변속
			Gas: {space_up: Idle, shift_down: Brake, ctrl_down: Nitro, up_down: Gas, down_down: Gas},
			Brake: {shift_up: Idle, up_down: Brake, down_down: Brake},
			Nitro: {ctrl_up: Gas, shift_up: Idle, up_down: Nitro, down_down: Nitro}
		}

	def start(self):
		self.cur_state.enter(self.car, ('NONE', 0))

	def update(self):
		self.cur_state.do(self.car)

	def handle_event(self, e):
		for check_event, next_state in self.transitions[self.cur_state].items():
			if check_event(e):
				self.cur_state.exit(self.car, e)
				self.cur_state = next_state
				self.cur_state.enter(self.car, e)
				return True

		return False

	def draw(self):
		self.cur_state.draw(self.car)

class Car:
	def __init__(self, type, x = 150, y = 90):
		self.x, self.y = x, y
		self.car_type = type()
		self.speed = 0.0
		self.prev_speed = 0.0			# 이전 프레임에서의 속도 -> 바퀴 회전수를 구하기 위함
		self.acc = 0.0
		self.move_distance = 0.0
		self.nitro = False
		self.nitro_gage = 100

		self.sim = Simulator(self)
		self.state_machine = StateMachine(self)
		self.state_machine.start()


	def update(self):
			self.state_machine.update()


	def handle_event(self, event):
		self.state_machine.handle_event(('INPUT', event))


	def draw(self):
		self.state_machine.draw()

