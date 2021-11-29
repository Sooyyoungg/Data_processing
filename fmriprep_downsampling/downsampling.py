#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import numpy as np
from nilearn import image
from nibabel.nifti1 import Nifti1Image
import nibabel as nib

def main(image_file, output_dir):
    # load our image
    #image_file = 'sub-NDARINVC868NEEC_ses-baselineYear1Arm1_task-rest_run-1_space-MNIPediatricAsym_cohort-4_res-2_desc-preproc_bold.nii.gz'
    # ex) time python3 downsampling.py /scratch/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-untar/fmriprep-deri-NDARINV003RTV85/fmriprep/sub-NDARINV003RTV85/ses-baselineYear1Arm1/func/sub-NDARINVC868NEEC_ses-baselineYear1Arm1_task-rest_run-1_space-MNIPediatricAsym_cohort-4_res-2_desc-preproc_bold.nii.gz
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
    subject = image_file.split('/')[-1].split('_')[0]
    session = image_file.split('_')[1]
    task = image_file.split('_')[2]
    run = image_file.split('_')[3]

    # Save information
    meta = {
            'subject': subject,
            'session': session,
            'task': task,
            'run': run,
            'filename': os.path.basename(image_file),
        }

    np.savez_compressed(output_dir, image = arr, **meta)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("image_file", type=str, help="echo the string you use here")
    parser.add_argument("output_dir", type=str, help="echo the string you use here")
    args = parser.parse_args()

    main(args.image_file, args.output_dir)
