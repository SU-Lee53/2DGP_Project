from pico2d import *
import game_framework
import game_world
import upgrade_mode

upgrade = None

def handle_events():
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			game_framework.quit()
		elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
			game_framework.change_mode(upgrade_mode)




def init():
	global screen
	screen = load_image('./screen/Tutorial_Screen.png')

def finish():
	pass


def update():
	pass


def draw():
	clear_canvas()
	screen.draw(400,300,800,600)
	update_canvas()


def pause():
	pass


def resume():
	pass