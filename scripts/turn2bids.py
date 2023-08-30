#!/usr/bin/env python3
import os
import shutil
import argparse

"""
Given a root directory with files in the following format:
1001_01_EdEp.bval
1001_01_EdEp.bvec
1001_01_EdEp.nii.gz
1001_01_EdEp_mask.nii.gz
1002_01_EdEp.bval
1002_01_EdEp.bvec
1002_01_EdEp.nii.gz
1002_01_EdEp_mask.nii.gz
1004_01_EdEp.bval
1004_01_EdEp.bvec
1004_01_EdEp.nii.gz
1004_01_EdEp_mask.nii.gz
...

Organize the files into the following format:
HCPEP
├── 1001_01_MR
│   └── harmonization
│       ├── 1001_01_EdEp.bval
│       ├── 1001_01_EdEp.bvec
│       ├── 1001_01_EdEp.nii.gz
│       └── 1001_01_EdEp_mask.nii.gz
├── 1002_01_MR
│   └── harmonization
│       ├── 1002_01_EdEp.bval
│       ├── 1002_01_EdEp.bvec
│       ├── 1002_01_EdEp.nii.gz
│       └── 1002_01_EdEp_mask.nii.gz
├── 1004_01_MR
│   └── harmonization
│       ├── 1004_01_EdEp.bval
│       ├── 1004_01_EdEp.bvec
│       ├── 1004_01_EdEp.nii.gz
│       └── 1004_01_EdEp_mask.nii.gz
...

"""


def main(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        # Get the subject ID from the filename
        subject_id = filename[:7]

        # Create the corresponding directories if they do not exist
        subject_dir = os.path.join(output_dir, f"{subject_id}_MR", "harmonization")
        os.makedirs(subject_dir, exist_ok=True)

        # Construct old and new file paths
        old_file_path = os.path.join(input_dir, filename)
        new_file_path = os.path.join(subject_dir, filename)

        # Copy the file to the new location
        shutil.copy(old_file_path, new_file_path)
        print(f'Copied file {old_file_path} to {new_file_path}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", help="Directory with the original files")
    parser.add_argument("output_dir", help="Root directory to save the organized files")
    args = parser.parse_args()
    main(args.input_dir, args.output_dir)
