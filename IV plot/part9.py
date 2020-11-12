# -*- coding: utf-8 -*-

import os
import argparse
import time
import argparse
import glob
import os

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
from final import final

# arg parser
parser = argparse.ArgumentParser()
parser.add_argument('folder_path', help='C:\\Users\\...', type=str)
parser.add_argument('sample', help='batch', type=str)
parser.add_argument('list', help='list of contacts to plot', nargs=argparse.REMAINDER)

##---

def main():
    print("Main")
    args = parser.parse_args()
    print("folder_path: ", args.folder_path)
    print("sample: ", args.sample)
    print("files: ", args.list)

    final().final1(folderpath=args.folder_path, files=args.list, sample=args.sample)
    

if __name__ == '__main__':
    main()

#################################################################################################
# What to write in CMD example:

# FIRST TYPE: 
# cd C:\Users\nikit\Documents\GaAs\CV_plots\IV_new

# THEN TYPE: 
# python part9.py C:\\Users\\nikit\\Documents\\GaAs\\share\\V1\\scratch\\2 B9Ba 1 11 2 12
#################################################################################################
