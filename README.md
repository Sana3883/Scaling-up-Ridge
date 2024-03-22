## README

### Overview
This repository contains scripts related to the paper titled "Scaling up ridge regression for brain encoding in a massive individual fMRI dataset". The paper evaluates different parallelization techniques to reduce the training time of brain
encoding with ridge regression on the CNeuroMod Friends dataset, one of the largest deep fMRI resource currently available.

### Directory Structure
- **Ridge:** Contains scripts related to ridge regression analysis, including ridgeCV regression, MultiOutput Ridge (MOR), and Batch-MultiOutput Ridge (B-MOR)  brain encoding scripts. Additionally, it includes a Dockerfile which provides information about the required settings and installations for B-MOR ridge regression.
- **Movie:** Contains Python scripts for extracting features from movies using a pretrained VGG16 model.
- **fMRI:** Contains Python scripts for generating fMRI data at three levels of resolution: parcel, ROI, and full brain.
- **notebooks:** Contains Jupyter notebooks and related CSV files for generating figures and visualizations presented in the paper.

