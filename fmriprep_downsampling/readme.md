# fmriprep_downsampling

Notion: https://caramel-log-9ed.notion.site/fmriprep-downsampling-9d4a8124b232469eb2598a410e77d661

To downsample resting state fMRI image by voxel size   
voxel size : (2, 2, 2) -> (8, 8, 8)

## Code
- downsampling_one.py : downsampling for only one subject's rsfMRI image
- downsampling.py : downsampling for input image and save the information including image to output path
- make_each_job_command.py : create job submission script for all subjects
