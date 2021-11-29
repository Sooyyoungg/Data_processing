##module import
import os
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from nilearn import image, input_data
from nilearn import datasets
import nilearn

##
# atlas가 있는 default directory
# WORK 환경변수 설정
#PATH_ATLAS_DEFAULT = (
#    Path(os.environ['WORK']) / 'atlas' if 'WORK' in os.environ else
#         Path(os.getcwd()) / 'atlas' # 현재위치
#)

PATH_ATLAS_DEFAULT=Path('/scratch/bigdata/ABCD/abcd-fmriprep-rs/atlas_nii')

##
# output 이름 지정할 때 사용
FILES_ATLAS = [
    'atlas-gordon.nii',
    'atlas-harvardoxford_cort-maxprob-thr25.nii',
]


# npy로 바꾸는 코드
def extract_atlas_timeseries(file_atlas, file_input, img_input, dir_atlas, dir_output):
    code_atlas = file_atlas.split('/')[-1].split('_')[0].replace('.nii','')
    file_output = Path(dir_output)/file_input.split('/')[-1].replace(
        '_bold.nii.gz',
        f'_{code_atlas}_timeseries.npy'
    )

    masker = input_data.NiftiLabelsMasker(
        labels_img = os.path.join(dir_atlas, file_atlas),standardize=True,
    )
    ts = masker.fit_transform(img_input)
    np.save(str(file_output),ts)

def main(file_input,dir_output, dir_atlas):
    img_input = image.load_img(file_input)

    for file_atlas in FILES_ATLAS:
        extract_atlas_timeseries(file_atlas,file_input,img_input,dir_atlas,dir_output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Extract segmented signals from the fMRI image.')

    # output
    parser.add_argument('--file_input', type=str,
                        help = 'Input fMRI image file')
    parser.add_argument('--dir_output',type=str,
                        help='Directory to store outputs')
    parser.add_argument('--dir_atlas',type=str, default=PATH_ATLAS_DEFAULT,
                        help='Directory to find atlas')

    args = parser.parse_args()

    main(args.file_input, args.dir_output, args.dir_atlas)
    # timeseries.py --file_input {input이름} --dir_output {output directory} 형태
