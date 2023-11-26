import car_types
import game_framework
from pico2d import *
import warning_mode
from player import Player


class Upgrader:
	player = None
	def __init__(self):
		self.x, self.y = 400, 300
		self.ui = load_image('./screen/UpgradeUI.png')
		self.font = load_font('impact.TTF')
		self.price = {'block': 1000, 'filter': 1000, 'exhaust': 1500, 'turbo': 3000, 'nitro': 5000}
		if Upgrader.player is None:
			Upgrader.player = Player(car_types.M3)



	def update(self):
		pass

	def handle_event(self, event):
		if event.type == SDL_KEYDOWN:
			if event.key == SDLK_1:
				if self.player.money >= self.price['block']:
					self.player.level['block'] += 1
					self.player.money -= self.price['block']
					self.price['block'] += 500
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_2:
				if self.player.money >= self.price['filter']:
					self.player.level['filter'] += 1
					self.player.money -= self.price['filter']
					self.price['filter'] += 500
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_3:
				if self.player.money >= self.price['exhaust']:
					self.player.level['exhaust'] += 1
					self.player.money -= self.price['exhaust']
					self.price['exhaust'] += 500
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_4:
				if self.player.money >= self.price['turbo']:
					self.player.level['turbo'] = True
					self.player.money -= self.price['turbo']
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_5:
				if self.player.money >= self.price['nitro']:
					self.player.level['nitro'] = True
					self.player.money -= self.price['nitro']
				else:
					game_framework.push_mode(warning_mode)


	def draw(self):
		self.ui.draw(self.x, self.y, 800, 600)
		self.font.draw(400, 540, f'{self.player.money}', (255, 255, 255))
		self.font.draw(500, 540, "STAGE PREPARATION", (255, 255, 255))

		self.font.draw(60, 130, f"""{self.price['block']}$""")
		self.font.draw(215, 130, f"""{self.price['filter']}$""")
		self.font.draw(370, 130, f"""{self.price['exhaust']}$""")
		self.font.draw(525, 120, f"""{self.price['turbo']}$""")
		self.font.draw(680, 130, f"""{self.price['nitro']}$""")

		self.font.draw(60, 100, f"""Lv: {self.player.level['block']}""")
		self.font.draw(215, 100, f"""Lv: {self.player.level['filter']}""")
		self.font.draw(370, 100, f"""Lv: {self.player.level['exhaust']}""")
		self.font.draw(525, 100, f"""{self.player.level['turbo']}""")
		self.font.draw(680, 100, f"""{self.player.level['nitro']}""")


