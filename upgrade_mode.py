from pico2d import *
import game_framework
from upgrade import Upgrader
from play_mode import player
import game_world


def handle_events():
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			game_framework.quit()
		else:
			upgrade.handle_event(event)



def init():
	global upgrade
	upgrade = Upgrader(player)
	game_world.add_object(upgrade)



def finish():
	game_world.clear()
	pass


def update():
	pass


def draw():
	clear_canvas()
	game_world.render()
	update_canvas()


def pause():
	pass


def resume():
	pass