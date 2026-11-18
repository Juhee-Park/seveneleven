
#재고 입고 코드
#선생님 담당
import hsssssss as h
import timer
import pygame
import random

pygame.init()
jeosong = pygame.mixer.music

jeosong.load("02. 일상 좌와 (日常坐臥).mp3")
jeosong.play(-1)

pokecard =['♥Q', 'SAR 리자몽', '죽은자의 소생', '지우몬', 'AR 거다이맥스 피카츄', '♠A', '바나나5', '블랙매지션', '현대카드', '크리스마스카드']

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
    while True:
        if answer_jeago == "2":
            h.say("흥, 구매를 원하는가? 구매를 원한다면 나와 어둠의 게임을 해야한다. 카드 드로우!!!!!!!!!!!!!!\n")
            jeosong.load("pokemon_battle.mp3")
            jeosong.play(-1)
            print("=================================")
            h.say("카드 드로우를 시작합니다. 1~10까지의 숫자 중 하나를 선택하세요.\n")

            card_this = random.sample(pokecard, 5)
            print("카드 목록:", card_this)
            print("\n카드 목록에서 하나를 선택하세요.(이름 혹은 번호):")
            input_card = input("")

            print("=================================")
            h.say(f"내 카드는... {random.choice(pokecard)}이군.\n결과를 확인하겠다.\n")

            if random.random() < 0.75:
                h.say("나니????????\n 그대가 이겼다..\n")

                h.say("구매 가능한 목록을 띄워주마. 흥.")
                mulgun = random.sample(list(재고목록.keys()), 7)
                canbuy = {item: random.randint(1, 10) for item in mulgun}


                print("=================================")
                h.say("재고 입고가 완료되었습니다.")
            else:
                h.say(f"흥, 고작 {card_this.index(input_card)}같은 카드로 나를 이기겠다고? ")
                h.say("엄마 젖이나 더 먹고와라 애송이!!!!!!!")
                print("=================================")
                h.say("재고 입고가 취소되었습니다. 다음에 다시 시도하세요.")
        elif answer_jeago == "1":
            h.say("흥, 자기소개라. 아주 오래전 이야기지. 예전의 난.. 어렸다. 그리고 2. 그냥 재고나 사기 3. 저번에 제대로 물건이 안왔다고 따지기")
            answer_jeago = input("")
        elif answer_jeago == "3":
            h.say("아 또 뭔데!!!!!!! 뭐가 이상한건데!!!!!!!!")

            print("=================================")
            h.say("지난번에 들어오지 않은 재고의 이름을 입력하세요.:")
            이상했던거 = input("")
            if 이상했던거 == 




