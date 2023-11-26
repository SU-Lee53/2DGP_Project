import random

import game_world
import game_framework
from pico2d import *

from Strip import PIXEL_PER_METER
import car
import play_mode
from behavior_tree import  BehaviorTree, Action, Sequence, Condition, Selector


class Opponent:

	def __init__(self, car_type):
		self.car = car.Car(car_type)
		self.difference = 0.0
		self.car.state_machine.cur_state = car.Idle
		self.upshift_param = self.op_get_upshift_param()
		self.state_show = load_font('ENCR10B.TTF', 16)
		self.build_behavior_tree()

	def update(self):
		self.car.update()
		self.bt.run()
		# diffrence = 상대방의 x좌표 - 플레이어의 x좌표
		self.difference = self.car.move_distance - play_mode.player.car.move_distance

	def draw(self):
		self.car.car_type.draw(self.car.x + (self.difference * PIXEL_PER_METER), self.car.y)

	def op_drive(self):
		self.car.state_machine.cur_state = car.Gas
		return BehaviorTree.RUNNING

	def op_upshift(self):
		if self.car.sim.gear_up():
			self.upshift_param = self.op_get_upshift_param()
			return BehaviorTree.SUCCESS
		else:
			return BehaviorTree.FAIL

	def op_get_upshift_param(self):
		return random.randint(0, 500)

	def op_can_upshift(self):
		if self.car.sim.engine.rpm >= self.car.sim.engine.max_rpm - 1000 + self.upshift_param:
			return BehaviorTree.SUCCESS
		else:
			return BehaviorTree.FAIL

	def op_can_drive(self):
		if get_time() - play_mode.start_time >= 3.0:
			return BehaviorTree.SUCCESS
		else:
			return BehaviorTree.FAIL

	def build_behavior_tree(self):
		c1 = Condition('Can Drive?', self.op_can_drive)
		c2 = Condition('Can Upshift?', self.op_can_upshift)

		a1 = Action('Opponent Drive', self.op_drive)
		a2 = Action('Opponent Upshift', self.op_upshift)

		SEQ_Drive = Sequence('Opponent Drive', c1, a1)
		SEQ_Upshift = Sequence('Opponent Upshift', c2, a2)

		root = SEL_Ai = Selector("Drive or Upshift", SEQ_Upshift, SEQ_Drive)

		self.bt = BehaviorTree(root)


