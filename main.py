#편의점 시스템 메인 파일
#선생님 담당
import hsssssss as h
import easter_island as e
import buy as b
import pygame as pg


#문자열 색바꾸기 가이드
# \033[31m <-  이거를 문자열에 넣으면 글자색이 빨간색으로 바뀌고, 
#31은 빨간색, 32는 초록색, 33은 노란색, 34는 파란색, 35는 보라색, 36은 하늘색, 37은 흰색입니다.
# 끝에 \033[0m <- 를 넣으면 다시 원래 색으로 돌아옵니다.

h.say('\033[31m안녕#하냐 이1곳은 7 일레븐 ["이스터 섬 지부..."]\033[0m')

h.say("\033[32m나2는 24시간 3운영하는 편%의점입니22다.\033[0m")

h.say('\033[33m자아555... 원하시2는 ["기능"]을 선택해주세요.\033[0m')

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