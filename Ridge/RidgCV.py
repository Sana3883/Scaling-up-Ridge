import sklearn
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeCV
from threadpoolctl import threadpool_info
from pprint import pprint
import os
print(sklearn.__version__)

import numpy as np
print("***the current state of the threadpool-enabled runtime libraries that are loaded ")
pprint(threadpool_info())

def func():       
    
    Movie_Data= np.load('<path_to_your_Movie Data>/Movie_Data.npy', allow_pickle=True)
    fMRI_Data= np.load('<path_to_your_fMRI Data>/fMRI_Data.npy', allow_pickle=True)

    Movie_Data= np.vstack(Movie_Data)
    fMRI_Data= np.vstack(fMRI_Data)

    x_train,x_test, y_train, y_test = train_test_split(Movie_Data, fMRI_Data, test_size=0.1)
    print(x_train.shape,x_test.shape, y_train.shape, y_test.shape)


    start = time.time()
    print(start)     
    R=RidgeCV(alphas=[0.1, 1, 100,  200, 300, 400, 600,  800, 900, 1000, 1200], gcv_mode='svd').fit(x_train, y_train)   
    stop = time.time()
    print(stop)
    print(f"******%%%%%%****************************Training time: {stop - start}s")
    
if __name__ == "__main__":
    func()


