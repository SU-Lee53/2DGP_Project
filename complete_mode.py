from pico2d import *
import game_framework
import game_world

upgrade = None

def handle_events():
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			game_framework.quit()




def init():
	global screen
	screen = load_image('./screen/Complete_Screen.png')

	bgm = load_music('./sound/background.mp3')
	bgm.set_volume(32)
	bgm.play()
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