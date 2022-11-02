import pymysql
from sqlalchemy import create_engine
import pandas as pd

# MYSQL DB 접속 엔진 객체 생성
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1q2w3e', db='project', charset='utf8')
cur = db.cursor()

#테이블 생성
cur.execute("DROP TABLE IF EXISTS crowd;")
cur.execute("DROP TABLE IF EXISTS day;")
cur.execute("DROP TABLE IF EXISTS home;")
cur.execute("DROP TABLE IF EXISTS away;")
cur.execute("DROP TABLE IF EXISTS stadium;")

cur.execute("""CREATE TABLE day (
	Id INT NOT NULL PRIMARY KEY,
    day VARCHAR(10)
    );
""")
cur.execute("""CREATE TABLE home (
	Id INT NOT NULL PRIMARY KEY,
    home VARCHAR(10)
    );
""")
cur.execute("""CREATE TABLE away (
	Id INT NOT NULL PRIMARY KEY,
    away VARCHAR(10)
    );
""")
cur.execute("""CREATE TABLE stadium (
	Id INT NOT NULL PRIMARY KEY,
    stadium VARCHAR(10)
    );
""")
cur.execute("""CREATE TABLE crowd (
	Id INT NOT NULL PRIMARY KEY,
    dayId INT,
    homeId INT,
    awayId INT,
    stadiumId INT,
    crowd INT,
    FOREIGN KEY(dayId) REFERENCES day(Id),
	FOREIGN KEY(homeId) REFERENCES home(Id),
    FOREIGN KEY(awayId) REFERENCES away(Id),
	FOREIGN KEY(stadiumId) REFERENCES stadium(Id)
    );
""")

day_data = [
    [1,"화"],
    [2,"수"],
    [3,"목"],
    [4,"금"],
    [5,"토"],
    [6,"일"]
]
team_data = [
    [1,"KIA"],
    [2,"KT"],
    [3,"LG"],
    [4,"NC"],
    [5,"SSG"],
    [6,"두산"],
    [7,"롯데"],
    [8,"삼성"],
    [9,"키움"],
    [10,"한화"]
]
std_data = [
    [1,"고척"],
    [2,"광주"],
    [3,"대구"],
    [4,"대전"],
    [5,"문학"],
    [6,"사직"],
    [7,"수원"],
    [8,"울산"],
    [9,"잠실"],
    [10,"창원"],
    [11,"포항"]
]


#데이터 인서트
for a in  day_data:
    cur.execute("INSERT INTO day (Id, day) VALUES (%s,%s)", a)
    
for a in  team_data:
    cur.execute("INSERT INTO home (Id, home) VALUES (%s,%s)", a)

for a in  team_data:
    cur.execute("INSERT INTO away (Id, away) VALUES (%s,%s)", a)
    
for a in  std_data:
    cur.execute("INSERT INTO stadium (Id, stadium) VALUES (%s,%s)", a)


df = pd.read_csv('crowd_tr.csv')

df.day =df.day.replace( {'화':1,'수':2,'목':3,'금':4,'토':5,'일':6} ).astype(int)
df.home = df.home.replace( {"KIA":1, "KT" :2, "LG":3 , "NC":4, "SSG":5, "두산":6, "롯데":7, "삼성":8 , "키움":9 , "한화" : 10}  ).astype(int)
df.away = df.away.replace( {"KIA":1, "KT" :2, "LG":3 , "NC":4, "SSG":5, "두산":6, "롯데":7, "삼성":8 , "키움":9 , "한화" : 10}  ).astype(int)
df.stadium = df.stadium.replace( {"고척":1, "광주" :2, "대구":3 , "대전":4, "문학":5, "사직":6, "수원":7, "울산":8 , "잠실":9 , "창원" : 10, "포항" : 11}  ).astype(int)


for row in df.itertuples():
    cur.execute("""INSERT INTO crowd (
        Id, dayId, homeId, awayId, stadiumId, crowd) values(%s,%s,%s,%s,%s,%s)""",
        (row[0],row[1], row[2], row[3], row[4], row[5]) )
 

db.commit()

cur.close()
db.close()