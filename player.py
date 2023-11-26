import game_world
import game_framework
from pico2d import *
from car import Car

class Player:
	def __init__(self, car_type):
		self.car = Car(car_type)
		self.level = {'block':1, 'filter':1, 'exhaust':1, 'turbo':False, 'nitro':False}
		self.money = 2000
		self.state_show = load_font('ENCR10B.TTF', 16)

	def update(self):
		self.car.update()

	def handle_event(self, event):
		self.car.handle_event(event)

	def draw(self):
		self.car.draw()

		self.state_show.draw(0, 10, f'acc: {self.car.acc: .2f}', (255,255,0))
		self.state_show.draw(200, 10, f'speed: {self.car.speed: .2f}', (255,255,0))
		self.state_show.draw(400, 10, f'rpm: {self.car.sim.engine.rpm : .2f}', (255,255,0))
		self.state_show.draw(600, 10, f'torque: {self.car.sim.engine.torque: .2f}', (255,255,0))
		self.state_show.draw(000, 30, f'temp: {self.car.sim.engine.temperature: .2f}', (255,255,0))
		self.state_show.draw(200, 30, f'distance: {self.car.move_distance: .2f}', (255,255,0))
		self.state_show.draw(400, 30, f'wheel: {self.car.car_type.wheel_rotation: .2f}', (255,255,0))
		self.state_show.draw(600, 30, f'gear: {self.car.sim.mission.gear: .2f}', (255,255,0))

	def reset(self):
		self.car.speed = 0.0
		self.car.prev_speed = 0.0
		self.car.acc = 0.0
		self.car.move_distance = 0.0
		self.car.sim.reset()
