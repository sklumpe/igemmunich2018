#!/usr/bin python

import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

#rearrange one contig according to different indices

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

            sequences = []

            for i in args.i:
                sequence_new = str(record.seq[i:length]) + str(record.seq[0:i])

                record = SeqRecord(Seq(sequence_new),
                                   id=str(record.id),
                                   description='indices: ('
                                               + str(i) + ',' + str(length - 1) + ')'
                                               + ' + (' + str(0) + ',' + str(i - 1) + ')')

                sequences.append(record)

    SeqIO.write(sequences, fasta_outfile, 'fasta')