import requests
import bs4

url = "https://finance.naver.com/sise/"

response = requests.get(url).text
document = bs4.BeautifulSoup(response, "html.parser")

kospi = document.select_one('#KOSPI_now').text
kosdaq = document.select_one('#KOSDAQ_now').text
kospi200 = document.select_one('#KPI200_now').text

print('현재 코스피 지수는 : ' + kospi)
print('현재 코스닥 지수는 : ' + kosdaq)
print('현재 코스피200 지수는 : ' + kospi200)


#1등 검색어 뽑기
url_search = "https://www.naver.com/"
response_search = requests.get(url_search).text
document_search = bs4.BeautifulSoup(response_search, "html.parser")

first_place = document_search.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a.ah_a > span.ah_k').text
print('\n현재 검색어 1등은 : ' + first_place)


#상위 10개 검색어 가져오기 (select_one 사용한 ver)
print()
base_tag = "#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > "
for i in range(10):
    second_tag = "li:nth-child(" + str(i+1) + ") > a.ah_a > span.ah_k"
    full_tag = base_tag + second_tag
    current_keyword = document_search.select_one(full_tag).text
    print("{0}등 검색어는: {1}".format(i+1, current_keyword))


#상위 10개 검색어 가져오기 (select 사용한 ver)
print()
keyword_list = document_search.select("span.ah_k")
for i in range(10):
    current_keyword2 = keyword_list[i].text
    print("{0}등 검색어는: {1}".format(i+1, current_keyword2))