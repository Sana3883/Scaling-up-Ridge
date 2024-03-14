# Import necessary libraries
from load_confounds import Params24
from nilearn.input_data import NiftiLabelsMasker
import glob
import numpy as np
from nilearn.interfaces.fmriprep import load_confounds_strategy

# Define the path to the preprocessed fMRI data files
path='<path_to_your_fMRI_files>/*MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'

# Find all files matching the specified path
configfiles = glob.glob(path, recursive=True)

# Sort the file paths based on a specific key derived from the file names
def key_func(s):
    start = s.find('_task-')
    end = s.find('_space-')
    return s[start:end]

configfiles = sorted(configfiles, key=lambda s: key_func(s))    

print('#################### The number of bold_files:')
print(len(configfiles))

# Initialize lists to store fMRI data for each season
fMRI_T1 = []
fMRI_T2 = []
fMRI_T3 = []

# Initialize the NiftiLabelsMasker with desired parameters
masker = NiftiLabelsMasker(labels_img='MIST_444.nii.gz', standardize=True, detrend=False, smoothing_fwhm=8).fit()

# Loop through each fMRI data file
for img in configfiles:
    print(img)
    
    # Load confounds using a specified strategy
    conf = load_confounds_strategy(img, denoise_strategy='simple', global_signal='basic')
    
    # Transform the fMRI data using the masker and confounds
    Data_fmri = masker.transform(img, confounds=conf[0])
    print(Data_fmri.shape)
    
    # Append the transformed fMRI data to the corresponding season list based on file name
    if 's01e' in img:
        fMRI_T1.append(Data_fmri)
    if 's02e' in img:
        fMRI_T2.append(Data_fmri)
    if 's03e' in img:
        fMRI_T3.append(Data_fmri)


# Save the fMRI data for each season as numpy arrays
np.save('Sub1_Parcel_T1.npy', fMRI_T1)
np.save('Sub1_Parcel_T2.npy', fMRI_T2)
np.save('Sub1_Parcel_T3.npy', fMRI_T3)


print('##################### Done!')

