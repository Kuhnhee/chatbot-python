import requests
from decouple import config

token = config('TELEGRAM_TOKEN')
print(token)

base = "https://api.telegram.org"
method = "sendMessage"
method_update = "getUpdates"
chat_id = "880698577" #my chat_id = 884275913
text = "why"
url = f"{base}/{token}/{method}?chat_id={chat_id}&text={text}"
# url = base + token + method + "?" + "chat_id=" + chat_id + "&" + "text=" + text

url_update = base + token + method_update
print(url)
res = requests.get(url_update).text
print(res)

setwebhook = "https://api.telegram.org/bot884275913:AAEt1F_irUBmUAtkiRersxBeNtQeNCJSv-Q/setWebhook?=bdfb7da4.ngrok.io/884275913:AAEt1F_irUBmUAtkiRersxBeNtQeNCJSv-Q"
deletewebhook = "https://api.telegram.org/bot884275913:AAEt1F_irUBmUAtkiRersxBeNtQeNCJSv-Q/deleteWebhook"