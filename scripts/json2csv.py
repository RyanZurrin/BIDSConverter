#!/usr/bin/env python3

import os
import json
import csv
import argparse

# define the headers for your csv file, you might want to adjust this to your needs
HEADERS = ["Subject",
           "Modality",
           "MagneticFieldStrength",
           "Manufacturer",
           "ManufacturersModelName",
           "InstitutionName",
           "InstitutionalDepartmentName",
           "InstitutionAddress",
           "DeviceSerialNumber",
           "StationName",
           "BodyPartExamined",
           "PatientPosition",
           "ProcedureStepDescription",
           "SoftwareVersions",
           "MRAcquisitionType",
           "SeriesDescription",
           "ProtocolName",
           "ScanningSequence",
           "SequenceVariant",
           "ScanOptions",
           "SequenceName",
           "ImageType",
           "SeriesNumber",
           "AcquisitionTime",
           "AcquisitionNumber",
           "ImageComments",
           "SliceThickness",
           "SpacingBetweenSlices",
           "SAR",
           "EchoTime",
           "RepetitionTime",
           "FlipAngle",
           "PartialFourier",
           "BaseResolution",
           "ShimSetting",
           "TxRefAmp",
           "PhaseResolution",
           "ReceiveCoilName",
           "ReceiveCoilActiveElements",
           "PulseSequenceDetails",
           "ConsistencyInfo",
           "MultibandAccelerationFactor",
           "PercentPhaseFOV",
           "EchoTrainLength",
           "PhaseEncodingSteps",
           "AcquisitionMatrixPE",
           "ReconMatrixPE",
           "BandwidthPerPixelPhaseEncode",
           "EffectiveEchoSpacing",
           "DerivedVendorReportedEchoSpacing",
           "TotalReadoutTime",
           "PixelBandwidth",
           "DwellTime",
           "PhaseEncodingDirection",
           "SliceTiming",
           "ImageOrientationPatientDICOM",
           "InPlanePhaseEncodingDirectionDICOM",
           "ConversionSoftware",
           "ConversionSoftwareVersion"]


def json2csv(root_dir, csv_file, headers=None, json_file_to_read=None):
    """  convert all json files in root_dir to a single csv file
    Args:
        root_dir (str): path to the root directory containing the json files
        csv_file (str): path to the csv file to be created
        headers (list): list of headers for the csv file
        json_file (str): name of the json file to be converted

    Returns:
        None
    """
    headers = headers or HEADERS
    json_file_to_read = json_file_to_read or "_MR_dMRI_dir98_AP.json"

    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()

        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if json_file_to_read in filename:
                    subject = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(os.path.join(dirpath, filename)))))
                    with open(os.path.join(dirpath, filename)) as json_file:
                        data = json.load(json_file)
                        data["Subject"] = subject
                        writer.writerow(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert json files to csv')
    parser.add_argument('--root_dir', '-r', type=str, required=True, help='path to the root directory containing the json files')
    parser.add_argument('--csv_file', '-c', type=str, required=True, help='path to the csv file to be created')
    parser.add_argument('--headers', '-hd', type=str, nargs='+', help='list of headers for the csv file')
    parser.add_argument('--json_file', '-j', type=str, help='name of the json file to be converted')
    args = parser.parse_args()

    # call the json2csv function with the parsed arguments
    json2csv(args.root_dir, args.csv_file, args.headers, args.json_file)

