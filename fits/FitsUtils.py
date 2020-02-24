#!/usr/local/bin/python3.5
# encoding: utf-8
'''
fits.FitsUtils -- shortdesc

fits.FitsUtils is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2020 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
from astropy.io import fits


#"../gag_evt_202001-12_v00.fits"
filePath = sys.argv[1]
# 检测Fits文件中所有的checksum
# Open the file pix.fits verifying the checksum values for all HDUs
def openFitsAndCheckSum(filePath,checkOrNot=True):
    hdul = fits.open(filePath,checksum=checkOrNot)
    checkState = hdul._open_kwargs['checksum']
    if (checkState):
        return 1
    else:
        return 0
    
print(openFitsAndCheckSum(filePath,True))

