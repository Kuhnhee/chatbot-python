from flask import Flask, render_template, request
from decouple import config
from pprint import pprint
import requests
import decouple
import random

app = Flask(__name__)
token = config('TELEGRAM_TOKEN')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send')
def send():
    msg = request.args.get('msg')

    base = "https://api.telegram.org"
    method_msg = "sendMessage"
    method_update = "getUpdates"
    chat_id = "880698577" #my chat_id = 884275913

    #chat_id를 가져오는 코드
    #1. getUpdates 메소드로 요청 보내기
    #2. 받아온 응답(json)을 dictonary로 바꿔서 첫번째 메세지의 chat 아이디를 가져온다
    url_upd = f"{base}/bot{token}/{method_update}"
    status = requests.get(url_upd).json()   #json -> dict 변환
    chat_id = status["result"][0]["message"]["chat"]["id"]

    #home에 보내온 msg를 받아 telegram api를 통해 메세지 전송
    url_msg = f"{base}/bot{token}/{method_msg}?chat_id={chat_id}&text={msg}"
    requests.get(url_msg) # 최종 메세지를 보내줌

    return render_template('send.html')

@app.route(f'/{token}', methods=['POST'])   #web hook이 들어오는
def webhook():
    '''
    1. 메아리 챗봇
    (1) webhook을 통해 telegram 보낸 요청 안에 있는 메세지를 가져와
    (2) 그대로 전송
    '''
    res = request.get_json()
    text = res.get("message").get("text")
    chat_id = res.get("message").get("chat").get("id")
    chat_msg = res.get("message").get("text")
    pprint(res)

    base = "https://api.telegram.org"
    method_msg = "sendMessage"

    #lotto를 물어보면 번호를 추첨해주도록 하자.
    numbers = range(1,46)
    lotto = sorted(random.sample(numbers, 6))
    lotto_msg = ','.join(str(n) for n in lotto)

    # /번역 댕댕이 -> 번역결과 출력
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    headers = {
        "X-Naver-Client-Id" : config('NAVER_ID'),
        "X-Naver-Client-Secret" : config('NAVER_SECRET')
    }
    data = {
        'source' : 'ko',
        'target' : 'en',
        'text' : chat_msg[4:]
    }
    trans_data = requests.post(papago_url, headers=headers, data=data).json()
    translated_msg = trans_data['message']['result']['translatedText']
    # pprint(res.json())

    
    # 파일 받았을 때 인식시키기
    # .get()을 사용하면 있을때~ 없을때~ 분기 가능
    if res.get("message").get("photo")[-1].get('file_id') is not None:
        file_id = res.get("message").get("photo")[-1].get('file_id')
        file_res = request.get(f"{base}/bot{token}/getFile?file_id={file_id}")
        file_path = file_res.json().get("result").get("file_path")
        file_url = f"{base}/file/bot{token}/{file_path}"        # 다운로드 url

        # 파일 다운로드. file stream이 날라올거야~ 명시
        image = requests.get(file_url, stream=True) 

        url = "https://openapi.naver.com/v1/vision/celebrity"

        headers = {
            "X-Naver-Client-Id" : config('NAVER_ID'),
            "X-Naver-Client-Secret" : config('NAVER_SECRET')
        }

        files = {
            'image' : image.raw.read(),
        }

        clova_res = requests.post(url, headers=headers, files=files)
        text = clova_res.json().get('faces')[0].get('celebrity').get('value')

    # 텍스트 메세지인가?
    else:
        if (chat_msg == "lotto"):
            text = lotto_msg
        elif (chat_msg[:3] == "/번역"):
            text = translated_msg


    url_msg = f"{base}/bot{token}/{method_msg}?chat_id={chat_id}&text={text}"
    requests.get(url_msg) # 최종 메세지를 보내줌

    return '', 200 #tuple 형태. 200: 잘 들어오고 있어요~ 라는 상태코드

if __name__ == "__main__":
    app.run(debug=True)