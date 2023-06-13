#!/usr/bin/env python3

import os
import shutil
import argparse


def main(input_dir, output_dir):
    replacements = {
        'sub-': '',
        'ses-1_dir-416': '01',
        'ses-1_dir-398': '01',
        'ses-1_dir-216': '01',
        'ses-1_dir-405': '01',
        'desc-dwiXcUnEdEp': 'EdEp',
        'desc-XcUnEdEp_dwi': 'EdEp'
    }

    for filename in os.listdir(input_dir):
        new_filename = filename
        for old, new in replacements.items():
            new_filename = new_filename.replace(old, new)

        old_file_path = os.path.join(input_dir, filename)
        new_file_path = os.path.join(output_dir, new_filename)

        # Copy the file to the new location with the new name
        shutil.copy(old_file_path, new_file_path)
        print(f'Copied file {old_file_path} to {new_file_path}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", help="Directory with the original files")
    parser.add_argument("output_dir", help="Directory to save the renamed files")
    args = parser.parse_args()
    main(args.input_dir, args.output_dir)
