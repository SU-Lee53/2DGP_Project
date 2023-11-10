import game_world
import game_framework
from pico2d import *
from Simulator import Simulator

# 필요한 차량의 상태 -> 정지 or 달림
def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP
def down_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN
def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE
def space_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE

PIXEL_PER_METER = (800.0 / 5)


class Idle:
	@staticmethod
	def enter(car, e):
		print('Idle')
		pass

	@staticmethod
	def exit(car, e):
		if up_down(e):
			car.sim.gear_up()
		elif down_down(e):
			car.sim.gear_down()

	@staticmethod
	def do(car):
		pass

	@staticmethod
	def draw(car, e):
		pass

class Drive:
	@staticmethod
	def enter(car, e):
		print('drive')
		pass

	@staticmethod
	def exit(car, e):
		if up_down(e):
			car.sim.gear_up()
		elif down_down(e):
			car.sim.gear_down()

	@staticmethod
	def do(car):
		pass

	@staticmethod
	def draw(car, e):
		pass


class StateMachine:
	def __init__(self, car):
		self.car = car
		self.cur_state = Idle
		self.transitions = {
			Idle: {space_down: Drive, up_down: Idle, down_down: Idle },	# up_down시 변속
			Drive: {space_up: Idle, up_down: Drive, down_down: Idle}
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
	def __init__(self, x = 50, y = 90):
		self.x, self.y = x, y
		self.body = None
		self.driver = None
		self.interior = None
		self.wheel = None
		self.wheelRadius = 0.0
		self.sim = Simulator(self)
		self.speed = 0.0
		self.acc = 0.0
		self.weight = 0.0
		self.state_machine = StateMachine(self)
		self.state_machine.start()

		self.speedometer = load_font('ENCR10B.TTF', 16)
		self.rpmmeter = load_font('ENCR10B.TTF', 16)

		self.SPEED_PER_PPS = lambda e: ((self.speed * 1000 / 60.0) / 60.0) * PIXEL_PER_METER
	def update(self):
			self.state_machine.update()

	def handle_event(self, event):
		self.state_machine.handle_event(('INPUT', event))

	def eval_speed(self):
		pass

	def draw(self):
		pass

