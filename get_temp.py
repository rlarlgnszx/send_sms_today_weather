import requests
from bs4 import BeautifulSoup
class Get_Temp:
    def __init__(self):
        self.today = dict()
        url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={}"
        날씨 = "서울날씨"
        url = url.format(날씨)
        html = requests.get(url);
        self.soup= BeautifulSoup(html.text,"html.parser");
        
    def get_temp(self):
        now_temperate = self.soup.select_one(".temperature_text > strong ").text;
        self.today[now_temperate[:5]]=now_temperate[5:]
        
    def get_dust(self):
        dust = self.soup.select(".item_today > a > span")
        title = self.soup.select(".item_today > a > strong")
        for i in range(3):
            self.today[title[i].text]=dust[i].text
            
    def get_rain_wind(self):
        rain_wind = self.soup.select_one(".summary_list")
        rain_wind_t = rain_wind.select(".term")
        rain_wind_d = rain_wind.select(".desc");
        for i in range(3):
            if rain_wind_t[i].text[:2]=="바람":
                self.today[rain_wind_t[i].text[:2]]=rain_wind_d[i].text
            else:
                self.today[rain_wind_t[i].text]=rain_wind_d[i].text
    def get_max_min(self):
        min_max = self.soup.select_one(".temperature_inner").text
        self.today["최저최고"] = min_max
        
        
    def start(self):
        self.get_temp()
        self.get_rain_wind()
        self.get_dust()
        self.get_max_min()
        return self.today
    
start = Get_Temp()
result = start.start()
print(result)

        
