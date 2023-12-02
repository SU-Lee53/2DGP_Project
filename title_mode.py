from pico2d import *
import game_framework
import play_mode
import upgrade_mode
import tutorial_mode


def init():
	global image
	global running
	image = load_image('./screen/Start_Screen.png')


def finish():
	global image
	del image


def update():
	pass


def draw():
	clear_canvas()
	image.draw(400, 300)
	update_canvas()


def handle_events():
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
			game_framework.change_mode(tutorial_mode)
