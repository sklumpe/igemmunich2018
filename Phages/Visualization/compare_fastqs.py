import sys
if len(sys.argv) < 2:
    print("Please enter AT LEAST ONE .fastq read file and lable with the explanation of the file for the plot in this format:"+"\n" +
          "label1-path_file1, label2-path_file2, label3-path_file3,... (Please don't use \"-\" anywhere else)"+"\n"+"Example:"+
      "\n"+"All T7 reads -T7/t7.fastq, Reads that did not mapped to E.coli K12 - T7/t7notAligned.fastq, All T4 reads -T4/t4.fastq Reads, Reads that did not mapped to E.coli K12 - T4/t4notAligned.fastq")
    exit()
sys.argv=(sys.argv[1:len(sys.argv)])
input_string= " ".join(sys.argv)
files = []
labels = []
array = input_string.split(",")
for a in array:
    labels.append(a.split("-")[0].strip())
    files.append(a.split("-")[1].strip())

for file in files:
    if not file.endswith(".fastq"):
        print("Please enter AT LEAST ONE .fastq read file and lable with the explanation of the file for the plot in this format:"+"\n" +
              "label1-path_file1, label2-path_file2, label3-path_file3,... (Please don't use \"-\" anywhere else)"+"\n"+"Example:"+
              "\n"+"All T7 reads -T7/t7.fastq, Reads that did not mapped to E.coli K12 - T7/t7notAligned.fastq, All T4 reads -T4/t4.fastq Reads, Reads that did not mapped to E.coli K12 - T4/t4notAligned.fastq")
        exit()
    
import HTSeq
import matplotlib.pyplot as plt
from matplotlib import colors

output = []
counter = 0
for file in files:
    reads = HTSeq.FastqReader(file)
    n_reads = 0
    for read in reads:
        n_reads += 1
    i = 0
    out = []
    for i in range(n_reads):
        out.append(counter)
    output.append(out)
    counter += 1

plt.ylabel('Number of reads', fontsize=8)
plt.xticks([])
plt.title('Comparison of sequencing data'+'\n'+'before and after mapping to E.coli K12', fontsize=12)
plt.hist(output, bins=1,  label=labels)
plt.legend(loc='upper right')
plt.savefig("fastq_comparison.png")
plt.close()
