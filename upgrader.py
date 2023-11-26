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
			if event.key == SDLK_1 and self.player.level['block'] <= 5:
				if self.player.money >= self.price['block']:
					self.player.level['block'] += 1
					self.player.money -= self.price['block']
					self.price['block'] += 500
					self.player.car.sim.engine.max_rpm += 500
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_2 and self.player.level['filter'] <= 5:
				if self.player.money >= self.price['filter']:
					self.player.level['filter'] += 1
					self.player.money -= self.price['filter']
					self.price['filter'] += 500
					self.player.car.car_type.max_temp += 20
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_3 and self.player.level['exhaust'] <= 5:
				if self.player.money >= self.price['exhaust']:
					self.player.level['exhaust'] += 1
					self.player.money -= self.price['exhaust']
					self.price['exhaust'] += 500
					self.player.car.car_type.rpm_raise += 50
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_4:
				if self.player.money >= self.price['turbo']:
					self.player.level['turbo'] = True
					self.player.money -= self.price['turbo']
					self.player.car.sim.engine.max_rpm += 2500
					self.player.car.car_type.rpm_raise += 250
				else:
					game_framework.push_mode(warning_mode)
			elif event.key == SDLK_5:
				if self.player.money >= self.price['nitro']:
					self.player.level['nitro'] = True
					self.player.money -= self.price['nitro']
					self.player.car.nitro = True
				else:
					game_framework.push_mode(warning_mode)


	def draw(self):
		self.ui.draw(self.x, self.y, 800, 600)
		self.font.draw(400, 540, f'{self.player.money}', (255, 255, 255))
		self.font.draw(500, 540, f"STAGE{play_mode.stage} PREPARATION", (255, 255, 255))

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


