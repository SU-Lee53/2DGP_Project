import game_framework
from pico2d import load_image

# 필요한 차량 고유 요소들을 차량 종류에 따라 모음.
# self.image = load_image('M3.png')
# self.front_wheel = load_image('Wheel.png')
# self.rear_wheel = load_image('Wheel.png')
# self.weight = 1470 * 0.10197  # kg to Newton
# self.diff_ratio = 3.62
# self.aerodynamics = 0.32
# self.frontal_area = 2.07
# self.rpm_raise = 360
# self.ratio = (0.0, 4.23, 2.53, 1.67, 1.23, 1.0, 0.83)
# self.max_rpm = r
# self.max_torque = t

class M3:
	def __init__(self):
		self.image = load_image('M3.png')
		self.front_wheel = load_image('Wheel.png')
		self.rear_wheel = load_image('Wheel.png')
		self.weight = 1470 * 0.10197	# kg to Newton
		self.diff_ratio = 3.62
		self.aerodynamics = 0.32
		self.frontal_area = 2.07
		self.rpm_raise = 360
		self.ratio = (0.0, 4.23, 2.53, 1.67, 1.23, 1.0, 0.83)
		self.max_rpm = 8000
		self.max_torque = 365
		self.wheel_radius = 0.45 / 2
		self.wheel_rotation = 0.0
		self.front_wheel_x = 93
		self.front_wheel_y = -30
		self.rear_wheel_x = -77
		self.rear_wheel_y = -30
	def draw(self, x, y):
		self.image.draw(x, y, 270, 72)
		self.front_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '', x + self.front_wheel_x, y + self.front_wheel_y, 40, 40)
		self.rear_wheel.clip_composite_draw(0, 0, 86, 86, self.wheel_rotation, '',  x + self.rear_wheel_x, y + self.rear_wheel_y, 40, 40)