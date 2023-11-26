import game_framework
from pico2d import load_image

# 필요한 차량 고유 요소들을 차량 종류에 따라 모음.
# self.image = load_image('M3.png')
# self.front_wheel = load_image('Wheel.png')
# self.rear_wheel = load_image('Wheel.png')
# self.weight = 1470 * 0.10197  # kg to N
# self.diff_ratio = 3.62
# self.aerodynamics = 0.32
# self.frontal_area = 2.07
# self.rpm_raise = 360
# self.ratio = (0.0, 4.23, 2.53, 1.67, 1.23, 1.0, 0.83)
# self.max_rpm = r
# self.max_torque = t

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class M3:
	def __init__(self):
		self.image = load_image('./car/M3.png')
		self.front_wheel = load_image('./car/Wheel.png')
		self.rear_wheel = load_image('./car/Wheel.png')
		self.nitro = load_image('./car/nitro.png')
		self.nitro_frame = 0
		self.weight = 1470 * 0.10197	# kg to Newton
		self.diff_ratio = 3.62
		self.aerodynamics = 0.32
		self.frontal_area = 2.07
		self.rpm_raise = 800
		self.ratio = (0.0, 4.23, 2.53, 1.67, 1.23, 1.0, 0.83)
		self.max_gear = 6
		self.max_rpm = 8000
		self.max_torque = 365
		self.max_temp = 100
		self.wheel_radius = 0.45 / 2

		self.wheel_rotation = 0.0
		self.front_wheel_x = 91
		self.front_wheel_y = -27
		self.rear_wheel_x = -75
		self.rear_wheel_y = -27

	def draw(self, x, y, boost):
		self.image.draw(x, y, 270, 72)
		self.front_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '', x + self.front_wheel_x, y + self.front_wheel_y, 40, 40)
		self.rear_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '',  x + self.rear_wheel_x, y + self.rear_wheel_y, 40, 40)
		if boost is True:
			self.nitro.clip_draw(int(self.nitro_frame) * 100, 0, 100, 100, 1, 75, 70, 70)
			self.nitro_frame = (self.nitro_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

class EK9:
	def __init__(self):
		self.image = load_image('./car/EK9.png')
		self.front_wheel = load_image('./car/Wheel.png')
		self.rear_wheel = load_image('./car/Wheel.png')
		self.nitro = load_image('./car/nitro.png')
		self.weight = 1073 * 0.10197	# kg to Newton
		self.diff_ratio = 4.40
		self.aerodynamics = 0.32
		self.frontal_area = 2.09
		self.rpm_raise = 1000
		self.ratio = (0.0, 3.23, 2.105, 1.458, 1.107, 1.0, 0.83)
		self.max_gear = 4
		self.max_rpm = 9000
		self.max_torque = 163
		self.max_temp = 100
		self.wheel_radius = 0.38 / 2

		self.wheel_rotation = 0.0
		self.front_wheel_x = 85
		self.front_wheel_y = -30
		self.rear_wheel_x = -93
		self.rear_wheel_y = -30

	def draw(self, x, y):
		self.image.draw(x, y, 270, 72)
		self.front_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '', x + self.front_wheel_x, y + self.front_wheel_y, 40, 40)
		self.rear_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '',  x + self.rear_wheel_x, y + self.rear_wheel_y, 40, 40)


class S4:
	def __init__(self):
		self.image = load_image('./car/S4.png')
		self.front_wheel = load_image('./car/Wheel.png')
		self.rear_wheel = load_image('./car/Wheel.png')
		self.nitro = load_image('./car/nitro.png')
		self.nitro_frame = 0
		self.weight = 1720 * 0.10197  # kg to Newton
		self.diff_ratio = 3.54
		self.aerodynamics = 0.28
		self.frontal_area = 2.49
		self.rpm_raise = 800
		self.ratio = (0.0, 3.67, 2.05, 1.46, 1.13, 0.87, 0.69)
		self.max_gear = 6
		self.max_rpm = 7000
		self.max_torque = 410
		self.max_temp = 100
		self.wheel_radius = 0.45 / 2

		self.wheel_rotation = 0.0
		self.front_wheel_x = 87
		self.front_wheel_y = -30
		self.rear_wheel_x = -78
		self.rear_wheel_y = -30

	def draw(self, x, y):
		self.image.draw(x, y, 270, 72)
		self.front_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '', x + self.front_wheel_x,
																				 y + self.front_wheel_y, 40, 40)
		self.rear_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '', x + self.rear_wheel_x,
																				y + self.rear_wheel_y, 40, 40)

