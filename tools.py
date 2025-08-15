import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


def preprocess_data_aparts(PATH):
    data = pd.read_csv(PATH)
    data = data.drop(['Этаж', 'Район', 'id', 'date', 'rooms', 'Цена', 'nprice'], axis=1)
    data['day'] = pd.to_datetime(data['day'])
    data['date'] = data['day']
    data['month'] = data['day'].dt.month
    data['year'] = data['day'].dt.year
    data['day'] = data['day'].dt.day
    data = data.dropna()
    data = data.sort_values(by='date').reset_index(drop=True)
    data = data.drop('date', axis=1)
    data.to_csv('train_data_aparts_pocessed.csv', index=False)
    
    
def separate_features(data: pd.DataFrame, target_name: str, sc_feat_name: str):
    X = data.drop(target_name, axis=1)
    y = data[[target_name]]
    
    S = X[[sc_feat_name]]
    X = X.drop(sc_feat_name, axis=1)
    
    return X, S, y


def encode_features_VAE(X, S, y, cat_cols_name, num_cols_name, sc_feat_type):
    #encode target variable
    scaler_target = MinMaxScaler()
    y_new = scaler_target.fit_transform(y)
    
    #encode features
    X_cat = pd.get_dummies(X[cat_cols_name].astype(str)).astype(float)
    scaler_num = MinMaxScaler()
    X_num = scaler_num.fit_transform(X[num_cols_name])
    X_new = np.concatenate([X_cat, X_num], axis=1)
    
    #encode scenario feature
    if sc_feat_type == 'cat':
        scaler_sc = LabelEncoder()
        S_new = scaler_sc.fit_transform(S)
        
    elif sc_feat_type == 'num':
        scaler_sc = MinMaxScaler()
        S_new = scaler_sc.fit_transform(S)
        
    else:
        assert 'Wrong feature type. Available: cat and num'
    
    scaler_dict = {'scaler_target': scaler_target,
                   'scaler_num': scaler_num,
                   'scaler_sc': scaler_sc}
    
    X_w_S = np.concatenate([S_new, X_new], axis=1)
    
    return X_new, X_w_S, S_new, y_new, scaler_dict