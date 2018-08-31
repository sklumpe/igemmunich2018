import sys
if len(sys.argv) < 4:
    print("Please enter 3 parameters:"+"\n" + "1. name of the phage (for example: T4)"+"\n"+
      "2. path to .fastq file with all reads"+"\n"+"3. path to .fastq file with reads that were left after aligning to E.coli K12"+
      "\n"+"***if you do not have a file mensioned in 2. or 3. just type \"no\" instead of 2. or 3. parameter respectively")
    exit()
    
phage_name = sys.argv[1]
all_reads_file = sys.argv[2]
left_reads_file = sys.argv[3]

if  not all_reads_file.endswith(".fastq") and not all_reads_file=="no":
    print("Please enter 3 parameters:"+"\n" + "1. name of the phage (for example: T4)"+"\n"+
      "2. path to .fastq file with all reads"+"\n"+"3. path to .fastq file with reads that were left after aligning to E.coli K12"+
      "\n"+"***if you do not have a file mensioned in 2. or 3. just type \"no\" instead of 2. or 3. parameter respectively")
    exit()
if  not left_reads_file.endswith(".fastq") and not left_reads_file=="no":
    print("Please enter 3 parameters:"+"\n" + "1. name of the phage (for example: T4)"+"\n"+
      "2. path to .fastq file with all reads"+"\n"+"3. path to .fastq file with reads that were left after aligning to E.coli K12"+
      "\n"+"***if you do not have a file mensioned in 2. or 3. just type \"no\" instead of 2. or 3. parameter respectively")
    exit()

import HTSeq
import matplotlib.pyplot as plt
from matplotlib import colors

if not all_reads_file=="no":
    reads = HTSeq.FastqReader(all_reads_file)
    n_reads = 0
    len_reads=[]
    for read in reads:
        len_reads.append(len(read.seq))
        n_reads= n_reads + 1
    plt.ylabel('Frequency', fontsize=10)
    plt.xlabel('Length of reads', fontsize=10)
    plt.title('Length frequencies of all '+str(n_reads)+' reads by sequencing '+phage_name, fontsize=12)
    plt.hist(len_reads, bins=100, color='green')
    plt.savefig(phage_name +"_all_reads.png")
    plt.close()

if not left_reads_file=="no":
    notAligned_reads = HTSeq.FastqReader(left_reads_file)
    notAligned_n_reads = 0
    notAligned_len_reads=[]
    for read in notAligned_reads:
        notAligned_len_reads.append(len(read.seq))
        notAligned_n_reads= notAligned_n_reads + 1
    plt.ylabel('Frequency', fontsize=10)
    plt.xlabel('Length of reads', fontsize=10)
    plt.title('Length frequencies of '+ str(notAligned_n_reads) +' reads \n that were not aligned to E.coli K12 by sequencing '+phage_name, fontsize=12)
    plt.hist(notAligned_len_reads, bins=100, color='red')
    plt.savefig(phage_name +"_notAligned_reads.png")
    plt.close()

if not left_reads_file=="no" and not all_reads_file=="no":
    plt.ylabel('Frequency', fontsize=10)
    plt.xlabel('Length of reads', fontsize=10)
    plt.title('Comparison of '+ phage_name +' sequencing data'+'\n'+'before and after mapping to E.coli K12', fontsize=12)
    plt.hist([notAligned_len_reads, len_reads], bins=100, color = ["red","green"], label=[str(notAligned_n_reads) +' reads that did not match E.coli K12', 'all '+ str(n_reads) +' reads'])
    plt.legend(loc='upper right')
    plt.savefig(phage_name +"reads_comparison.png")
    plt.close()
