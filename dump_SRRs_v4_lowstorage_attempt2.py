#!/usr/bin/python3

import subprocess

new_srr_id_list = []
with open('missing_SRRs.txt', 'r') as file1:
  data = file1.read().rstrip()
  new_srr_id_list = data.split(',')

# Use this when full storage available. Uses the subprocess module to run the command line.  Iterates over the SRR list, donwloading the sra file from NCBI.
for i in new_srr_id_list:
  subprocess.call(['/Users/dbrow208/Documents/BINF/sratoolkit.2.9.6-1-mac64/bin/prefetch', i])

# Use this while small storage available. The estimate is that roughly 4500 files will fit in 900 GB of space, based off previous runs.
#i = 0
#while i < 4500:
#  subprocess.call(['/Users/dbrow208/Documents/BINF/sratoolkit.2.9.6-1-mac64/bin/prefetch', new_srr_id_list[i]])
#  i += 1
