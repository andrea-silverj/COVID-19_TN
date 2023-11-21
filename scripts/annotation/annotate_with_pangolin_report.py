#!usr/bin/env python3
from Bio import SeqIO
import csv
import sys
import re
args=sys.argv

fasta_file=args[1]
pangolin_metadata=args[2]

pangolin_metadata_list=[]
with open(pangolin_metadata,'r') as f:
	next(f) #skip heading row in text file
	tab_metadata = csv.reader(f,delimiter=',') #read text file with csv
	for row in tab_metadata:
		pangolin_metadata_list.append(row) #add the data from the text file to the list

record_ids=[]
record_pangolin=[]

for record in pangolin_metadata_list:
	record_ids+=[record[0]]
	record_pangolin+=[record[1]]		

pangolin_dict=dict(zip(record_ids,record_pangolin))


for rec in SeqIO.parse(fasta_file, "fasta"):
	for pango_lineage in record_pangolin:
		print(">"+rec.id+"\n"+str(rec.seq))


print(record_ids, record_pangolin)