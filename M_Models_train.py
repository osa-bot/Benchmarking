# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:32:05 2025

На входе 'deals6.csv' - подготовленный в M_Data_prep.py для обучения моделей
'id' - млентификатор объекта, 
'Цена' - цена фактическая, 
'Площадь квартиры', 
'Этаж', 
'Район', 
'day',date' - дата заключения сделки,
'количество этажей всего', 
'высота объекта',
'Этажность объекта подземная', 
'Этажность объекта наземная',
'Количество квартир',
'Общая площадь объекта',
'Площадь жилых помещений объекта', 
'lon', 'lat' - десятичные географические координаты объекта, 
'rooms', 'floor' количество комнат и этаж из описания квартиры,
'Квартиры среднего качества (типовые)' - индекс цен к IV кварталу 2024 года,
'nprice' - цена с учётом индекса, 
'metroprox' - близость к метро по евклидову расстоянию,
'rwprox'  - близость к железнодорожным станциям,
'medprox'  - близость к поликлиникам,
'kidprox'  - близость к детским садам,
'schoolprox'  - близость к школам,
'cemetprox'  - близость к кладбищам,
'industrprox'  - близость к промышленным объектам и складам,
'daysin', 'daycos' - кодированный день года для сезонности, 
'liveratio' - отношение жилой площади к общей для УИН, 
'highratio'- отношение высоты к количеству этажей для УИН, 
'pricemetr' - цена кв. метра приведённая к IV кварталу 2024
@author: user
"""
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import pickle
import time

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

def seconds_to_str(seconds): #Секунды в строку ЧЧ:ММ:СС, на входе скалярно
    mm, ss = divmod(seconds, 60)
    hh, mm = divmod(mm, 60)
    return "%02d:%02d:%02d" % (hh, mm, ss)
    
print('Let\'s get started')
print(time.asctime())
s=time.time()
df=pd.read_csv('data/train_data.csv')
moddir='models/'

df.drop(df[df['pricemetr']>1.5].index, inplace=True)

ccl=['id', 
     'Площадь квартиры',
     'количество этажей всего','Количество квартир', 'высота объекта','Этажность объекта наземная',
     'lat', 'lon', 
     'metroprox', 'rwprox','medprox','kidprox','schoolprox','cemetprox','industrprox', 
     'daysin', 'daycos', 
     'floor', #'rooms',
     'liveratio', 'highratio',
     'nprice', 'pricemetr'
     ]#'rooms',
df[ccl].dropna()

for model, name in zip([KNeighborsRegressor(n_neighbors=5),
                        GradientBoostingRegressor(n_estimators=100, learning_rate=0.7),
                        RandomForestRegressor(n_estimators=50, min_samples_split=2, min_samples_leaf=1)],
                       ['KNN', 'GBoost', 'RF']):
    print(name)
    s2=time.time()
    for per_meter in [True, False]:
        X=df[ccl].dropna().drop(['id', 'nprice', 'pricemetr'], axis=1)
        if per_meter:
            print('Price per meter forecast')
            y=df[ccl].dropna().pricemetr
        else:
            print('Oblect price forecast')
            y=df[ccl].dropna().nprice
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        X_train.shape, y_train.shape
        
        #model=RandomForestRegressor(n_estimators=50, min_samples_split=2, min_samples_leaf=1)
        model.fit(X_train, y_train)
        print('\tR^2_test:%.2f; R^2_train:%.2f'%(model.score(X_test,y_test), model.score(X_train,y_train)))
        
        y_pred=model.predict(X_test)
        y_pr_tr=model.predict(X_train)
        err1, err2 = mean_absolute_percentage_error(y_test, y_pred), mean_absolute_percentage_error(y_train, y_pr_tr)
        print('\tMAPE_test:%.1f%%; MAPE_train:%.1f%%'%(err1*100,err2*100))
        
        if per_meter:
            filen=name+'_model_pm.pkl'
        else:
            filen=name+'_model.pkl'
        with open(moddir+filen, 'wb') as f:
            pickle.dump(model, f)
        f.close()
        print('Model saved as %s'%filen)
    print('Time:', seconds_to_str(time.time()-s2),'\n')
print('Time total:', seconds_to_str(time.time()-s))
print(time.asctime())
print('Bye')

