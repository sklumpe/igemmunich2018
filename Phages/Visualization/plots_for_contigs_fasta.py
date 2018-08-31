import sys
if len(sys.argv) < 4:
    print("Please enter 3 parameters:"+"\n" + "1. name of the phage (for example: T4)"+"\n"+
          "2. path to .fasta file with contigs assembled from all reads"+"\n"+"3. path to .fasta file with contigs assembled from reads that were left after aligning to E.coli K12"+
          "\n"+"***if you do not have a file mensioned in 2. or 3. just type \"no\" instead of 2. or 3. parameter respectively")
    exit()

phage_name = sys.argv[1]
all_contigs_file = sys.argv[2]
notAligned_contigs_file = sys.argv[3]

if  not all_contigs_file.endswith(".fasta") and not all_contigs_file=="no":
    print("Please enter 3 parameters:"+"\n" + "1. name of the phage (for example: T4)"+"\n"+
          "2. path to .fasta file with contigs assembled from all reads"+"\n"+"3. path to .fasta file with contigs assembled from reads that were left after aligning to E.coli K12"+
          "\n"+"***if you do not have a file mensioned in 2. or 3. just type \"no\" instead of 2. or 3. parameter respectively")
    exit()

if  not notAligned_contigs_file.endswith(".fasta") and not notAligned_contigs_file=="no":
    print("Please enter 3 parameters:"+"\n" + "1. name of the phage (for example: T4)"+"\n"+
          "2. path to .fasta file with contigs assembled from all reads"+"\n"+"3. path to .fasta file with contigs assembled from reads that were left after aligning to E.coli K12"+
          "\n"+"***if you do not have a file mensioned in 2. or 3. just type \"no\" instead of 2. or 3. parameter respectively")
    exit()


import HTSeq
import matplotlib.pyplot as plt
from matplotlib import colors

contig_len=[]
reads_pro_contig=[]
notAligned_contig_len=[]
notAligned_reads_pro_contig=[]

if not all_contigs_file=="no":
    for s in HTSeq.FastaReader( all_contigs_file ):
        reads_pro_contig.append(int(s.descr.split(' ')[1].split('=')[1]))
        contig_len.append(int(s.descr.split(' ')[0].split('=')[1]))
    plt.ylabel('Frequency', fontsize=10)
    plt.xlabel('Number of mapped reads', fontsize=10)
    plt.title('Read mapping rate for all assembled contigs \n by analysing '+phage_name+' phage')
    plt.hist(reads_pro_contig, bins=100, color = "green")
    plt.savefig( phage_name+"_contigs_mapping_rate.png")
    plt.close()
    
    plt.ylabel('Frequency', fontsize=10)
    plt.xlabel('Contig length', fontsize=10)
    plt.title('Contigs length overview for all assembled contigs \n by analysing '+phage_name+' phage')
    plt.hist(contig_len, bins=100, color = "green")
    plt.savefig( phage_name+"_contigs_length.png")
    plt.close()

if not notAligned_contigs_file=="no":
    for s in HTSeq.FastaReader( notAligned_contigs_file ):
        notAligned_reads_pro_contig.append(int(s.descr.split(' ')[1].split('=')[1]))
        notAligned_contig_len.append(int(s.descr.split(' ')[0].split('=')[1]))
    
    plt.ylabel('Frequency', fontsize=10)
    plt.xlabel('Number of mapped reads', fontsize=10)
    plt.title('Read mapping rate for all contigs \n assembled from reads that were not mapped to E.coli K12 \n by analysing '+phage_name+' phage')
    plt.hist(notAligned_reads_pro_contig, bins=100, color = "red")
    plt.savefig( phage_name+"_notAligend_contigs_mapping_rate.png")
    plt.close()
    
    plt.ylabel('Frequency', fontsize=10)
    plt.xlabel('Contig length', fontsize=10)
    plt.title('Contigs length overview for all contigs \n assembled from reads that were not mapped to E.coli K12 \n by analysing '+phage_name+' phage')
    plt.hist(notAligned_contig_len, bins=100, color = "red")
    plt.savefig( phage_name+"_notAligned_contigs_length.png")
    plt.close()

if not notAligned_contigs_file=="no" and not all_contigs_file=="no":
    plt.ylabel('Frequency', fontsize=10)
    plt.xlabel('Number of mapped reads', fontsize=10)
    plt.title('Read mapping rate for contigs assembled from '+phage_name+' reads', fontsize=12)
    plt.hist([reads_pro_contig, notAligned_reads_pro_contig], bins=100, color = ["green", "red"], label=[ 'contigs assembled from all reads','contigs assembled from reads that \n did not match E.coli K12'])
    plt.legend(loc='upper right')
    plt.savefig( phage_name+"_mapping_rate.png")
    plt.close()
    
    plt.ylabel('Frequency', fontsize=10)
    plt.xlabel('Contig length', fontsize=10)
    plt.title('Contigs length overview for '+phage_name+' phage', fontsize=12)
    plt.hist([contig_len, notAligned_contig_len], bins=100, color = ["green", "red"], label=[ 'contigs assembled from all reads','contigs assembled from reads that \n did not match E.coli K12'])
    plt.legend(loc='upper right')
    plt.savefig( phage_name+"_length.png")
    plt.close()
