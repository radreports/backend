from  dicom2fhir import dicom2fhir
from fhir import resources as fr
from fhir.resources.imagingstudy import ImagingStudy
# fhir.resources.imagingstudy.ImagingStudy
dicom_dir = "/Users/anilyerramasu/Development/deeponcology/backend/temp/test1"
response = dicom2fhir.process_dicom_2_fhir(dicom_dir)
print(response.id)
# print(response.identifier[0])
print(response.identifier[0].use)
print(response.identifier[0].system)
# result = ImagingStudy(response)
# ImagingStudy.
# response.json()
# print(response.status)
# fr.imagingstudy.ImagingStudy(response)
# result = fr.imagingstudy.ImagingStudy(response)
# print(type(response))