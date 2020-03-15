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
import seaborn as sns



 
def folder_manager(dictionary):
    """ 
    Folder set-up to get store results. Create folder to grab 
    reference genome.
    """
     # Make Data Source folder
    os.system('mkdir data_source')
    # Make folder containing reference genome
    os.system('mkdir ref_genome')
    # make folder containing data for PCA/merging/zipping
    os.system('mkdir data_sourcer')
    # Copy reference genome to directory
    os.system("cp -r " + dictionary['reference'] + "* ref_genome")


def fastq_bam_converter(dictionary):
    """
    Convert Fastq files to BAM.
    Store Index of the reference genome. 
    """
     # Convert FastQ file to BAM
    os.system('bwa mem ' +  dictionary['ref_genome_file'] + " " + dictionary['fq_testfile'] + ' | ' + 'samtools sort -o SP1.bam')
    # Get reference genome as dictionary


def get_dictionary_index(dictionary): 
    """
    Convert reference genome to dictionary
    Store Index of the reference genome. 
    """
    os.system('gatk CreateSequenceDictionary -R ' + dictionary['ref_genome_file'] 
    + ' -O ref_genome/Homo_sapiens_assembly38.dict')
    # Get index from reference genome
    os.system('samtools faidx ' + dictionary['ref_genome_file'])
    

def bam_vcf_converter(dictionary, filename):
    """
    Convert BAM files to VCF.
    """
    # Add or replace: input is create from fast_bam_converter
    os.system('gatk AddOrReplaceReadGroups \
    -I filename -O align.bam -RGLB lib1 -RGPL pilot -RGPU SRR008003 -RGSM 20')
    #Convert Bam to VCF
    os.system('gatk HaplotypeCaller -R ' + dictionary['ref_genome_file'] + \
    ' -I align.bam -O ref_genome/bam_vcf_converted.vcf')

def filter_chromosomes(dictionary):
    """
    Filter chromosomes using Plink2 commands.
    Filter using maf, mind, geno, and snps only.
    Output as VCF File. 
    """
    os.system('plink2 --vcf ' + dictionary['ch19'] +  ' --make-bed --snps-only --maf ' + \
    str(dictionary['maf_value']) + ' --geno ' + str(dictionary['geno_value']) + \
    " --mind " + str(dictionary['mind_value']) +  ' --recode vcf --out data_sourcer/cleaned_ch19')

def filter_chromosomes(dictionary):
    """
    Filter chromosomes using Plink2 commands.
    Filter using maf, mind, geno, and snps only.
    Output as VCF File. 
    """
    os.system('plink2 --vcf ' + dictionary['ch19'] +  ' --make-bed --snps-only --maf ' + \
    str(dictionary['maf_value']) + ' --geno ' + str(dictionary['geno_value']) + \
    " --mind " + str(dictionary['mind_value']) +  ' --recode vcf --out data_sourcer/cleaned_ch19')
    os.system('plink2 --vcf ' + dictionary['ch20'] +  ' --make-bed --snps-only --maf ' + \
    str(dictionary['maf_value']) + ' --geno ' + str(dictionary['geno_value']) + \
    " --mind " + str(dictionary['mind_value']) +  ' --recode vcf --out data_sourcer/cleaned_ch20')
    os.system('plink2 --vcf ' + dictionary['ch21'] +  ' --make-bed --snps-only --maf ' + \
    str(dictionary['maf_value']) + ' --geno ' + str(dictionary['geno_value']) + \
    " --mind " + str(dictionary['mind_value']) +  ' --recode vcf --out data_sourcer/cleaned_ch21')
    os.system('plink2 --vcf ' + dictionary['ch22'] +  ' --make-bed --snps-only --maf ' + \
    str(dictionary['maf_value']) + ' --geno ' + str(dictionary['geno_value']) + \
    " --mind " + str(dictionary['mind_value']) +  ' --recode vcf --out data_sourcer/cleaned_ch22')
   
  
def compress_vcf():
    """ 
    Take in filter chromosomes and compress
    it it gz format.
    """
    os.system('bgzip -c data_sourcer/cleaned_ch19.vcf > data_sourcer/cleaned_ch19.vcf.gz')
    os.system('bgzip -c data_sourcer/cleaned_ch20.vcf > data_sourcer/cleaned_ch20.vcf.gz')
    os.system('bgzip -c data_sourcer/cleaned_ch21.vcf > data_sourcer/cleaned_ch21.vcf.gz')
    os.system('bgzip -c data_sourcer/cleaned_ch22.vcf > data_sourcer/cleaned_ch22.vcf.gz')

    
def merge_vcf():
    """
    Merge VCF Files. 
    """
    os.system('bcftools concat data_sourcer/cleaned_ch19.vcf.gz data_sourcer/cleaned_ch20.vcf.gz \
    data_sourcer/cleaned_ch21.vcf.gz data_sourcer/cleaned_ch22.vcf.gz -o data_sourcer/merge_all_vcf.vcf')
    
def pca(mergedfile):
    """
    Run PCA on merged file 
    """
    os.system('%time !plink2 --vcf mergedfile --pca 2')
    

def plotting(eigenval, eigenvec, population_tsv):
    """
    Plotting PCA using eigen vectors and Eigen values.
    Labeling clusters using population codes. 
    """
    val = pd.read_csv(eigenval, header= None)
    vec = pd.read_csv(eigenvec, delimiter=' ',header=None, names= ['Sample name','pop','x','y'])
    codes= pd.read_csv(population_tsv,sep='\t')[['Sample name', 'Sex', 'Superpopulation code']]
    eigen_pop= vec.join(codes.set_index('Sample name'), on= 'Sample name')
    plotting = sns.scatterplot(x=eigen_pop.x, y= -1 * eigen_pop.y, hue=eigen_pop['Superpopulation code'])
    plotting.figure.savefig("pca_all22.png")


