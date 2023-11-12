import game_world
import game_framework
from pico2d import *
from Simulator import Simulator
import car_types

PIXEL_PER_METER = (800.0 / 20)


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
		car.prev_speed = car.speed
		car.speed -= 10 * game_framework.frame_time
		car.speed = max(car.speed, 0)
		car.eval_wheel_rotation()
		car.move_distance += car.speed * game_framework.frame_time

	@staticmethod
	def draw(car):
		car.car_type.draw(car.x, car.y)

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
		car.sim.engine.rpm += car.car_type.rpm_raise * car.sim.mission.ratio[car.sim.mission.gear] * game_framework.frame_time							# 차량 업그레이드시 이 rpm 가중치를 올려주면 좋을듯함
		car.sim.engine.rpm = min(car.sim.engine.rpm, car.sim.engine.max_rpm)
		car.sim.get_torque()
		car.prev_speed = car.speed
		car.eval_speed()
		car.eval_wheel_rotation()
		car.move_distance += car.speed * game_framework.frame_time

	@staticmethod
	def draw(car):
		car.car_type.draw(car.x, car.y)


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
	def __init__(self, type, x = 150, y = 90,):
		self.x, self.y = x, y
		self.car_type = type()
		self.speed = 0.0
		self.prev_speed = 0.0			# 이전 프레임에서의 속도 -> 바퀴 회전수를 구하기 위함
		self.acc = 0.0
		self.move_distance = 0.0
		self.dist_per_pixel = 0.0
		self.sim = Simulator(self)
		self.state_machine = StateMachine(self)
		self.state_machine.start()

		self.accmeter = load_font('ENCR10B.TTF', 16)
		self.speedometer = load_font('ENCR10B.TTF', 16)
		self.rpmmeter = load_font('ENCR10B.TTF', 16)
		self.torquemeter = load_font('ENCR10B.TTF', 16)

	def update(self):
			self.state_machine.update()

	def handle_event(self, event):
		self.state_machine.handle_event(('INPUT', event))

	def eval_speed(self):
		if game_framework.frame_time != 0:
			self.acc = (self.sim.engine.torque * self.sim.mission.ratio[self.sim.mission.gear] * self.car_type.diff_ratio) / self.car_type.weight
			self.speed += self.acc * game_framework.frame_time

	def eval_wheel_rotation(self):
		if self.prev_speed != 0.0 and self.state_machine.cur_state == Drive:
			self.car_type.wheel_rotation += (self.speed * game_framework.frame_time) / (self.car_type.wheel_radius)
			# self.car_type.wheel_rotation = (self.move_distance * (2 * 3.141592) / self.car_type.wheel_radius**2 * 3.142592) * (self.speed / self.prev_speed)
		elif self.prev_speed != 0.0 and self.state_machine.cur_state == Idle:
			self.car_type.wheel_rotation -= (self.speed * game_framework.frame_time) / (self.car_type.wheel_radius)
		elif self.prev_speed == 0.0:
			self.car_type.wheel_rotation = 0.0
	def get_pps(self):
		self.SPEED_PER_PPS = ((self.speed * 1000 / 60.0) / 60.0) * PIXEL_PER_METER

	def draw(self):
		self.state_machine.draw()


		self.accmeter.draw(0, 10, f'acc: {self.acc: .2f}', (255,255,0))
		self.speedometer.draw(200, 10, f'speed: {self.speed: .2f}', (255,255,0))
		self.speedometer.draw(200, 30, f'distance: {self.move_distance: .2f}', (255,255,0))
		self.speedometer.draw(400, 30, f'wheel: {self.car_type.wheel_rotation: .2f}', (255,255,0))
		self.speedometer.draw(600, 30, f'gear: {self.sim.mission.gear: .2f}', (255,255,0))
		self.rpmmeter.draw(400, 10, f'rpm: {self.sim.engine.rpm : .2f}', (255,255,0))
		self.torquemeter.draw(600, 10, f'torque: {self.sim.engine.torque: .2f}', (255,255,0))
