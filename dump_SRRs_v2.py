#!/usr/bin/python3

import subprocess

new_srr_id_list = []
with open('these_SRRs.txt', 'r') as file1:
  data = file1.read().rstrip()
  new_srr_id_list = data.split(',')

# Uses the subprocess module to run the command line.  Iterates over the SRR list, donwloading the sra file from NCBI.
for i in new_srr_id_list:
  subprocess.call(['prefetch', i])
