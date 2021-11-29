#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import numpy as np
from nilearn import image
from nibabel.nifti1 import Nifti1Image
import nibabel as nib

# load oiur image
image_file = 'sub-NDARINVC868NEEC_ses-baselineYear1Arm1_task-rest_run-1_space-MNIPediatricAsym_cohort-4_res-2_desc-preproc_bold.nii.gz'
img = nib.load(image_file)
#print(img.shape)
#print(type(img))
#print(img.affine)

# Define new affine matrix size
aff_ds = np.diag((8, 8, 8))

# Downsampled image
img_ds = image.resample_img(img,target_affine=aff_ds)
arr = image.get_data(img_ds)

# Obtain image-related information
subject = image_file.split('_')[0]
session = image_file.split('_')[1]
task = image_file.split('_')[2]
run = image_file.split('_')[3]
print(subject, session, task, run)

# Save information
meta = {
            'subject': subject,
            'session': session,
            'task': task,
            'run': run,
            'filename': os.path.basename(image_file),
        }

np.savez_compressed('./result', image = arr, **meta)
        
    #nib.save(img_ds, '/scratch/06657/tg859565/practice.nii.gz')
