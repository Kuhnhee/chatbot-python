import requests
from bs4 import BeautifulSoup as bs

# 1. op.gg에 요청을 보낸다.
url = "https://www.op.gg/summoner/userName=cuzz"

# 2. html 응답을 받아
res = requests.get(url)

# 3. html 안에 있는 정보를 출력
doc = bs(res.text, "html.parser")
win = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')

print(win.text) # <span class="wins">241W</span> default set은 영어. 브라우저에 의해 W->"승" 변환


