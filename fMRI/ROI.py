# Import necessary libraries
from nilearn.input_data import NiftiMasker
import glob
import numpy as np
from nilearn.image import math_img

####################################################################
# Define the parcellation file path and create a binary mask for visual regions

parc = '<path_to_your_file>/template_cambridge_basc_multiscale_sym_scale007.nii.gz'
visual = math_img('img==4', img=parc)

# Initialize the NiftiMasker with specified parameters
masker = NiftiMasker(standardize=True, smoothing_fwhm=8, detrend=False, mask_img=visual)

####################################################################

# Define the path where fMRI data is stored
path='<path_to_your_files>/*MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'

# Globbing all file paths with the specified pattern
configfiles = glob.glob(path, recursive=True)

# Sorting the file paths based on custom key function
def key_func(s):
    start = s.find('_task-')
    end = s.find('_space-')
    return s[start:end]

configfiles = sorted(configfiles, key=lambda s: key_func(s))
print(len(configfiles))

#####################################################################

# Initialize lists to store fMRI data for each season
fMRI_T1=[]
fMRI_T2=[]
fMRI_T3=[]


# Loop through each file path
for path in configfiles:
    print(path)
    # Transform fMRI data using the masker
    Data_fmri = masker.fit_transform(path)
    print(Data_fmri.shape)

    # Append the transformed fMRI data to corresponding season list
    if 's01e' in path:
        fMRI_T1.append(Data_fmri)
    if 's02e' in path:
        fMRI_T2.append(Data_fmri)
    if 's03e' in path:
        fMRI_T3.append(Data_fmri)


# Save the lists of fMRI data for each season
np.save('2_Sub1_ROI_T1.npy', fMRI_T1)
np.save('2_Sub1_ROI_T2.npy', fMRI_T2)
np.save('2_Sub1_ROI_T3.npy', fMRI_T3)


print('##################### Done!')

