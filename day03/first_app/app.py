from flask import Flask
import random
import requests
import bs4
from datetime import datetime
app = Flask(__name__)

# 1.주문 받는 방식(어떻게)
@app.route("/")
# 2. 무엇을 제공할지(무엇)
def hello():
    return "Hello World!"

# 1.주문 받는 방식(어떻게)
@app.route("/hi")
# 2. 무엇을 제공할지(무엇)
def hi():
    return "hi"

# 1. /name
# 2. 여러분의 영문이름
@app.route("/name")
def name():
    return "Kuhnhee Lee"


@app.route("/hello/<person>")   
def greeting(person):
    return "hello, {0}".format(person)


# /cube/1 = 1^3,   /cube/2 = 2^8
@app.route("/cube/<num>")
def cube(num):
    return str(int(num)**3)

# random lotto 번호 추천
@app.route("/lotto")
def lotto():
    numbers = range(1,46)
    lotto = random.sample(numbers, 6)
    c = ''.join(str(n) for n in lotto)
    return "오늘의 로또 추천번호는...<h1>{0}</h1>를 추천합니다.".format(c)

# random 점심메뉴 추천
@app.route("/lunch")
def lunch():
    menu = ["김밥", "피자", "햄버거", "삼겹살", "파스타"]
    choice = random.choice(menu)
    return "오늘의 점심 메뉴로는...{0}를 추천합니다.".format(choice)

# /kospi => 현재 네이버 기준 kospi
@app.route("/kospi")
def kospi():
    url = "https://finance.naver.com/sise/"

    response = requests.get(url).text
    document = bs4.BeautifulSoup(response, "html.parser")

    kospi = document.select_one('#KOSPI_now').text
    kosdaq = document.select_one('#KOSDAQ_now').text
    kospi200 = document.select_one('#KPI200_now').text

    msg = "현재 코스피 지수는: {0}<br> 현재 코스닥 지수는: {1}<br> 현재 코스피200 지수는: {2}".format(kospi, kosdaq, kospi200)
    return msg

# /newyear
@app.route("/newyear")
def newyear():
    #만약 오늘이 1월 1일 이라면 예, 아니면 아니요.
    flag = (datetime.now().month == 1 and datetime.now().day == 1)
    
    if flag:
        return "<h1>예</h1>"
    else:
        return "<h1>아니요</h1>"


# /index
@app.route("/index")
def index():
    return "<html><head></head><body><h1>홈페이지</h1><p>이건 내용</p></body></html>"
