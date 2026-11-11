#편의점 시스템 메인 파일
#선생님 담당
import hsssssss as h
import easter_island as e
import buy as b

h.say('안녕#하냐 이1곳은 7 일레븐 ["이스터 섬 지부..."]')

h.say("나2는 24시간 3운영하는 편%의점입니22다.")

h.say('자아555... 원하시2는 ["기능"]을 선택해주세요.')

print("1. 물건 구매, 2. 재고 입고, 3. 재고 확인, 4. 환불, 5. 고용")
answer = input("번호를 입력해주세요 : ")

while True:
    if answer == "1":
        h.say("물건 구매를 선택하셨습니다.")
        b.buy()
        exit()
    elif answer == "2":
        h.say("재고 입고를 선택하셨습니다.")
        break
    elif answer == "3":
        h.say("재고 확인을 선택하셨습니다.")
        break
    elif answer == "4":
        h.say("환불을 선택하셨습니다.")
        break
    elif answer == "5":  
        h.say("고용을 선택하셨습니다.")
        h.employment()
        exit()
    elif answer == "moai":
        e.moai()
        exit()
    else:
        h.say("잘못된 입력입니다. 프로그램을 종료합니다.")