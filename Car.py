import game_world
import game_framework
from pico2d import *
import Simulator


class StateMachine:
	def __init__(self, car):
		pass

	def start(self):
		pass

	def update(self):
		pass

	def handle_event(self, e):
		pass

	def draw(self):
		pass
class Car:
	def __init__(self, x = 50, y = 90):
		self.x, self.y = x, y
		self.body = None
		self.driver = None
		self.interior = None
		self.wheel = None
		self.sim = Simulator()
		self.speed = 0.0
		self.acc = 0.0
		self.weight = 0.0
		self.state_machine = StateMachine(self)
		self.state_machine.start()

	def eval_speed(self):
		pass

	def draw(self):
		pass

