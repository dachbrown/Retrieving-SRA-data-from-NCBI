#!/usr/bin/python3

import subprocess
import time
import sys

new_srr_id_list = []
with open('these_SRRs.txt', 'r') as file1:
  data = file1.read().rstrip()
  new_srr_id_list = data.split(',')

#print(new_srr_id_list)

# Uses the subprocess module to run the command line.  Iterates over the SRR list, dumping the .sra as only the aligned FASTA (no q) in a split and zipped format.
for i in new_srr_id_list:
#  subprocess.call(['/Users/dbrow208/Documents/BINF/sratoolkit.2.9.6-1-mac64/bin/fastq-dump', '--split-files', '--fasta', '--gzip', i])
  subprocess.call(['/Users/dbrow208/Documents/BINF/sratoolkit.2.9.6-1-mac64/bin/prefetch', i])
  sys.stdout = open('srr_dl_errors.txt', 'a')
#  outfile.close()
#  with open('srr_download_errors.txt', 'a') as outfile:
#  output_line = sys.stdout
#  outfile.write(output_line)
#  time.sleep(15)
