import os
from path import Path

setting_script = '#!/bin/bash\n#$ -N TIME\n#$ -q all.q\n#$ -m ea\n#$ -S /bin/bash\n#$ -cwd\n#$ -l h_vmem=10G\n#$ -o ../tmp/log_$JOB_ID.output\n#$ -e ../tmp/log_$JOB_ID.error\n'

jobs = open('/scratch/bigdata/ABCD/abcd-fmriprep-rs/jobs.txt')

while True:
    job_com = jobs.readline()
    
    sub_name = job_com.split()[-1]
    sub_num = sub_name.split('-')[-1]
    run_num = job_com.split()[1].split('/')[11].split('run-')[1].split('_')[0]

    file_name = 'job_'+sub_num+'_run_'+run_num

    out_com = 'time '+job_com

    with open('./job_command/'+file_name+'.txt', 'w') as f:
            f.writelines(setting_script)
            f.writelines('\n'+out_com)
            f.writelines('\nexit')
