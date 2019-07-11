'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
vals = list(score.values())
avg = sum(vals)/len(vals)
print("average point is: {0}".format(avg))


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 10
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
a_val = list(scores['a'].values())
b_val = list(scores['b'].values())
a_avg = sum(a_val)/len(a_val)
b_avg = sum(b_val)/len(b_val)
print("average of class a is: {}".format(a_avg))
print("average of class b is: {}".format(b_avg))

math_avg = (scores['a']['수학'] + scores['b']['수학']) / len(scores.keys())
lang_avg = (scores['a']['국어'] + scores['b']['국어']) / len(scores.keys())
music_avg = (scores['a']['음악'] + scores['b']['음악']) / len(scores.keys())
print("average of math is: {}".format(math_avg))
print("average of korean is: {}".format(lang_avg))
print("average of music is: {}".format(music_avg))


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
seoul_avg = sum(city['서울']) / len(city['서울'])
dajeon_avg = sum(city['대전']) / len(city['대전'])
print("서울의 평균 온도는 {}도였다.".format(seoul_avg))
print("대전의 평균 온도는 {}도였다.".format(dajeon_avg))

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
max_temp = 0
max_temp_city = ""
for key, vals in city.items():
    if max(vals) > max_temp:
        max_temp = max(vals)
        max_temp_city = key

min_temp = 0
min_temp_city = ""
for key, vals in city.items():
    if min(vals) < min_temp:
        min_temp = min(vals)
        min_temp_city = key
print("가장 추운 도시는 {0}로, 온도는 {1}였다.".format(min_temp_city, min_temp))
print("가장 더운 도시는 {0}로, 온도는 {1}였다.".format(max_temp_city, max_temp))
# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
temps = city['서울']
# flag = False
# for i in temps:
#     if i == 2:
#         flag = True
# if flag:
#     print("있다.")
# else:
#     print("없다.")
print(2 in city['서울'])