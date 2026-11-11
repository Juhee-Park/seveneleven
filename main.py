#편의점 시스템 메인 파일
import hsssssss as h

h.say("안녕하세요 이곳은 세븐 일레븐 이스터 섬 지부...")

h.say("저희는 24시간 운영하는 편의점입니다.")

h.say("자아... 원하시는 기능을 선택해주세요.")

print("1. 물건 구매, 2. 재고 입고, 3. 재고 확인, 4. 환불, 5. 고용")
answer = input("번호를 입력해주세요 : ")

while True:
    if answer == "1":
        h.say("물건 구매를 선택하셨습니다.")
        break
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
        break
    else:
        h.say("잘못된 입력입니다. 프로그램을 종료합니다.")