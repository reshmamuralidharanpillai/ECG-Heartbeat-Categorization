import pandas as pd

def get_train_data():
    url='https://drive.google.com/file/d/1dc3nkcw457egLXpfyFSjnz-eYsLFeOfa/view?usp=share_link'
    file_id=url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?id=' + file_id
    ecg_train = pd.read_csv(dwn_url,header=None)
    
    return ecg_train

def get_test_data():
    url='https://drive.google.com/file/d/1DCZzSml1yMbK7wsAxGHTOjNgkKC-OkWu/view?usp=share_link'
    file_id=url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?id=' + file_id
    ecg_test = pd.read_csv(dwn_url,header=None)
    
    return ecg_test

def get_train_split():
    x = np.array(ecg_train.loc[:, 0:186])
    y = ecg_train[187]

    return x,y

def get_test_split():
    X_test= np.array(ecg_test.loc[:, 0:186])
    y_test = ecg_test[187]

    return X_test,y_test