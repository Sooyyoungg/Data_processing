#!/bin/bash

timestamp=$(date +"%T")
echo "$timestamp"

#base_path="/data/bigdata/ABCD/abcd-fmriprep-rs"
base_path="/scratch/bigdata/ABCD/abcd-fmriprep-rs"

file='fmriprep-deri-NDARINVZZLZCKAY'
#echo $file_name

cd $base_path/$file
mkdir atlas
cd fmriprep
sub_name=$(find -type d -name 'sub*')
cd $sub_name/ses-baselineYear1Arm1/func
	
bold_files=$(find . -name '*res-2_desc-preproc_bold.nii.gz')
for bold_image in $bold_files
do
	python3 $base_path/timeseries.py --file_input $bold_image --dir_output $base_path/$file/atlas #--dir_atlas $base_path
done

timestamp=$(date +"%T")
echo "$timestamp"
