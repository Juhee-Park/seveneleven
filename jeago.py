
#재고 입고 코드
#선생님 담당
import hsssssss as h
import timer
import pygame

pygame.init()
jeosong = pygame.mixer.music
jeosong.load("pokemon_battle.mp3")

firtmeet = True
#더 팔고싶은거 있으면 추가하기
재고목록 = {
    "사과": 0,
    "바나나": 0,
    "오렌지": 0,
    "포도": 0,
    "딸기": 0,
    'moai': 0,
    '마일드 세븐' : 0,
    '보헴 브라운' : 0,
    '커피': 0,
    '고구마(매우맛있음)': 0,
    '호빵': 0,
    '치킨': 0,
    '피자': 0,
    '푸딩' : 0,
    '나폴리맛피아과자': 0


}

def stock_in():
    h.say('\033[31재고5 입고5를 위해 ["시간"]을 체크r합니다.\033[0m')
    h.say("\033[31현재 시간:\033[0m")
if timer.get_hour() < 9 and timer.get_hour() >= 0:
    h.say("아직 재고 입고 시간이 아닙니다. 9~12시 사이에 입고가 가능합니다.")
elif timer.get_hour() >= 9 and timer.get_hour() < 12:
    h.say("재고 입고 시간이 되었습니다. 당신의 부름에 따라 밖에 재고 트럭이 옵니다.")

    print("=================================")

    h.say("\033[33오-이. 나다. 이 트럭의 정당한 주인이자 이 쎄븐 일래븐의 적합한 거래자. 어둠을 가르고 빛을 가르고 그림자도 가르고 강아지도 기르는 자 그 이름은 1.누구세요??? 2. 재고 사기 3. 저번에 제대로 물건이 안왔다고 따지기\033[0m")

    answer_jeago = input("")
    if answer_jeago == "1":
        h.say("\033[33흥, 구매를 원하는가? 구매를 원한다면 나와 어둠의 게임을 해야한다. 카드 드로우!!!!!!!!!!!!!!\033[0m")
        jeosong.play(-1)




