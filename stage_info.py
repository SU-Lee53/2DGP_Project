import car_types
import play_mode
from opponent import Opponent


class stage_info():
	@staticmethod
	def stage1(opponent, reward):
		play_mode.opponent = Opponent(car_types.EK9)
		play_mode.opponent.car.x, play_mode.opponent.car.y = 150, 150
		play_mode.reward = 2000
	@staticmethod
	def stage2(opponent, reward):
		play_mode.opponent = Opponent(car_types.S4)
		play_mode.opponent.car.x, play_mode.opponent.car.y = 150, 150
		play_mode.reward = 3000

	@staticmethod
	def stage3(opponent, reward):
		play_mode.opponent = Opponent(car_types.RX7)
		play_mode.opponent.car.x, play_mode.opponent.car.y = 150, 150
		play_mode.reward = 4000

	@staticmethod
	def stage4(opponent, reward):
		play_mode.opponent = Opponent(car_types.CLK)
		play_mode.opponent.car.x, play_mode.opponent.car.y = 150, 150
		play_mode.reward = 5000

	@staticmethod
	def stage5(opponent, reward):
		play_mode.opponent = Opponent(car_types.Murcielago)
		play_mode.opponent.car.x, play_mode.opponent.car.y = 150, 150
		play_mode.reward = 5000











