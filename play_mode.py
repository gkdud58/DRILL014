from pico2d import *
import random
import game_world
import game_framework
from boy import Boy
from grass import Grass
from bird import Bird, FLY_SPEED_KMPH_MIN, FLY_SPEED_KMPH_MAX

boy = None
BIRD_COUNT = 10


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

    # 새 10마리: 세로 10단 배치, 시작 x / 방향 / 속도는 무작위
    for i in range(BIRD_COUNT):
        bird = Bird(random.randint(50, 1550), 170 + i * 40,
                    random.uniform(FLY_SPEED_KMPH_MIN, FLY_SPEED_KMPH_MAX))
        bird.dir = random.choice((-1, 1))
        game_world.add_oject(bird)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()









