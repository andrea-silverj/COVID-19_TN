#!usr/bin/env python3
from Bio import SeqIO
import sys

args=sys.argv

fasta_1=args[1]
ids=args[2]
op_ids=open(ids, "r")
list_op_ids=list(op_ids)

list_ids=[]
for i in list_op_ids:
	list_ids+=[i.strip("\n")]

for rec in SeqIO.parse(fasta_1, "fasta"):
	if rec.id in list_ids:
		print(">"+str(rec.description)+"\n"+str(rec.seq))
