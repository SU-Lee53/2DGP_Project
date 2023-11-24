import game_world
import game_framework
from pico2d import *
import play_mode
import result_mode


def one_down(e):
	print('one down')
	return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_1
def two_down(e):
	print('two down')
	return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_2
def three_down(e):
	print('three down')
	return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_3
def four_down(e):
	print('fpur down')
	return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_4
def five_down(e):
	print('five down')
	return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_5

class Upgrader:
	def __init__(self, car):
		self.x, self.y = 400, 300
		self.ui = load_image('UpgradeUI.png')
		self.car = car
		self.font = load_font('ENCR10B.TTF')



	def update(self):
			self.state_machine.update()


	def handle_event(self, event):
		if event.type == SDL_KEYDOWN:
			if event.key == SDLK_1:
				self.car.level['block'] += 1
			elif event.key == SDLK_2:
				self.car.level['filter'] += 1
			elif event.key == SDLK_3:
				self.car.level['exhaust'] += 1
			elif event.key == SDLK_4:
				self.car.level['turbo'] += False
			elif event.key == SDLK_5:
				self.car.level['nitro'] += False





	def draw(self):
		self.ui.draw(self.x, self.y, 800, 600)

