import car_types
import game_framework
from pico2d import *

import play_mode
import warning_mode
from player import Player

# 엔진 블록: 최고속도 증가 -> 최대 RPM을 올려주면
# 엔진 필터: 엔진 내구성 증가 -> 더 높은 열에도 버티고 냉각성능이 올라감
# 배기 : 가속도 증가
# 터보 : 최고속도, 가속도 큰폭으로 증가
# 니트로 : 말그대로 니트로

class Upgrader:
	player = None
	price = None
	def __init__(self):
		self.x, self.y = 400, 300
		self.ui = load_image('./screen/UpgradeUI.png')
		self.font = load_font('impact.TTF')
		if Upgrader.price is None:
			Upgrader.price = {'block': 1000, 'filter': 1000, 'exhaust': 1000, 'turbo': 3000, 'nitro': 5000}
		if Upgrader.player is None:
			Upgrader.player = Player(car_types.M3)

		self.player.money_usage = 0
		self.level_diff = self.player.level.copy()
		self.price_diff = Upgrader.price.copy()



	def update(self):
		pass

	def handle_event(self, event):
		if event.type == SDL_KEYDOWN:
			if event.key == SDLK_1 and self.player.level['block'] <= 5:
				if self.player.money >= self.price['block']:
					self.player.level['block'] += 1
					self.player.money -= Upgrader.price['block']
					self.player.money_usage += Upgrader.price['block']
					Upgrader.price['block'] = 1000 + 500 * (self.player.level['block'] - 1)
					self.player.car.sim.engine.max_rpm += 500
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_2 and self.player.level['filter'] <= 5:
				if self.player.money >= self.price['filter']:
					self.player.level['filter'] += 1
					self.player.money -= Upgrader.price['filter']
					self.player.money_usage += Upgrader.price['filter']
					Upgrader.price['filter'] = 1000 + 500 * (self.player.level['filter'] - 1)
					self.player.car.car_type.max_temp += 20
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_3 and self.player.level['exhaust'] <= 5:
				if self.player.money >= self.price['exhaust']:
					self.player.level['exhaust'] += 1
					self.player.money -= Upgrader.price['exhaust']
					self.player.money_usage += Upgrader.price['exhaust']
					Upgrader.price['exhaust'] = 1000 + 500 * (self.player.level['exhaust'] - 1)
					self.player.car.car_type.rpm_raise += 50
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_4 and self.player.level['turbo'] is False:
				if self.player.money >= self.price['turbo']:
					self.player.level['turbo'] = True
					self.player.money -= Upgrader.price['turbo']
					self.player.money_usage += Upgrader.price['turbo']
					Upgrader.price['turbo'] = 2500 + 500 * (self.player.level['turbo'] - 1)
					self.player.car.sim.engine.max_rpm += 2500
					self.player.car.car_type.rpm_raise += 250
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_5 and self.player.level['nitro'] is False:
				if self.player.money >= self.price['nitro']:
					self.player.level['nitro'] = True
					self.player.money -= Upgrader.price['nitro']
					self.player.money_usage += Upgrader.price['nitro']
					self.player.car.nitro = True
				else:
					game_framework.push_mode(warning_mode)


	def draw(self):
		self.ui.draw(self.x, self.y, 800, 600)
		self.font.draw(400, 540, f'{self.player.money}$', (255, 255, 255))
		self.font.draw(60, 500, f"STAGE{play_mode.stage} PREPARATION", (255, 255, 255))
		self.font.draw(500, 540, f'Press SPACE to start stage{play_mode.stage} ->', (255, 255, 255))

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


