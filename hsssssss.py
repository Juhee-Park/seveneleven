#고용 코드입니다.
#현서 담당
import time
import horrorgame as r
def say(stentence): 
    for i in stentence :
        print(i,end='', flush=True)
        time.sleep(0.05)
    print()

def employment():
        say('\033[31m호@오오5 직1원이 되고$ 싶/ 다고["요"]^?>\033[0m')
        say('\033[31m아아4아@ 마침1 ["직원"]을 구하#고 있^^었는데 ㅁ말이죠>\033[0m')
        say('\033[31m그$렇#다면5 면접부*터 보5고 ["담당"]을 선택하시5!\033[0m')
        r.horrors()
        exit()