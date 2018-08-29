#!/usr/bin python

import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# rearrange one contig according to different indices to resolve a possible repeat

parser = argparse.ArgumentParser()
# --fasta input, --o output, --id to be manipulated,
# --is index of repeat start, --ie index of repeat end

parser.add_argument("fasta", type=str, nargs=1)
parser.add_argument("o", type=str, nargs=1)
parser.add_argument("id", type=str, nargs=1)
parser.add_argument("istart", type=int, nargs=5)
parser.add_argument("iend", type=int, nargs=5)

args = parser.parse_args()

fasta_infile = args.fasta
with open(args.o[0], 'w') as fasta_outfile:
    for record in SeqIO.parse(fasta_infile[0], "fasta"):

        if record.id in args.id:

            original_record = record
            sequences = []
            count = 0
            length = len(record.seq)

            for index_start, index_end in zip(args.istart, args.iend):
                sequence_new = str(original_record.seq[index_start:length]) + str(original_record.seq[0:index_end + 1])

                record = SeqRecord(Seq(sequence_new),
                                   id=str(original_record.id) + '_' + str(count),
                                   description='indices: ('
                                               + str(index_start) + ',' + str(length - 1) + ')'
                                               + ' + (' + str(0) + ',' + str(index_end) + ')')

                sequences.append(record)
                count += 1

    SeqIO.write(sequences, fasta_outfile, 'fasta')
