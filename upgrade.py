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
				print('one down')
				self.car.level['block'] += 1
			elif event.key == SDLK_2:
				print('two down')
				self.car.level['filter'] += 1
			elif event.key == SDLK_3:
				print('three down')
				self.car.level['exhaust'] += 1
			elif event.key == SDLK_4:
				print('four down')
				self.car.level['turbo'] += False
			elif event.key == SDLK_5:
				print('five down')
				self.car.level['nitro'] += False



	def draw(self):
		self.ui.draw(self.x, self.y, 800, 600)
		self.font.draw(400, 540, f'{self.car.money}', (255, 255, 255))
		self.font.draw(60, 120, f"""Lv: {self.car.level['block']}""")
		self.font.draw(215, 120, f"""Lv: {self.car.level['filter']}""")
		self.font.draw(370, 120, f"""Lv: {self.car.level['exhaust']}""")
		self.font.draw(525, 120, f"""{self.car.level['turbo']}""")
		self.font.draw(680, 120, f"""{self.car.level['nitro']}""")


