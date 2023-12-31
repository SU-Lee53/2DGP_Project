from pico2d import *
import game_framework
import play_mode
import upgrade_mode

# 패배조건
# 1. 부정출발
# 2. 엔진 블로우(변속 실수로인해 최대 RPM을 넘음)
# 3. 차량 과열

fail_statement = None
race_result = None

def init():
	global image
	global running
	global statement

	if race_result is True:
		image = load_image('./screen/Win_Screen.png')
	else:
		image = load_image('./screen/Lose_Screen.png')

	statement = load_font('./font/impact.TTF', 30)

def finish():
	global image
	del image


def update():
	pass

def draw():
	clear_canvas()
	image.draw(400, 300)
	if race_result is False:
		statement.draw(300, 250, f'reward:{play_mode.reward // 5}', (255,255,255))
		statement.draw(300, 280, fail_statement, (255,255,255))
	else:
		statement.draw(300, 200, f'reward:{play_mode.reward}', (255,255,255))
	update_canvas()


def handle_events():
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
			game_framework.pop_mode()
			game_framework.change_mode(upgrade_mode)
