from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/greet/<name>")
def greet(name):
    #name에는 "/hello/이름"의 이름이 들어감.
    return render_template('greet.html', username=name)

@app.route("/menu")
def menu():
    #랜덤으로 음식 메뉴를 추천하고, 해당 음식의 사진을 보여주는 기능을 구현
    hamburg = "https://recipes-secure-graphics.grocerywebsite.com/0_GraphicsRecipes/4589_4k.jpg"
    pizza = "https://upload.wikimedia.org/wikipedia/commons/a/a3/Eq_it-na_pizza-margherita_sep2005_sml.jpg"
    taco = "https://cbmpress.com/toronto/wp-content/uploads/sites/3/2017/08/tacomain-01.jpg"
    menu_dict = {"햄버거":hamburg, "피자":pizza, "타코":taco}
    choice_menu = random.choice(list(menu_dict))
    choice_pic = menu_dict[choice_menu]
    return render_template("menu.html", name=choice_menu, pic=choice_pic)

# /lotto 랜덤 넘버를 추천해주고, 최신 로또와 비교하여 등수를 알려주는 기능
@app.route("/lotto")
def lotto():

    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url) 
    dict_lotto = res.json()    #json file이 dict 구조로 들어온 것.
    
    # winner에 1등 당첨 번호를 넣기
    winner = [dict_lotto["drwtNo" + str(i)] for i in range(1,7)] 

    same_cnt = 0
    my_lotto = sorted(random.sample(range(1,46), 6))     # 로또 랜덤 추천

    same_cnt = len(set(winner) & set(my_lotto)) # 교집합
    
    if same_cnt==6:
        place = "1등"
    elif same_cnt==5:
        place = "2등"
    elif same_cnt==4:
        place = "3등"
    elif same_cnt==3:
        place = "4등"
    else:
        place = "꽝"

    return render_template("lotto.html", winner=str(winner), my_lotto=str(my_lotto), place=place)
    

if __name__ == "__main__":
    app.run(debug=True)