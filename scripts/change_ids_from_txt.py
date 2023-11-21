#!usr/bin/env python3
from Bio import SeqIO
import sys

args=sys.argv

fasta_1=args[1]
newids=args[2]
op_ids=open(newids, "r")
list_op_ids=list(op_ids)

list_ids=[]
for i in list_op_ids:
	list_ids+=[i.strip("\n")]

for rec, new_id in zip(SeqIO.parse(fasta_1, "fasta"), list_ids):
	print(">"+str(new_id)+"\n"+str(rec.seq))