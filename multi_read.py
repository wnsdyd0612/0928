import sys
from glob import glob
import os

for input_file in glob(os.path.join(".",'*.txt')):
    with open(input_file,'r') as filereader:
        print("=====")
        for row in filereader:
            print("{}".format(row.strip()))

     filereader.close()
