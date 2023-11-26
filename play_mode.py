from pico2d import *
import game_framework

import game_world
import result_mode
import upgrade_mode
from Strip import Strip
from stage_info import stage_info

player = None
strip = None
start_time = None
stage = 1
opponent = None
reward = None
strip_length = None

def handle_events():
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
			game_framework.change_mode(upgrade_mode)
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			game_framework.quit()
		else:
			player.handle_event(event)


def init():
	global strip
	global player
	global start_time
	global opponent
	global reward

	start_time = get_time()

	player = upgrade_mode.upgrade.player
	player.reset()
	game_world.add_object(player, 1)

	strip = Strip()
	game_world.add_object(strip, 0)

	match stage:
		case 1:
			stage_info.stage1()
		case 2:
			stage_info.stage2()
		case 3:
			stage_info.stage3()
		case 4:
			stage_info.stage4()
		case 5:
			stage_info.stage5()

	game_world.add_object(opponent)




def finish():
	game_world.clear()
	pass


def update():
	if player.car.sim.engine.rpm > player.car.sim.engine.max_rpm:
		result_mode.race_result = False
		result_mode.fail_statement = 'Engine Blow'
		game_framework.change_mode(result_mode)

	if player.car.sim.engine.temperature >= 100:
		result_mode.race_result = False
		result_mode.fail_statement = 'Engine Overheating'
		game_framework.change_mode(result_mode)

	if player.car.move_distance > 5.0 and get_time() - start_time <= 3.0:
		result_mode.race_result = False
		result_mode.fail_statement = 'False Start'
		game_framework.change_mode(result_mode)

	if opponent.car.move_distance >= strip_length:
		result_mode.race_result = False
		result_mode.fail_statement = 'Opponent Win'
		game_framework.change_mode(result_mode)

	if player.car.move_distance >= strip_length:
		global stage
		result_mode.race_result = True
		player.money += reward
		stage += 1
		game_framework.change_mode(result_mode)

	game_world.update()
	game_world.handle_collisions()


def draw():
	clear_canvas()
	game_world.render()
	update_canvas()


def pause():
	pass


def resume():
	pass
