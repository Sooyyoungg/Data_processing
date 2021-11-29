#!/bin/bash

import os
from path import Path
import numpy as np
import glob

PATH_DATA = Path('/scratch/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-untar')
PATH_OUT = Path('/scratch/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-time')

# 
SH_file = '/scratch/bigdata/ABCD/abcd-fmriprep-rs/time.sh'

cmds = []
dirs_input = sorted(PATH_DATA.glob('fmriprep-deri-*'))

for fprep in dirs_input:
    # extract sub name
    sub_num=os.path.basename(fprep) #-> split해서 마지막 이름만 받기
    sub_name=sub_num.split('-')[2]

    sub_run_folder=fprep+'/fmriprep/sub-'+sub_name+'/ses-baselineYear1Arm1/func'
    sub_run=[f for f in os.listdir(sub_run_folder) if 'res-2_desc-preproc_bold.nii.gz' in f]

    # return the base name from the path
    dir_out = str(PATH_OUT / os.path.basename(fprep))
    for s_run in sub_run:
        # cmds from : .sh file + input file(npz) + (output path+sub_name)
        cmds.append(' '.join([SH_file, str(sub_run_folder+'/'+s_run), dir_out, '\n']))

with open('./jobs.txt', 'w') as f:
    f.writelines(cmds)
