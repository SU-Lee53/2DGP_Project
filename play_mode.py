import random
from pico2d import *
import game_framework

import game_world
from Car import Car
from Strip import Strip
import car_types

def handle_events():
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			game_framework.quit()
		else:
			car.handle_event(event)


def init():
	global strip
	global car

	car = Car(car_types.Murcielago)
	game_world.add_object(car, 1)

	strip = Strip(car)
	game_world.add_object(strip, 0)




def finish():
	game_world.clear()
	pass


def update():
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
