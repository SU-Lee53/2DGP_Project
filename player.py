import game_world
import game_framework
from pico2d import *
from car import Car

class Player:
	def __init__(self, car_type):
		self.car = Car(car_type)
		self.level = {'block':1, 'filter':1, 'exhaust':1, 'turbo':False, 'nitro':False}
		self.money = 2000

	def update(self):
		self.car.update()

	def handle_event(self, event):
		self.car.handle_event(event)

	def draw(self):
		self.car.draw()




