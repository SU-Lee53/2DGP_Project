from pico2d import *
import game_framework

import game_world
import result_mode
from Strip import Strip
from car import Car
import car_types

player = None
strip = None
start_time = None

def handle_events():
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			game_framework.quit()
		else:
			player.handle_event(event)


def init():
	global strip
	global player
	global start_time

	start_time = get_time()

	player = Car(car_types.M3)
	game_world.add_object(player, 1)

	strip = Strip(player)
	game_world.add_object(strip, 0)



def finish():
	game_world.clear()
	pass


def update():
	if player.sim.engine.rpm > player.sim.engine.max_rpm:
		result_mode.race_result = False
		result_mode.fail_statement = 'Engine Blow'
		game_framework.change_mode(result_mode)

	if player.sim.engine.temperature >= 100:
		result_mode.race_result = False
		result_mode.fail_statement = 'Engine Overheating'
		game_framework.change_mode(result_mode)

	if player.move_distance > 5.0 and get_time() - start_time <= 3.0:
		result_mode.race_result = False
		result_mode.fail_statement = 'False Start'
		game_framework.change_mode(result_mode)

	if player.move_distance >= 500.0:
		result_mode.race_result = True
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
