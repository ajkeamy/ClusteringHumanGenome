# Imports
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


def plotting():
    eigenvec = pd.read_csv('plink.eigenvec', delimiter=' ',header=None, names= ['a','b','x','y'])
    pca = plt.scatter(eigenvec['x'], eigenvec['y'], s=2)
    plt.savefig('pca.png')


if __name__ == '__main__':
    arguments= sys.argv
    print(arguments)
    if arguments[1] == 'data-test':
        os.system('chmod 700 src/test.sh')
        os.system('./src/test.sh')
    

    if arguments[2] == 'process':
        os.system('chmod 700 src/process.sh')
        os.system('./src/process.sh')
    
        plotting()

