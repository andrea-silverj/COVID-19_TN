#!usr/bin/env python3
from Bio import SeqIO
import sys
import re

args=sys.argv

fasta_1=args[1]

for rec in SeqIO.parse(fasta_1, "fasta"):
	print(">"+rec.id+"\n"+str(rec.seq))