class RX7:
	def __init__(self):
		self.image = load_image('./car/RX7.png')
		self.front_wheel = load_image('./car/Wheel.png')
		self.rear_wheel = load_image('./car/Wheel.png')
		self.nitro = load_image('./car/nitro.png')
		self.nitro_frame = 0
		self.weight = 1310 * 0.10197  # kg to Newton
		self.diff_ratio = 4.1
		self.aerodynamics = 0.28
		self.frontal_area = 2.49
		self.rpm_raise = 800
		self.ratio = (0.0, 3.48, 2.01, 1.39, 1.00, 0.72, 0.69)
		self.max_gear = 5
		self.max_rpm = 6500
		self.max_torque = 255
		self.max_temp = 100
		self.wheel_radius = 0.40 / 2

		self.wheel_rotation = 0.0
		self.front_wheel_x = 87
		self.front_wheel_y = -25
		self.rear_wheel_x = -77
		self.rear_wheel_y = -25

	def draw(self, x, y):
		self.image.draw(x, y, 270, 72)
		self.front_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '', x + self.front_wheel_x,
																				 y + self.front_wheel_y, 40, 40)
		self.rear_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '', x + self.rear_wheel_x,
																				y + self.rear_wheel_y, 40, 40)

class CLK:
	def __init__(self):
		self.image = load_image('./car/CLK.png')
		self.front_wheel = load_image('./car/Wheel.png')
		self.rear_wheel = load_image('./car/Wheel.png')
		self.nitro = load_image('./car/nitro.png')
		self.nitro_frame = 0
		self.weight = 1310 * 0.10197  # kg to Newton
		self.diff_ratio = 2.65
		self.aerodynamics = 0.28
		self.frontal_area = 2.44
		self.rpm_raise = 700
		self.ratio = (0.0, 4.38, 2.86, 1.92, 1.35, 1.00, 0.87, 0.73)
		self.max_gear = 7
		self.max_rpm = 7500
		self.max_torque = 630
		self.max_temp = 100
		self.wheel_radius = 0.48 / 2

		self.wheel_rotation = 0.0
		self.front_wheel_x = 82
		self.front_wheel_y = -25
		self.rear_wheel_x = -75
		self.rear_wheel_y = -25

	def draw(self, x, y):
		self.image.draw(x, y, 270, 72)
		self.front_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '', x + self.front_wheel_x,
																				 y + self.front_wheel_y, 40, 40)
		self.rear_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '', x + self.rear_wheel_x,
																				y + self.rear_wheel_y, 40, 40)


class Murcielago:
	def __init__(self):
		self.image = load_image('./car/Murcielago.png')
		self.front_wheel = load_image('./car/Wheel.png')
		self.rear_wheel = load_image('./car/Wheel.png')
		self.nitro = load_image('./car/nitro.png')
		self.nitro_frame = 0
		self.weight = 1841 * 0.10197  # kg to Newton
		self.diff_ratio = 2.53
		self.aerodynamics = 0.33
		self.frontal_area = 2.53
		self.rpm_raise = 600
		self.ratio = (0.0, 3.09, 2.10, 1.56, 1.24, 1.06, 0.93)
		self.max_gear = 6
		self.max_rpm = 8000
		self.max_torque = 660
		self.max_temp = 100
		self.wheel_radius = 0.40 / 2

		self.wheel_rotation = 0.0
		self.front_wheel_x = 82
		self.front_wheel_y = -20
		self.rear_wheel_x = -90
		self.rear_wheel_y = -20

	def draw(self, x, y):
		self.image.draw(x, y, 270, 72)
		self.front_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '', x + self.front_wheel_x,
																				 y + self.front_wheel_y, 40, 40)
		self.rear_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '', x + self.rear_wheel_x,
																				y + self.rear_wheel_y, 40, 40)









