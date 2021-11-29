# fmriprep_downsampling

To downsample resting state fMRI image by voxel size   
voxel size : (2, 2, 2) -> (8, 8, 8)

## Code
- downsampling_one.py : downsampling for only one subject's rsfMRI image
- downsampling.py : downsampling for input image and save the information including image to output path
- make_each_job_command.py : create job submission script for all subjects
