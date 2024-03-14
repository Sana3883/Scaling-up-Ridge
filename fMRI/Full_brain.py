# Importing necessary libraries
from nilearn.input_data import NiftiMasker
import glob
import numpy as np
from nilearn.interfaces.fmriprep import load_confounds_strategy

# Defining the path where the preprocessed bold files are located
path='<path_to_your_files>/*MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'

# Finding all bold file paths recursively in the specified directory
configfiles = glob.glob(path, recursive=True)

# Defining a function to extract task information for sorting
def key_func(s):
    start = s.find('_task-')
    end = s.find('_space-')
    return s[start:end]

# Sorting the bold files based on the task information extracted
configfiles=sorted(configfiles, key=lambda s: key_func(s))    


print('#################### The number of bold_files:')
print(len(configfiles))

# Defining lists to store fMRI data for different seasons
fMRI_T1=[]
fMRI_T2=[]
fMRI_T3=[]


# Defining the mask file path
mask= '<path_to_your_files>/sub-01_ses-001_task-s01e01b_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'

# Creating a NiftiMasker object for preprocessing
masker = NiftiMasker(standardize=True, smoothing_fwhm=8 , detrend=True, mask_img=mask).fit()

# Iterating through each bold file
for img in configfiles: 
    
    print(img)
    
    # Loading confound regressors using fmriprep's load_confounds_strategy function
    conf = load_confounds_strategy(img, denoise_strategy='simple', global_signal='basic')
    
    # Transforming the fMRI data using the NiftiMasker object
    Data_fmri=masker.transform(img, confounds=conf[0]) 

    # Printing the shape of the transformed data
    print(Data_fmri.shape)
    
    path=img
   
    if 's01e' in path:
        fMRI_T1.append(Data_fmri)

    if 's02e' in path:
        fMRI_T2.append(Data_fmri)

    if 's03e' in path:
        fMRI_T3.append(Data_fmri)


# Saving the season-wise fMRI data as numpy arrays
np.save('Sub1_Full_T1.npy', fMRI_T1)
np.save('Sub1_Full_T2.npy', fMRI_T2)
np.save('Sub1_Full_T3.npy', fMRI_T3)


print('##################### Done!########')

