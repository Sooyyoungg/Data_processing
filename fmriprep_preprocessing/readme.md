# Functional MRI Data Preprocessing
To pre-process fmri data, I apply atlas containing gordon and harvard-oxford

# Structure
https://app.cloudcraft.co/view/ae47fa94-1b9d-4f06-9424-109d5eb28864?key=aPv9-PX8Oa0JLRkBnr1eDA
![fmriprep_ABCD](https://user-images.githubusercontent.com/43199011/124473921-dc167380-ddda-11eb-8a9e-0dd9b12c54fd.png)

## Main directory
~~~Bash
/scratch/bigdata/ABCD/abcd-fmriprep-rs
~~~

## Preparing Data
- untar.sh : Untar each frmiprep tar data 
~~~Bash
/scratch/bigdata/ABCD/abcd-fmriprep-rs
~~~
- duplicate_untar.sh : Duplicate untared frmi data just in case 
~~~Bash
/scratch/bigdata/ABCD/abcd-fmriprep-rs
~~~

## Before using Job Scheduler
- timeseries.py : Apply atlas to extract timeseries data 
~~~Bash
/scratch/bigdata/ABCD/abcd-fmriprep-rs
~~~
- atlas_one.sh :  Apply timeseries.py code to a fmriprep of one subject 
~~~Bash
/scratch/bigdata/ABCD/abcd-fmriprep-rs/before_job_scheduler
~~~
- atlas.sh : Apply timeseries.py code to all of the fmri data 
~~~Bash
/scratch/bigdata/ABCD/abcd-fmriprep-rs/before_job_scheduler  
~~~
-> Finally, not using atlas_one.sh & atlas.sh

## After using Job Scheduler
- time_create_jobs.py : create jobs.txt >> /scratch/bigdata/ABCD/abcd-fmriprep-rs/after_job_scheduler
- jobs.txt : create commands for all subjects' fmri data >> /scratch/bigdata/ABCD/abcd-fmriprep-rs   
 ~~~Bash
 # example      
 /scratch/bigdata/ABCD/abcd-fmriprep-rs/time.sh /scratch/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-untar/fmriprep-deri-NDARINV0CTJAAHC/fmriprep/sub-NDARINV0CTJAAHC/ses-baselineYear1Arm1/func/sub-NDARINV0CTJAAHC_ses-baselineYear1Arm1_task-rest_run-1_space-MNIPediatricAsym_cohort-4_res-2_desc-preproc_bold.nii.gz        
 /scratch/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-time/fmriprep-deri-NDARINV0CTJAAHC
 ~~~

## Final using Job Scheduler
- make_each_job.sh : Dividing commands of jobs.txt into each subjects and saving as sh files    
~~~Bash 
/scratch/bigdata/ABCD/abcd-fmriprep-rs/final_job_scheduler
~~~

## Common Use
- time.sh : Apply timeseries.py code to a fmriprep of one subject (similar to atlas_one.sh)     
~~~Bash 
/scratch/bigdata/ABCD/abcd-fmriprep-rs 
~~~

## Details
each subject has several fmriprep images in terms of run
some subjects have 1-4 runs, others have 3 runs and the others have 5-6 runs.  
-> all names of the job text files include run number

# How the codes work
1. time_create_jobs.py : make jobs.txt
2. qsub -q all.q -l h_vmem=12G -cwd job* : implement job-{subject_ID}.txt script  
  -> if it doesn't work, use 'for j in job*; qsub -q all.q -l h_vmem=12G -cwd $j; done' command
4. time.sh : apply time.sh in job-{subject_ID}.txt     
> <img width="911" alt="스크린샷 2021-07-05 오후 9 22 42" src="https://user-images.githubusercontent.com/43199011/124471033-5ba24380-ddd7-11eb-9415-ced6c0877b58.png">
5. timeseries.py : apply atlas in time.sh.  
> <img width="594" alt="스크린샷 2021-07-05 오후 9 29 33" src="https://user-images.githubusercontent.com/43199011/124471681-221e0800-ddd8-11eb-9d77-ac0f620dfd59.png">

# Qsub
## Basic command
- qstat -f: check the queues
- qconf -sc: check the options of job
- qstat: check the running job
- qdel: stop the running queue

## Qsub options
- -q all.q: using all of the queues
- -l h_vmem: set the maximum memory amount
- -cwd: job file which I want to run
- -N: set the job name
