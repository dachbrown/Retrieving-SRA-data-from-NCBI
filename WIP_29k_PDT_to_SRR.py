#!/usr/bin/python3
import re
import subprocess
import time

# This script should loop through the 29k PDTs provided by Colby, compare them to PDG000000004.1277.amr.metadata.tsv provided by Denis, and output the WGS accessions to be downloaded using SRA toolkit

# Opens the file of 29k PDTs and adds each to a list, removing formatting
pdt_id_list = []
with open('e.coli.ids', 'r') as file1:
  pdt_id_list = file1.read().rstrip().split(',')

# The entire metadata table
metadata = []
# Only the PDTs from the metadata table
pdt_only_metadata = []
# Opens the metadata file and populates the above variables
with open('PDG000000004.1277.amr.metadata.tsv', 'r') as file2:
  metadata = file2.readlines()
  for line in metadata:
    line = line[0:14]	# Each PDT has 14 characters
    pdt_only_metadata.append(line)

# The line number of the 29k PDTs in the metadata table is the index position
pdt_position = []
for i in pdt_id_list:
  if i in pdt_only_metadata:
    pdt_position.append(pdt_only_metadata.index(i))

# The 29k subset of the metadata
subset_metadata = []
# Compares the 29k PDTs against all the PDTs from the metadata table, writing a file containing only the 29k PDTs and all of their associated metadata
with open('all_info_29k_PDTs.tsv', 'w') as file3:
  for i in pdt_position:
    subset_metadata.append(metadata[i])
    file3.write(metadata[i])

# The 29k subset split by tab
split_subset = []
for i in subset_metadata:
  i = i.split('\t')
  split_subset.append(i)

# This is here as there some differences in the size of the data.  Some of the PDT list that Colby sent do not match any of the PDTs in the metadata table, and those PDTs that do match do NOT all seem to have SRRs.
# Possible future solution is to make the dictionary keys be Colby's list, and then populate values of 'False' for any PDT missing, but also create a section for BioProject and BioSample accession numbers, which seem to have been included in the metadata table
print(len(pdt_id_list))
print(len(pdt_only_metadata))
print(len(pdt_position))

srr_id_list = []
with open('PDT_and_SRR.tsv', 'w') as file4:
  for i in range(len(split_subset)):
    srr_id_list.append(split_subset[i][6])	# Populate the list of SRR with the SRR identifier
    file4.write(split_subset[i][0] + '\t' + split_subset[i][6] + '\n')	# The identifier containing the PDT is position 0, while the SRR is at position 6

pdt_srr_dict = dict(zip(pdt_id_list, srr_id_list))

# Next step is to access NCBI using the SRA toolkit and then batch download everything.

# Remove duplicates from the SRRs, in case there are any
srr_id_list = list(dict.fromkeys(srr_id_list))
# Sort the list
srr_id_list.sort()
# Remove any values where there is no value
srr_id_list = srr_id_list[1:]
# The below was to fix a formatting issue where there were some SRRs that were not separated.  I am unsure why they are attached, unless both SRR values refer to the same project.  I will find out more 5/30/19.
change = ','.join(srr_id_list)
new_srr_id_list = change.split(',')
#print(new_srr_id_list)
#print(len(new_srr_id_list))	# There are only about 19k genomes once the empty values are removed

# need to make a choice about wget or SRA toolkit

# Used the below to quickly dump the relevant files so I would not have to repeat the time consuming first part.
with open('these_SRRs.txt', 'w') as file5:
  file5.write(change)

#for i in new_srr_id_list:
#  subprocess.call(['/Users/dbrow208/Documents/BINF/sratoolkit.2.9.6-1-mac64/bin/fastq-dump', '--split-files', '--fasta', '--aligned', '--gzip', i])
#  time.sleep(15)

#OR

#base_url = 'ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/'
#err = 'ERR/'
#drr = 'DRR/'
#srr = 'SRR/'
#sra = '.sra'
#current_string = ''
#for i in srr_id_list:
#  if i.startswith('D'):
#    if i < 'DRR063':
#      current_string = 'wget ' + base_url + %s + %s + %s + %s + %s ] % (drr, i[:7], i, i, sra)
#      subprocess.run(['wget ' + base_url + %s + %s + %s + %s + %s ] % (drr, i[:7], i, i, sra))
#    else:
#      subprocess.run(['wget',
#  if i.startswith('E'):
#    if :
#    elif:
#    else:
#      continue
#  if i.startswith('S'):
#    if :
#    elif :
#    else:
#      continue
#  else:
#    continue
