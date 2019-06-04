#!/usr/bin/python3

# Use this script to check the directory to see if all SRRs were downloaded

# Import packages to create a list of files in the designated directory
from os import listdir
from os.path import isfile, join

# Instantiate variables
data = ''
data_list = []
all_files_list = []
present_files = []
missing_files_list = []
missing_SRRs_list = []
missing_SRRs_string = ''

# The pathway of the directory where the files are downloaded
download_path = '/Users/dbrow208/Documents/BINF/ncbi/public/sra'

# Open the file with the SRRs and read the data into memory
with open('these_SRRs.txt', 'r') as file1:
  data = file1.read().rstrip('\n')

# Make a list from the input data
data_list = data.split(',')

# Shorten the data due to the smaller memory on this local machine, the value should match that of the while loop inn dump_SRRs_v3_lowstorage.py
data_list = data_list[:4500]

# Change the data list into actual file names to check against those found in the directory
for i in data_list:
  all_files_list.append(i + '.sra')

# Create a list of all current files in the directory
present_files = [f for f in listdir(download_path) if isfile(join(download_path, f))]

# Compare the files that should be in the directory to those that are actually in the directory
for i in all_files_list:
  if i not in present_files:
    missing_files_list.append(i)

# Remove the extension from the file names
missing_SRRs_list = [i.strip('.sra') for i in missing_files_list]

print(len(missing_SRRs_list))
# Convert back to a string to work with the dump_SRRs.py scripts
missing_SRRs_string = ','.join(missing_SRRs_list)

# Write the output file of SRRs to be checked and/or attempt to download them again
with open('missing_SRRs.txt', 'w') as file2:
  file2.write(missing_SRRs_string)
