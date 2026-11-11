from pico2d import load_image, get_canvas_width

import game_framework

# 새(Bird) 비행 애니메이션 - 물리 단위 상수 정의
# boy.py 와 동일하게 "미터 -> 픽셀", "km/h -> 초당 픽셀", "초당 프레임" 순서로 환산한다.

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel = 30 cm  (boy.py 와 같은 축척)

# 새 한 마리의 비행 속도 범위 (km/h). 작은 새의 순항 속도 수준.
FLY_SPEED_KMPH_MIN = 30.0
FLY_SPEED_KMPH_MAX = 50.0


def kmph_to_pps(kmph):
    """km/h -> pixel/second. (km/h -> m/min -> m/s -> pixel/s)"""
    mpm = kmph * 1000.0 / 60.0
    mps = mpm / 60.0
    return mps * PIXEL_PER_METER


# ---------------------------------------------------------------
# 스프라이트 시트(bird_animation.png, 918x506) 구조
#   5열 x 3행, 총 14프레임 (1행 5개, 2행 5개, 3행 4개)
#   픽셀 분석 결과 열 간격 182px, 행 간격 약 169px
# ---------------------------------------------------------------
SHEET_COLUMNS = 5
SHEET_HEIGHT = 506
CELL_W = 182
CELL_H = 169
FRAME_COUNT = 14

# ---------------------------------------------------------------
# 날갯짓 속도: "프레임 속도"를 상수가 아니라 비행 속도에서 유도한다.
#   boy.py: RUN_FRAMES_PER_SECOND = 속도(m/s) / 보폭(m) * 보폭당 프레임
#   bird  : FLAP_FPS = 속도(m/s) / 1회 날갯짓당 이동거리(m) * 1회 날갯짓 프레임(14)
# 빨리 나는 새일수록 날개를 더 빨리 친다.
# ---------------------------------------------------------------
METERS_PER_FLAP = 4.0  # 날개 한 번 치는 동안 앞으로 나아가는 거리 (m)
FRAMES_PER_FLAP = FRAME_COUNT


def flap_frames_per_second(speed_kmph):
    speed_mps = speed_kmph * 1000.0 / 3600.0
    return speed_mps / METERS_PER_FLAP * FRAMES_PER_FLAP


DRAW_W = CELL_W // 2  # 화면에는 절반 크기로 그린다
DRAW_H = CELL_H // 2


class Bird:
    image = None  # 10마리가 시트를 공유하도록 클래스 변수로 한 번만 로드

    def __init__(self, x, y, speed_kmph):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.speed_kmph = speed_kmph
        self.frame = 0.0  # 실수 프레임: 그릴 때만 int() 로 내림
        self.dir = 1  # 1: 오른쪽, -1: 왼쪽

    def update(self):
        pass

    def draw(self):
        index = int(self.frame) % FRAME_COUNT
        col = index % SHEET_COLUMNS
        row = index // SHEET_COLUMNS
        left = col * CELL_W
        bottom = max(0, SHEET_HEIGHT - (row + 1) * CELL_H)  # pico2d 는 y 가 아래부터
        flip = '' if self.dir == 1 else 'h'
        self.image.clip_composite_draw(left, bottom, CELL_W, CELL_H,
                                       0, flip, self.x, self.y, DRAW_W, DRAW_H)
