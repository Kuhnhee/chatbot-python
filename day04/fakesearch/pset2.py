import random
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scraping": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "jisu",
            "class president": "김병철",
            "groups": {
                "A": ["송치원", "정윤영", "이한얼", "이현빈", "박진홍"],
                "B": ["이수진", "정의진", "임우섭", "김민지", "이건희"],
                "C": ["이여진", "오재석", "김명훈", "이재인", "양찬우"],
                "D": ["김건호", "김윤재", "조동빈", "김병철", "김재현"]
            }
        },
        "gm":  {
            "lecturer": "justin",
            "manager": "pro-gm"
        },
        "gj": {
            "lecturer": "change",
            "manager": "pro-gj"
        }
    }
}


"""
난이도* 1. 지역(location)은 몇개 있나요? : list length
출력예시)
4
"""
print("----Q1----")
print(len(ssafy['location']))
"""
난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in
출력예시)
False
"""
print("----Q2----")
print('requests' in ssafy['language']['python']['python standard library'])
"""
난이도** 3. seoul반의 반장의 이름을 출력하세요. : depth 있는 접근
출력예시)
고승연
"""
print("----Q3----")
print(ssafy["classes"]["seoul"]["class president"])

"""
난이도*** 4. ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
출력 예시)
python
web
"""
print("----Q4----")
for i in ssafy["language"].keys():
    print(i)

"""
난이도*** 5 ssafy seoul반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
출력 예시)
change
pro-gj
"""
print("----Q5----")
for i in ssafy["classes"]["seoul"].keys():
    if i == "lecturer":
        print(ssafy["classes"]["seoul"]["lecturer"])
    elif i == "manager":
        print(ssafy["classes"]["seoul"]["manager"])

"""
난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
"""
print("----Q6----")
# 방법 1
print("--way1--")
fw = ssafy["language"]["python"]["frameworks"].keys()
for i in fw:
    spec = ssafy["language"]["python"]["frameworks"][i]
    print("{0}는 {1}이다.".format(i, spec))


# 방법 2
print("--way2--")
flask = list(ssafy["language"]["python"]["frameworks"].keys())[0]
django = list(ssafy["language"]["python"]["frameworks"].keys())[1]
flask_spec = ssafy["language"]["python"]["frameworks"][flask]
django_spec = ssafy["language"]["python"]["frameworks"][django]
print("{0}는 {1}이다.".format(flask, flask_spec))
print("{0}는 {1}이다.".format(django, django_spec))



"""
난이도***** 7. 오늘 Git pusher 뽑기 위해 groups의 A 그룹에서 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
출력예시)
오늘의 당번은 하승진
"""
print("----Q7----")
temp = ssafy['classes']['seoul']['groups']['A']
name = random.choice(temp)
print("오늘의 당번은 " + name)