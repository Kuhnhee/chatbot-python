import webbrowser

url = "https://search.daum.net/search?q="
keywords = ["아이유", "설현", "수지"]
for name in keywords:
    webbrowser.open(url+name)