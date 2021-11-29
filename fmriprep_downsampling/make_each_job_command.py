#!/bin/bash
import os
from path import Path
import numpy as np
import glob

# setting options for job submission
setting_script = '#!/bin/bash\n#$ -N Downsampling\n#$ -q all.q\n#$ -m ea\n#$ -S /bin/bash\n#$ -cwd\n#$ -l h_vmem=12G\n#$ -o ../tmp/log_$JOB_ID.output\n#$ -e ../tmp/log_$JOB_ID.error\n'

PATH_DATA = Path('/scratch/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-untar')

# find all data
dirs_input = sorted(PATH_DATA.glob('fmriprep-deri-*'))

# for all data
for sub_image in dirs_input:
    # sub_image (ex) /scratch/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-untar/fmriprep-deri-NDARINV003RTV85 

    # extract subject number
    # ex) NDARINV003RTV85
    sub_num =  sub_image.split('-')[-1]
    
    # set the basic path
    # ex) /scratch/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-untar/fmriprep-deri-NDARINV003RTV85/fmriprep/sub-NDARINV003RTV85/ses-baselineYear1Arm1/func/
    basic_path = PATH_DATA+'/fmriprep-deri-'+sub_num+'/fmriprep/sub-'+sub_num+'/ses-baselineYear1Arm1/func/'

    sub_run=[f for f in os.listdir(basic_path) if 'res-2_desc-preproc_bold.nii.gz' in f]

    # downsampling code path
    downsampling_code = '/scratch/bigdata/ABCD/abcd-fmriprep-rs/fmriprep_downsampling/downsampling.py'

    # output directory
    output_path = '/scratch/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-downsampling/fmriprep-deri-'+sub_num+'/fmriprep/sub-'+sub_num+'/ses-baselineYear1Arm1/func/'
    os.makedirs(output_path)

    for image_file in sub_run:
        # image_file (ex) sub-NDARINV0NK7MVCJ_ses-baselineYear1Arm1_task-rest_run-4_space-MNIPediatricAsym_cohort-4_res-2_desc-preproc_bold.nii.gz
        
        # set job script file name
        # file_name (ex) job_NDARINV10HWA6YU_2
        run_num = image_file.split('_')[3].split('-')[1]
        file_name = 'job_'+sub_num+'_run_'+run_num

       # output directory + file name 
        output_dir = output_path+image_file.split('.')[0]+'_ds'

        with open('./downsampling_job_command/'+file_name+'.txt', 'w') as f:
            f.writelines(setting_script)
            # ex) time python3 downsampling.py /scratch/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-untar/fmriprep-deri-NDARINV003RTV85/fmriprep/sub-NDARINV003RTV85/ses-baselineYear1Arm1/func/sub-NDARINVC868NEEC_ses-baselineYear1Arm1_task-rest_run-1_space-MNIPediatricAsym_cohort-4_res-2_desc-preproc_bold.nii.gz
            f.writelines('\n'+'time python3 '+downsampling_code+' '+basic_path+image_file+' '+output_dir)
            f.writelines('\n\nexit')
