import requests
from bs4 import BeautifulSoup

today = dict()
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={}"
날씨 = "서울날씨"
url = url.format(날씨)
html = requests.get(url);
soup= BeautifulSoup(html.text,"html.parser");
now_temperate = soup.select_one(".temperature_text > strong ").text;
today[now_temperate[:5]]=now_temperate[5:]
dust = soup.select(".item_today > a > span")
title = soup.select(".item_today > a > strong")

for i in range(3):
    today[title[i].text]=dust[i].text
rain_wind = soup.select_one(".summary_list")
rain_wind_t = rain_wind.select(".term")
rain_wind_d = rain_wind.select(".desc");
for i in range(3):
    today[rain_wind_t[i].text]=rain_wind_d[i].text
temp = soup.select_one(".temperature_inner").text
print(temp)
print(today)