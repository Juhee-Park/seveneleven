import main as m
import hsssssss as h
s = True
def shadechoice():
    h.say('누군가가 보인다.')
    h.say('말을 걸까?')
    d = input('(Y/N)')
    if d == 'N':
        m.main2()
        exit()
    else:
        h.say('긍정으로 받아드렸다.')
        h.say('\033[32안녕!\033[0m')
        h.say('\033[32젠장')
        h.say('그런ㄷ')
        h.say('     ')
        h.say('이 외로운 거래자를 도와주지 않겠나?')
        h.say('돈만 조금 주')
        h.say('무료야.')
        h.say('면접 말이지, 그게 번호ㄱ')
        h.say('③\033[0m')
        h.say('\033[34난 널 믿었어. 이게 올바른 거래라 믿었다고. 이\033[0m')
        h.say('\033[33걱정 마 찰리! 모든게 잘\033[0m')
        h.say('\033[34내가 다 해결하겠다고!')
        h.say('으아아아아아아아아아!!!!')
        s = False
        m.main2()
        exit()
if s == True:        
    shadechoice()