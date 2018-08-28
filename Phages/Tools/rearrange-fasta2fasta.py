#!/usr/bin python

import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# rearrange one contig according to different indices

parser = argparse.ArgumentParser()
# --fasta input, --o output, --id to be manipulated, --i indices
parser.add_argument("fasta", type=str, nargs=1)
parser.add_argument("o", type=str, nargs=1)
parser.add_argument("id", type=str, nargs=1)
parser.add_argument("i", type=int, nargs='+')

args = parser.parse_args()

fasta_infile = args.fasta
with open(args.o[0], 'w') as fasta_outfile:
    for record in SeqIO.parse(fasta_infile[0], "fasta"):

        if record.id in args.id:
            length = len(record.seq)

            original_record = record
            sequences = []
            count = 0

            for i in args.i:
                sequence_new = str(original_record.seq[i:length]) + str(original_record.seq[0:i])

                record = SeqRecord(Seq(sequence_new),
                                   id=str(original_record.id) + '_' + str(count),
                                   description='indices: ('
                                               + str(i) + ',' + str(length - 1) + ')'
                                               + ' + (' + str(0) + ',' + str(i - 1) + ')')

                sequences.append(record)
                count += 1

    SeqIO.write(sequences, fasta_outfile, 'fasta')
