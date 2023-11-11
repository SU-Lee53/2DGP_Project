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
		car.sim.engine.rpm -= 300 * car.sim.mission.ratio[car.sim.mission.gear] * game_framework.frame_time
		car.sim.engine.rpm = max(car.sim.engine.rpm, 850)
		car.speed -= 10 * game_framework.frame_time
		car.speed = max(car.speed, 0)

	@staticmethod
	def draw(car):
		pass

class Drive:
	@staticmethod
	def enter(car, e):
		car.timer = get_time()
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
		car.sim.engine.rpm += car.rpm_raise * car.sim.mission.ratio[car.sim.mission.gear] * game_framework.frame_time							# 차량 업그레이드시 이 rpm 가중치를 올려주면 좋을듯함
		car.sim.engine.rpm = min(car.sim.engine.rpm, car.sim.engine.max_rpm)
		car.sim.get_torque()
		car.eval_speed()
		if car.speed >= 100.0:
			to100 = get_time()
			print('0-100', to100 - car.timer)

	@staticmethod
	def draw(car):
		pass


class StateMachine:
	def __init__(self, car):
		self.car = car
		self.cur_state = Idle
		self.transitions = {
			Idle: {space_down: Drive, up_down: Idle, down_down: Idle },	# up_down시 변속
			Drive: {space_up: Idle, up_down: Drive, down_down: Drive}
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
		self.timer = None
		self.x, self.y = x, y
		self.image = load_image('M3.png')
		self.front_wheel = load_image('Wheel.png')
		self.rear_wheel = load_image('Wheel.png')
		self.speed = 0.0
		self.acc = 0.0
		self.weight = 1470 * 0.10197	# kg to Newton
		self.diff_ratio = 3.62
		self.aerodynamics = 0.32
		self.frontal_area = 2.07
		self.rpm_raise = 360
		self.state_machine = StateMachine(self)
		self.state_machine.start()

		self.sim = Simulator(self)
		self.accmeter = load_font('ENCR10B.TTF', 16)
		self.speedometer = load_font('ENCR10B.TTF', 16)
		self.rpmmeter = load_font('ENCR10B.TTF', 16)
		self.torquemeter = load_font('ENCR10B.TTF', 16)

		self.SPEED_PER_PPS = lambda e: ((self.speed * 1000 / 60.0) / 60.0) * PIXEL_PER_METER
	def update(self):
			self.state_machine.update()

	def handle_event(self, event):
		self.state_machine.handle_event(('INPUT', event))

	def eval_speed(self):
		if game_framework.frame_time != 0:
			self.acc = (self.sim.engine.torque * self.sim.mission.ratio[self.sim.mission.gear] * self.diff_ratio) / self.weight
			self.speed += self.acc * game_framework.frame_time

	def draw(self):
		self.state_machine.draw()

		self.image.draw(400,200)
		self.front_wheel.draw(556,148, 70, 70)
		self.rear_wheel.draw(270,148, 70, 70)

		self.accmeter.draw(0, 10, f'acc: {self.acc: .2f}', (255,255,0))
		self.speedometer.draw(200, 10, f'speed: {self.speed: .2f}', (255,255,0))
		self.rpmmeter.draw(400, 10, f'rpm: {self.sim.engine.rpm : .2f}', (255,255,0))
		self.torquemeter.draw(600, 10, f'torque: {self.sim.engine.torque: .2f}', (255,255,0))
