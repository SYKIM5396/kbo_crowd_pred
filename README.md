# kbo_crowd_pred
한국프로야구 관중수를 예측하는 웹 애플리케이션을 제작하고 배포하는 프로젝트입니다

배포된 서비스 주소
https://kbo-crowd.herokuapp.com/

![kbo_crowd_pred](https://user-images.githubusercontent.com/110078574/199927041-dd565b59-1589-4cf3-8ca6-6387613155f6.jpg)

### data folder
data : 데이터를 수집하고 처리하며 적재하는 일련의 과정에 사용한 코드와 파일
+ scrape.py - 웹 스크레이핑을 이용하여 데이터 수집
+ crowd.csv - 수집한 데이터를 임시로 저장한 csv파일
+ ml.ipynb - 데이터 전처리 및 머신러닝 모델링 & 모델 피클링을 위한 쥬피터 노트북 파일
+ crowd_tr.csv - 전처리 완료된 csv파일
+ load.py - crowd_tr.csv를  mySQL에 적재하는 코드
+ model.pkl - 피클링된 모델의 pkl파일
+ mysql_schema.png 관계형 데이터베이스 mysql에 저장된 데이터의 스키마

### web folder
web : 웹 애플리케이션 개발에 사용한 코드와 파일
+ Procfile - 웹 애플리케이션 실행을 위한 명령어 지정파일
+ requirements.txt - 웹 에플리케이션 구동에 필요한 모듈 목록
+ flask_kbo - flask로 구현한 웹 애플리케이션 디렉토리
  + \_\_init_\_.py - 애플리케이션 구동을 위한 시동 파일
  + static - 정적파일을 불러오기 위한 디렉토리 경로
  + templates - 웹에서 보여지는 부분인 html파일이 위치한 경로
  + views - 실제로 웹 페이지에 구현할 내용을 위한 파이썬 코드파일 경로
    + main_views.py - 메인화면 렌더링을 위한 flask blueprint가 포함된 py파일
    + res_views.py - 예측 결과화면 렌더링을 위한 flask blueprint가 포함된 py파일
