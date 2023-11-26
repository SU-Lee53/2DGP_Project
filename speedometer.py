from pico2d import *

import play_mode


class Speedometer:
	def __init__(self, player):
		self.player = player
		self.speedometer = load_image('./car/speedometer.png')
		self.gearmeter = load_image('./car/gearmeter.png')
		self.red_gage = load_image('./shapes/red_gage.png')
		self.green_gage = load_image('./shapes/green_gage.png')
		self.font = load_font('DS-DIGIT.TTF')
		self.rpm_gage = self.green_gage
		self.temp_gage = self.green_gage
		self.rpm_length = 10
		self.temp_length = 10

	def update(self):
		if self.player.car.sim.engine.rpm >= self.player.car.sim.engine.max_rpm - 1000:
			self.rpm_gage = self.red_gage
		else:
			self.rpm_gage = self.green_gage

		if self.player.car.sim.engine.temperature >= 80:
			self.temp_gage = self.red_gage
		else:
			self.temp_gage = self.green_gage

	# gage max length = 150
	# gage min length = 10
	# 이 사이로 값을 조정한다
		self.rpm_length = (((self.player.car.sim.engine.rpm - 850) / (self.player.car.sim.engine.max_rpm - 850)) * 140) + 10
		self.temp_length = (((self.player.car.sim.engine.temperature - 50) / (100 - 50)) * 140) + 10


	def draw(self):
		self.speedometer.draw(150, 500, 250, 150)
		self.gearmeter.draw(150, 400, 250, 50)
		self.font.draw(180, 550, f'{int(self.player.car.speed)}', (0, 255, 0))
		self.font.draw(180, 400, f'{int(self.player.car.sim.mission.gear)}', (0, 255, 0))
		self.rpm_gage.draw(180, 500, self.rpm_length, 30)
		self.temp_gage.draw(180, 450, self.temp_length, 30)