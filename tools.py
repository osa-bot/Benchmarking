import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


def preprocess_data_aparts(PATH):
    """
    Prepare apartment listings for downstream modeling.
    
        The function ingests a raw CSV containing real‑estate records and
        transforms it into a tidy, time‑aware feature set suitable for
        machine‑learning experiments.  It removes columns that are not
        useful for predictive modeling, normalises the date information
        into separate day, month, and year fields, discards rows with
        missing values, and orders the remaining observations chronologically.
        The cleaned data is then written to ``train_data_aparts_pocessed.csv``.
        This pipeline ensures that subsequent feature engineering and
        training steps operate on a consistent, well‑structured dataset.
    
        Why these steps?
        ----------------
        * **Dropping columns** – identifiers, location tags, and raw price
          fields are omitted because they either leak target information
          or are not needed for the current modeling task.
        * **Date decomposition** – extracting month and year allows models
          to capture seasonal or temporal trends that may influence
          apartment prices or demand.
        * **Missing‑value removal** – guarantees that algorithms that
          cannot handle NaNs receive a complete dataset.
        * **Chronological sorting** – many downstream analyses (e.g.,
          time‑series validation or sliding‑window training) assume
          data is ordered by time.
    
        Parameters
        ----------
        PATH : str
            Path to the input CSV file containing raw apartment data.
    
        Returns
        -------
        None
            The processed dataset is saved to ``train_data_aparts_pocessed.csv``
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
    Split a DataFrame into the components required for a typical supervised‑learning
    pipeline that also tracks a protected attribute.
    
    The routine removes the label and the sensitive column from the feature set so
    that models can be trained on a clean predictor matrix while still having
    the sensitive attribute available for fairness checks or post‑processing.
    This separation is a common first step in pipelines that enforce or evaluate
    equitable behavior.
    
    Args:
        data: A pandas DataFrame that contains every column used in the analysis.
        target_name: The column name that holds the target variable.
        sc_feat_name: The column name that represents the sensitive attribute.
    
    Returns:
        tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]
            * X – the feature matrix with the target and sensitive column removed.
            * S – a single‑column DataFrame holding the sensitive attribute.
            * y – a single‑column DataFrame containing the target variable.
    """
    X = data.drop(target_name, axis=1)
    y = data[[target_name]]
    
    S = X[[sc_feat_name]]
    X = X.drop(sc_feat_name, axis=1)
    
    return X, S, y


def encode_features_VAE(X, S, y, cat_cols_name, num_cols_name, sc_feat_type):
    """
    Prepares tabular data for a variational auto‑encoder that models both the main features
    and a sensitive attribute.  The routine converts categorical columns to one‑hot
    vectors, scales numeric columns and the target to the [0, 1] range, and encodes the
    sensitive attribute according to its type.  The resulting arrays can be fed
    directly into a VAE, while the returned scalers enable reconstruction of the
    original values after inference.
    
    Args:
        X (pd.DataFrame):
            DataFrame containing the predictor variables.  Columns listed in
            ``cat_cols_name`` are treated as categorical, those in ``num_cols_name``
            as numeric.
        S (pd.Series or np.ndarray):
            Sensitive attribute to be encoded.  Its type is specified by
            ``sc_feat_type``.
        y (pd.Series or np.ndarray):
            Target variable that will be scaled to the [0, 1] range.
        cat_cols_name (list[str]):
            Names of categorical columns in ``X``.
        num_cols_name (list[str]):
            Names of numeric columns in ``X``.
        sc_feat_type (str):
            Either ``'cat'`` to encode the sensitive attribute with a
            ``LabelEncoder`` or ``'num'`` to scale it with a ``MinMaxScaler``.
    
    Returns:
        tuple:
            X_new (np.ndarray):
                One‑hot encoded categorical features concatenated with min‑max
                scaled numeric features, excluding the sensitive attribute.
            X_w_S (np.ndarray):
                Same as ``X_new`` but with the encoded sensitive attribute
                prepended.
            S_new (np.ndarray):
                Encoded representation of the sensitive attribute.
            y_new (np.ndarray):
                Min‑max scaled target variable.
            scaler_dict (dict):
                Mapping of fitted scalers: ``'scaler_target'``, ``'scaler_num'``
                and ``'scaler_sc'`` for later inverse transforms.
    
    Raises:
        AssertionError:
            If ``sc_feat_type`` is not ``'cat'`` or ``'num'``.
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