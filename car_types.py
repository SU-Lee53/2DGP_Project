
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
		self.front_wheel = load_image('M3.png')
		self.rear_wheel = load_image('M3.png')
