#현재 시간을 계산해주는 코드
import time

start_time = time.monotonic()

#get_hour()를 실행하면 09시 처럼 현재 시간이 나옴. 시간은 3분마다 1시간씩 바뀜
def get_hour() -> str:
    elapsed_hours = int((time.monotonic() - start_time) // 180)
    hour = (9 + elapsed_hours) % 24
    return f"{hour:02d}시"

print(get_hour())  # 실행 직후: 09시