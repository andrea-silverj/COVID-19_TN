#!usr/bin/env python3
from Bio import SeqIO
from ete3 import Tree
import csv
import sys
import re
args=sys.argv

treefile=args[1]
gisaid_metadata=args[2]

tree = Tree(treefile)

gisaid_metadata_list=[]
with open(gisaid_metadata,'r') as f:
	next(f) #skip heading row in text file
	tab_metadata = csv.reader(f,delimiter='\t') #read text file with csv
	for row in tab_metadata:
		gisaid_metadata_list.append(row) #add the data from the text file to the list

record_ids=[]
record_date=[]
record_country=[]
record_place=[]
record_nextstrain=[]
record_pangolin=[]
for record in gisaid_metadata_list:
	record_ids+=[record[2]]
	record_date+=[record[4]]
	record_country+=[record[6]]
	record_place+=[record[7]]
	record_nextstrain+=[record[17]]
	record_pangolin+=[record[18]]

record_date_beast=[]
for date in record_date:
	record_date_beast+=[date.replace("-", "/").replace("/XX/","/06/").replace("/XX","/15")]

##################Play with this if you want to format incomplete dates##################
	#if re.match(r'(\d+)', date) == True:
	#	record_date_beast+=[date.replace("-", "/")+"/06/15"]	
	#elif re.match(r'(\d+-\d+)', date) == True:
	#	record_date_beast+=[date.replace("-", "/").replace("/XX","/06")+"/15"]
	#elif re.match(r'(\d+-\d+-\d+)', date) == True:		
		
record_country_nospace=[]
for country in record_country:
	record_country_nospace+=[re.sub("[^a-zA-Z_]", "", country.replace(" ","_"))]

record_place_nospace=[]
for place in record_place:
	record_place_nospace+=[re.sub("[^a-zA-Z_]", "", place.replace(" ","_"))]


information_meta=[m+"|"+str(n)+"|"+str(o)+"|"+str(p)+"|"+str(q)+"@"+str(r) for m,n,o,p,q,r in zip(record_ids,record_place_nospace,record_country_nospace,record_nextstrain,record_pangolin,record_date_beast)]

metadata_dict=dict(zip(record_ids,information_meta))


for leaf in tree.iter_leaves():
	if leaf.name in metadata_dict.keys():
		leaf.name=metadata_dict[leaf.name]

	elif re.search("EPI_ISL_", leaf.name) is not None and leaf.name not in metadata_dict.keys():
		leaf.name=leaf.name+"|no_metadata"

	else:
		leaf.name=((("FEM_TN|"+re.sub("-", "/",leaf.name.replace("/","|"))).replace("|20","@20").replace("/1/","/01/").replace("/2/","/02/").replace("/3/","/03/").replace("/4/","/04/").replace("/5/","/05/").replace("/6/","/06/").replace("/7/","/07/").replace("/8/","/08/").replace("/9/","/09/")).replace("/1","/01").replace("/2","/02").replace("/3","/03").replace("/4","/04").replace("/5","/05").replace("/6","/06").replace("/7","/07").replace("/8","/08").replace("/9","/09")).replace("/010","/10").replace("/011","/11").replace("/012","/12").replace("/013","/13").replace("/014","/14").replace("/015","/15").replace("/016","/16").replace("/017","/17").replace("/018","/18").replace("/019","/19").replace("/020","/20").replace("/021","/21").replace("/022","/22").replace("/023","/23").replace("/024","/24").replace("/025","/25").replace("/026","/26").replace("/027","/27").replace("/028","/28").replace("/029","/29").replace("/030","/30").replace("/031","/31")


tree.write(format=0,outfile="allgisaid_alltn.tre")