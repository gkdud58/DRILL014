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
