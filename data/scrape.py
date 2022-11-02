import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.koreabaseball.com/History/Crowd/GraphDaily.aspx'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('tbody').find_all('tr')

csvFile = open("crowd.csv","a", encoding='utf-8')
writer = csv.writer(csvFile)
writer.writerow (('day','home','away','stadium','crowd'))

#파싱한 html에서 요일 홈 원정 구장 관중수 데이터를 찾아 한줄씩 csv파일에 입력한다.
for game in table:
    tmp = game.find_all('td')
    day = tmp[1].getText()
    home = tmp[2].getText()
    away = tmp[3].getText()
    stadium = tmp[4].getText()
    crowd = tmp[5].getText()
    writer.writerow((day,home,away,stadium,crowd))

csvFile.close()
    
    
        
