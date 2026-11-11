from pico2d import *
import random
import game_world
import game_framework
from bird import Bird, FLY_SPEED_KMPH_MIN, FLY_SPEED_KMPH_MAX
from grass import Grass

birds = []
BIRD_COUNT = 10


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def init():
    global birds

    birds = []
    for i in range(BIRD_COUNT):
        # 세로로 겹치지 않게 10단으로 나눠 배치, 시작 x 와 속도는 무작위
        bird = Bird(random.randint(50, 1550), 120 + i * 45,
                    random.uniform(FLY_SPEED_KMPH_MIN, FLY_SPEED_KMPH_MAX))
        bird.dir = random.choice((-1, 1))
        birds.append(bird)
        game_world.add_oject(bird)

    grass = Grass()
    game_world.add_oject(grass, 0)


def pause():
    pass


def resume():
    pass


def finish():
    global birds
    game_world.clear()
    birds = []


def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()









