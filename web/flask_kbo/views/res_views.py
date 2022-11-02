from flask import Blueprint, request ,render_template
import pickle
import pandas as pd
import numpy as np

res_bp = Blueprint('res', __name__)

def pred(day,home,away,stadium):
    with open('./flask_kbo/model.pkl','rb') as pickle_file:
        model = pickle.load(pickle_file)
    X_test = pd.DataFrame([[day,home,away,stadium]],columns=['day','home','away','stadium'])
    result = np.round(model.predict(X_test)) #요일 홈팀 원정팀 구장 데이터를 넣어 머신러닝 predict
    return result

@res_bp.route('', methods=['GET','POST'])
def calculate():
    day = request.form.get('day')  #POST로 데이터를 받을경우 form.get사용
    home = request.form.get('home')
    away = request.form.get('away')
    stadium = request.form.get('stadium')
    list1 = [day,home,away,stadium]
    res = round(pred(day,home,away,stadium)[0])
    return render_template('index.html', list1=list1, result=res)
    
