import math
import numpy as np

# Load stimuli data
Data1 = np.load('<path_to_your_video_files>/*_stimuli_S1.npy', allow_pickle=True)
Data2 = np.load('<path_to_your_video_files>/*_stimuli_S2.npy', allow_pickle=True)
Data3 = np.load('<path_to_your_video_files>/*_stimuli_S3.npy', allow_pickle=True)

# Stack the data
Data1 = np.vstack(Data1)
Data2 = np.vstack(Data2)
Data3 = np.vstack(Data3)


print(Data1.shape)
print(Data2.shape)
print(Data3.shape)


# Load fMRI data 
D1 = np.load('<path_to_your_fMRI_files>/*_Parcel_T1.npy', allow_pickle=True)
D2 = np.load('<path_to_your_fMRI_files>/*_Parcel_T2.npy', allow_pickle=True)
D3 = np.load('<path_to_your_fMRI_files>/*_Parcel_T3.npy', allow_pickle=True)


# Stack the fMRI data
D1 = np.vstack(D1)
D2 = np.vstack(D2)
D3 = np.vstack(D3)

print(D1.shape)
print(D2.shape)
print(D3.shape)


# Calculate rates
rate1 = len(Data1) / len(D1)
rate2 = len(Data2) / len(D2)
rate3 = len(Data3) / len(D3)


print(rate1, rate2, rate3)

# Process and save data for each season
for season in range(1, 4):
    count = []
    Movie_2 = []
    Data = locals()['Data{}'.format(season)]
    rate = locals()['rate{}'.format(season)]

    for j in range(len(Data)):
        if rate * j < len(Data):
            kk = math.floor(rate * j)
            CC = np.array(Data[kk])
            Movie_2.append(CC)

    np.save('Season{}_sub1.npy'.format(season), Movie_2)
    print("################################## season{}".format(season))
    MM2 = np.asarray(Movie_2)
    print(MM2.shape)

