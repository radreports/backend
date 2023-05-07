from pydicom import dcmread
from pydicom.data import get_testdata_file
from pydicom.filereader import read_dicomdir
from pathlib import Path
from pprint import pprint
import os
from pydicom.data import get_testdata_files
# fpath = get_testdata_file("CT_small.dcm")
# ds = dcmread(fpath)
# print("Patient Name:",ds.PatientName)
# print("Patient Age:",ds.PatientAge)
# print("Study id::",ds.StudyInstanceUID)
# print("series ID::",ds.SeriesInstanceUID)

fpath = "temp/tmpkt13nns9/tmpfwsn9jrr/"
# filepath = "../temp/test1/"

fpath = "../temp/test1"
dicom_set = []
for root, _, filenames in os.walk(fpath):
    for filename in filenames:
        dcm_path = Path(root,filename)
        if dcm_path.suffix == ".dcm":
            try:
                dicom = dcmread(dcm_path,force = True )
            except IOError as e:
                print("Error ---")
            else:
                dicom_set.append(dicom)

print(dicom_set[0].PatientName)
print(dicom_set[0].PatientID)
print(dicom_set[0].Modality)
print(dicom_set[0].StudyID)
print(dicom_set[0].StudyDate)
print(dicom_set[0].StudyTime)
print(dicom_set[0].StudyInstanceUID)
print(dicom_set[0].SOPClassUID)
print(dicom_set[0].StudyDescription)
# print(dicom_set[0].StudyDescription)
print(dicom_set[0].SeriesInstanceUID)




# print(dicom_set[0].file_meta)