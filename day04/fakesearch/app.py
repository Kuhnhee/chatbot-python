from flask import Flask, render_template, request
from faker import Faker
import random
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)
fake = Faker('ko_KR')

#랜덤직업
nameJob_dict = {}

#궁합 보여주기
# pair_dict = {}
double_dict = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pastlife')
def pastlife():
    return render_template('pastlife.html')

@app.route('/pastlife/result')
def pastlife_result():
    name = request.args.get("name")

    # 동일한 이름일 경우 동일한 직업이 출력되도록 하자.
    if name in nameJob_dict:
        job = nameJob_dict[name]
    else:
        job = fake.job()
        nameJob_dict[name] = job

    return render_template('pastlife_result.html', job=job, name=name)

@app.route('/chemistry')
def chemistry():
    return render_template('chemistry.html')

@app.route('/chemistry/result')
def chemistry_result():

    babo = request.args.get("babo")
    you = request.args.get("you")

    # # pair data saved in pair_dict (tuple 사용한 방식)
    # if (babo,you) in pair_dict:
    #     num = pair_dict[(babo,you)]
    # else:
    #     num = random.randint(51,100)
    #     pair_dict[(babo,you)] = num #fake chemistry number

    # pair data saved in double_dict & in_dict (dict in dict 방식)
    if babo not in double_dict:
        double_dict[babo] = {}
    if (babo in double_dict) and (you not in double_dict[babo]):
        double_dict[babo][you] = random.randint(51,100)
    num = double_dict[babo][you]


    return render_template('chemistry_result.html', babo=babo, you=you, num=num)

@app.route('/admin')
def admin():

    msg = ""
    for key, val in double_dict.items():
        val_list = [v for v in val]
        val_string = ",".join(val_list)
        temp_msg = "{0}는 {1}에게 흥미가 있어보인다..\n".format(key, val_string)
        msg += temp_msg
        
    return render_template('admin.html', msg=msg)

@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/opgg/search')
def opgg_search():

    ID = request.args.get("ID")
    
    # 1. op.gg에 요청을 보낸다.
    url = "https://www.op.gg/summoner/userName=" + ID

    # 2. html 응답을 받아
    res = requests.get(url)

    # 3. html 안에 있는 정보를 출력
    doc = bs(res.text, "html.parser")
    win_raw = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins').text
    lose_raw = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses').text

    win = win_raw[:len(win_raw)-1]
    lose = lose_raw[:len(lose_raw)-1]

    return render_template('opgg_search.html', ID=ID, win=win, lose=lose)

if __name__=='__main__':
    app.run(debug=True)

