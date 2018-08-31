import sys
if len(sys.argv) < 3:
    print("Please enter input file (.fasta) and output file (.fasta)!")
    exit()
input_file = sys.argv[1]
output_file = sys.argv[2]
if  not (input_file.endswith(".fasta") and output_file.endswith(".fasta")):
    print("Please enter input file (.fasta) and output file (.fasta)!")
    exit()
import HTSeq
sequence=None
max_len = 0
max_sequence =None
my_fasta_file = open( output_file, "w" )
for s in HTSeq.FastaReader( input_file ):
    if(max_len<len(s.seq)):
        max_len=len(s.seq)
        max_sequence=HTSeq.Sequence(s.seq, name=s.descr)
    if(len(s)>100000):
        sequence = HTSeq.Sequence(s.seq, name=s.descr)
        sequence.write_to_fasta_file( my_fasta_file )
if sequence is None:
    max_sequence.write_to_fasta_file( my_fasta_file )
my_fasta_file.close()
