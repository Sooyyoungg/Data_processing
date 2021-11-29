#!/bin/bash

SECONDS=0

DIR_CODE="/scratch/bigdata/ABCD/abcd-fmriprep-rs"

ATLAS=$1    #~~/sub-NDARINVPL7L6GEM_ses-baselineYear1Arm1_task-rest_run-1_space-MNIPediatricAsym_cohort-4_res-2_desc-preproc_bold.nii.gz
DIR_OUT=$2  #/scratch/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-time/fmriprep-deri-NDARINVPL7L6GE

FILENAME=$(basename $ATLAS)
sub_array=($(echo $FILENAME | tr "_" "\n"))
sub_name=${sub_array[0]}

FILE_OUT="$DIR_OUT/fmriprep/$sub_name/ses-baselineYear1Arm1/func"
#FILE_OUT_TEMP="/tmp"

mkdir -p $FILE_OUT

if [ ! -f "$FILE_OUT" ]; then
	/usr/bin/python3 $DIR_CODE/timeseries.py --file_input $ATLAS --dir_output $FILE_OUT

	#If the output directory does not exist, then generate a new directory
        if [ ! -d "$DIR_OUT" ]; then mkdir -p $DIR_OUT; fi 
	
	#cp $FILE_OUT_TEMP $FILE_OUT
        #rm $FILE_OUT_TEMP

        echo "Done - $FILENAME - $SECONDS"

else
        echo "Pass - $FILENAME - $SECONDS"
fi    
