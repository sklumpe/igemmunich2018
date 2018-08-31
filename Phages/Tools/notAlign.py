import sys
import matplotlib.pyplot as plt
if len(sys.argv) < 3:
    print("Please enter input file (.sam) and output file (.fastq)!")
    exit()
input_file = sys.argv[1]
output_file = sys.argv[2]
if  not (input_file.endswith(".sam") and output_file.endswith(".fastq")):
    print("Please enter input file (.sam) and output file (.fastq)!")
    exit()
import HTSeq
import numpy as np
alignment_file = HTSeq.SAM_Reader(input_file)
len_reads=[]
my_fastq_file = open( output_file, "w" )
for aln in alignment_file:
    if not aln.aligned:
        len_reads.append(len(aln.read.seq))
        if len(aln.read.seq)>200:
            myread = HTSeq.SequenceWithQualities( aln.read.seq, aln.read.name, aln.read.qualstr )
            myread.write_to_fastq_file( my_fastq_file )
my_fastq_file.close()
import matplotlib.pyplot as plt
%matplotlib inline
plt.hist(len_reads, bins=10)
plt.savefig(output_file+".png")
