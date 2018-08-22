#!/usr/bin python

import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

parser = argparse.ArgumentParser()
parser.add_argument("fasta", type=str, nargs=1)
parser.add_argument("o", type=str, nargs=1)
parser.add_argument("n", type=int, nargs=1)
parser.add_argument("ids", type=str, nargs='+')

args = parser.parse_args()

fasta_infile = args.fasta

with open(args.o[0], 'w') as fasta_outfile:

    sequences = []

    for record in SeqIO.parse(fasta_infile[0], "fasta"):

        # for each entry in input fasta file check if ID is meant to be manipulated
        if record.id in args.ids:
            length = len(record.seq)
            n = args.n[0]

            # fuse end of old sequence in front of beginning of old sequence, according to specified properties
            sequence_new = str(record.seq[length - n:length]) + str(record.seq[0:n])

            record = SeqRecord(Seq(sequence_new),
                               id=str(record.id),
                               description='indices: ('
                                           + str(length - n) + ',' + str(length - 1) + ')'
                                           + ' + (' + str(0) + ',' + str(n - 1) + ')')
            sequences.append(record)

    SeqIO.write(sequences, fasta_outfile, 'fasta')
