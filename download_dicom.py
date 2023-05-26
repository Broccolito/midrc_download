import pydicom
import numpy as np
from PIL import Image
import pandas as pd
import os
from dicom_csv import join_tree
import subprocess

cred = "/mnt/c/Users/SimonsonLab/Desktop/download_midrc/credentials.json" # change this file path

object_ids = ['dg.MD1R/624578c1-6c62-4358-8f5f-ebd2fc480c49',
'dg.MD1R/c3d7828d-630d-44c8-8f07-40bbd9125712',
'dg.MD1R/2b7b40cb-87a7-483c-b4d0-1ebcdb081c42',
'dg.MD1R/a5621c8e-8de1-4181-af83-f1dd6de541e4',
'dg.MD1R/1c5722da-3752-4d9d-aa57-1bdacaebe43a',
'dg.MD1R/31fa2439-b463-48d7-baee-478801621710',
'dg.MD1R/a88ff562-9c43-4d3e-be45-296a56df556c',
'dg.MD1R/c0de8602-3a2a-4e16-85c6-3ed99391fc92',
'dg.MD1R/ae47c0e6-0233-4de4-809a-b8c72896b5a9',
'dg.MD1R/ddf489c1-9c93-421d-ae64-4bdb1cb5120c']

for object_id in object_ids:
    cmd = "gen3 --auth {} --endpoint data.midrc.org drs-pull object {}".format(cred,object_id)
    # display(cmd)
    subprocess.run(cmd, shell=True, capture_output=True)

