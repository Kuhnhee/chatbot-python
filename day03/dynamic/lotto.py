# lotto api를 통해 최신 당첨번호를 가져온다.

import requests
import random


url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
res = requests.get(url)    #json file을 dict 구조로 바꿔줘야함.

json_lotto = res.text      #json file이 string으로 들어온 것. (이렇게 하면 안돼)
dict_lotto = res.json()    #json file이 dict 구조로 들어온 것.

# winner에 1등 당첨 번호를 넣기
winner = [dict_lotto["drwtNo" + str(i)] for i in range(1,7)]

place = 0
trial = 0
third_count = 0
fourth_count = 0
fifth_count = 0
while(True):
    same_cnt = 0
    trial += 1
    my_lotto = sorted(random.sample(range(1,46), 6))     # 로또 랜덤 추천

    # for i in winner:
    #     for j in my_lotto:
    #         if i == j:
    #             same_cnt += 1
    #             break
    same_cnt = len(set(winner) & set(my_lotto)) # 교집합
    
    if same_cnt==6:
        print("1st place, this was {0}th trial".format(trial))
        print("You've got {0} times of 3rd places, {1} times of 4th places, {2} times of 5th places".format(third_count,fourth_count,fifth_count))
        print("\nYour number is... {0}".format(my_lotto))
        print("Correct num is... {0}".format(winner))
        place = 1
        break;
    elif same_cnt==5:
        third_count += 1
    elif same_cnt==4:
        fourth_count += 1
    elif same_cnt==3:
        fifth_count += 1
    else:
        continue