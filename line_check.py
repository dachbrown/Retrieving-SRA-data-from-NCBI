#!/usr/bin/python3

data = ''
data_list = []

# verifies the line number of the file
with open('these_SRRs.txt', 'r') as file1:
  data = file1.read()

data_list = data.split(',')

print(data_list[4498], data_list[4499], data_list[4500], data_list[4501])
