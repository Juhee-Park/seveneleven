#고용 코드입니다.
import time
def say(stentence): 
    for i in stentence :
        print(i,end='', flush=True)
        time.sleep(0.05)
    print()
