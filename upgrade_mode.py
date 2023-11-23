from pico2d import *
import game_framework

import game_world


def handle_events():
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			game_framework.quit()
		else:
			pass



def init():
	global upgrade_ui
	upgrade_ui = load_image('UpgradeUI.png')
	game_world.add_object(upgrade_ui)


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