"""
Alexandra Keamy 
A13589993
DSC 180A
Assignment 1: Data Ingestion
"""


# Import Statement 
import gzip
import shutil
import pandas as pd 
import gzip
import os
import requests
import urllib


def download_data(chrom, outpath):
        """
        Downloads the urls to get the path. 
        Checks to see if path exist. If no path exists,
        a new path  is made and added to directory. 
        Loops through json file, and retrieves
        urls. Renamed based on chromsome numbers and 
        print statement appears when finished
        """

    if not os.path.exists(outpath):
        os.mkdir(outpath)
    start = string.find('chr')+3
    string[start: start+ string[start:].find('.')]    
    # print('Downloading data from: {}'.format(chrom))
    for chr in chrom:
        start = string.find('chr')+3
        name = string[start: start+ string[start:].find('.')]    
        urllib.request.urlretrieve(links,f'{outpath}/chromosome_data/{name}.vcf.gz)                               
    print("File Downloaded")

    


# Unzips gzip files
def unzip_gz(url, outpath): 
    """ 
    The genetic data is downloaded in a format where it is 
    gz zipped. This function unzips the file
    """

    with gzip.open(url, 'rb') as f1:
        with open('file.txt', 'wb') as f2:
        shutil.copyfileobj(f1, f2)
