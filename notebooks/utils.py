import pandas as pd
import numpy as np
from collections import Counter
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def get_train_data():
    ecg_train = pd.read_csv("../data/raw/mitbih_train.csv",header=None)
    
    return ecg_train

def get_test_data():
    ecg_test = pd.read_csv("../data/raw/mitbih_test.csv",header=None)
    
    return ecg_test

def get_train_split():
    ecg_train = pd.read_csv("../data/raw/mitbih_train.csv",header=None)
    X_train = np.array(ecg_train.loc[:, 0:186])
    y_train = np.array(ecg_train.loc[:,187])

    return X_train,y_train

def get_test_split():
    ecg_test = pd.read_csv("../data/raw/mitbih_test.csv",header=None)
    X_test= np.array(ecg_test.loc[:, 0:186])
    y_test = np.array(ecg_test.loc[:,187])

    return X_test,y_test

def preprocess(X_train,y_train,X_test):
    counter = Counter(y_train)
    print(counter)
    
    # Instantiate SMOTE
    smote = SMOTE()

    # Apply SMOTE to balance the dataset
    X_train_processed, y_train_processed = smote.fit_resample(X_train, y_train)

    counter = Counter(y_train_processed)
    print(counter)

#####################################################################################

    # Create an instance of StandardScaler
    scaler = StandardScaler()

    # Fit the scaler on your data
    scaler.fit(X_train_processed)

    # Transform the data using the scaler
    X_train_scaled = scaler.transform(X_train_processed)

    # Calculate the mean and variance of the scaled data
    mean = np.mean(X_train_scaled, axis=0)
    variance = np.var(X_train_scaled, axis=0)

    # Check if the mean and variance are close to zero and one, respectively
    if np.allclose(mean, 0) and np.allclose(variance, 1):
        print("The features have zero mean and unit variance.")
    else:
        print("The features do not have zero mean and unit variance.")

#####################################################################################

    # Apply PCA
    pca = PCA(n_components=.95)  # Specify the desired number of components
    X_train_processed = pca.fit_transform(X_train_processed)
    X_test = pca.transform(X_test)

    # Explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_
    print("Explained variance ratio:", explained_variance_ratio)

    # Access the principal components
    principal_components = pca.components_
    print("Principal components:", principal_components)

    # Access the transformed data
    print("Transformed data shape:", X_train_processed.shape)

    cumulative_variance_ratio = np.cumsum(explained_variance_ratio)
    print(cumulative_variance_ratio)

    return X_train_processed, y_train_processed, X_test