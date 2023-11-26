import car_types
import play_mode
from opponent import Opponent


class stage_info():
	@staticmethod
	def stage1():
		play_mode.opponent = Opponent(car_types.EK9)
		play_mode.opponent.car.x, play_mode.opponent.car.y = 150, 170
		play_mode.reward = 2000
		play_mode.strip_length = 500
	@staticmethod
	def stage2():
		play_mode.opponent = Opponent(car_types.S4)
		play_mode.opponent.car.x, play_mode.opponent.car.y = 150, 170
		play_mode.reward = 3000
		play_mode.strip_length = 1000

	@staticmethod
	def stage3():
		play_mode.opponent = Opponent(car_types.RX7)
		play_mode.opponent.car.x, play_mode.opponent.car.y = 150, 170
		play_mode.reward = 4000
		play_mode.strip_length = 1500

	@staticmethod
	def stage4():
		play_mode.opponent = Opponent(car_types.CLK)
		play_mode.opponent.car.x, play_mode.opponent.car.y = 150, 170
		play_mode.reward = 5000
		play_mode.strip_length = 2000

	@staticmethod
	def stage5():
		play_mode.opponent = Opponent(car_types.Murcielago)
		play_mode.opponent.car.x, play_mode.opponent.car.y = 150, 170
		play_mode.reward = 5000
		play_mode.strip_length = 3000











