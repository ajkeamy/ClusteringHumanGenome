# Import Statements 
import pandas as pd
import numpy as np
import gzip
import shutil
import time 
import matplotlib.pyplot as plt
import os 
import shlex
import sys
import subprocess as sp
import json
import os
from etl import *


def main(): 
    # Import Json file
    dictionary = json.load(open("test-params.json"))

    arguments= sys.argv
    print(arguments)
    if arguments[1] == 'data-test':
        folder_manager()
        fastq_bam_converter(dictionary)
        get_dictionary_index(dictionary)
        bam_vcf_converter(dictionary, 'SP1.bam')

    

    if arguments[2] == 'process':
        filter_chromosomes()
        compress_vcf()
        merge_vcf()
        pca(dictionary['merged_file'])
        plotting(dictionary['eigenvalue'], dictionary['eigenvector'], dictionary['pop_code'])

if __name__ == '__main__':
    main()