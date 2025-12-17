import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


def preprocess_data_aparts(PATH):
    """
    Preprocesses apartment data from a CSV file to prepare it for machine learning benchmarking.
    
    This method reads apartment data from a CSV file and performs essential data preparation steps
    including removing irrelevant features, extracting temporal components from date information,
    handling missing values, and organizing data chronologically. These preprocessing steps ensure
    the dataset is clean and properly structured for subsequent feature engineering and model training
    in fairness-aware machine learning pipelines.
    
    Args:
        PATH (str): The file path to the input CSV file containing raw apartment data.
    
    Returns:
        None. The method saves the processed data to 'train_data_aparts_pocessed.csv'
        in the current working directory.
    """
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
    """
    Separates features, sensitive attributes, and target variable from a dataset.
    
    This method partitions a pandas DataFrame into three distinct components to facilitate
    fairness-aware machine learning workflows: a feature matrix for model training, a sensitive
    attribute matrix for fairness analysis, and a target variable. By isolating sensitive
    attributes from the main feature set, this separation enables downstream fairness
    evaluations and constraint-based model training while maintaining the integrity of
    each component.
    
    Args:
        data: The input DataFrame containing all features, target variable, and
            sensitive attribute columns.
        target_name: The name of the column to be used as the target variable.
        sc_feat_name: The name of the column to be extracted as the sensitive
            attribute.
    
    Returns:
        A tuple containing three elements:
            - X: DataFrame of features with target and sensitive attribute removed,
                suitable for model training.
            - S: DataFrame containing only the sensitive attribute column for
                fairness analysis.
            - y: DataFrame containing only the target variable column.
    """
    X = data.drop(target_name, axis=1)
    y = data[[target_name]]
    
    S = X[[sc_feat_name]]
    X = X.drop(sc_feat_name, axis=1)
    
    return X, S, y


def encode_features_VAE(X, S, y, cat_cols_name, num_cols_name, sc_feat_type):
    """
    Prepares features and target variable for generative modeling by applying appropriate encoding and scaling transformations.
    
    This method standardizes input features, sensitive attributes, and target variables to ensure they are in a suitable format
    for advanced machine learning models. Categorical features are one-hot encoded, numerical features are normalized using 
    MinMaxScaler, and sensitive attributes are encoded according to their data type. The method carefully separates standard 
    features from sensitive attributes while maintaining the ability to reconstruct original values through returned scalers.
    
    Args:
        X (pd.DataFrame): Feature matrix containing both categorical and numerical columns.
        S (pd.Series or np.ndarray): Sensitive attribute column to be encoded.
        y (pd.Series or np.ndarray): Target variable to be encoded and scaled.
        cat_cols_name (list): Names of categorical columns in X to be one-hot encoded.
        num_cols_name (list): Names of numerical columns in X to be scaled.
        sc_feat_type (str): Type of sensitive attribute, either 'cat' for categorical (uses LabelEncoder)
            or 'num' for numerical (uses MinMaxScaler).
    
    Returns:
        tuple: A tuple containing five elements:
            - X_new (np.ndarray): Encoded and scaled feature matrix without sensitive attributes.
            - X_w_S (np.ndarray): Concatenated array of encoded sensitive attributes and encoded features.
            - S_new (np.ndarray): Encoded sensitive attribute array.
            - y_new (np.ndarray): Scaled target variable array.
            - scaler_dict (dict): Dictionary containing three fitted scalers with keys 'scaler_target',
                'scaler_num', and 'scaler_sc' for inverse transformations.
    
    Raises:
        AssertionError: If sc_feat_type is neither 'cat' nor 'num'.
    """
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