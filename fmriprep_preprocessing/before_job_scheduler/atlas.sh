#!/bin/bash

base_path="/data/bigdata/ABCD/abcd-fmriprep-rs/abcd-fmriprep-rs-untar"
cd $base_path
fmri_files=$(find . -name 'fmriprep-deri-*')
#echo $file_name

for file in $fmri_files
do
	cd $base_path
	cd $file
	mkdir atlas
	cd fmriprep
	sub_name=$(find -type d -name 'sub*')
	cd $sub_name/ses-baselineYear1Arm1/func
	
	bold_files=$(find . -name '*res-2_desc-preproc_bold.nii.gz')
	for bold_image in $bold_files
	do
		python3 $base_path/timeseries.py --file_input $bold_image --dir_output $base_path/$file/atlas --dir_atlas $base_path
	done
done
