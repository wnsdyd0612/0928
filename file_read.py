import sys

input_file = "sample.txt"
filereader = open(input_file, 'r')

for row in filereader:
     print(row.strip())

filereader.close()
