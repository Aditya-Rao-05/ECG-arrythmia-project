"""
This file is to read and analyse the data within the ptb-xl dataset files.
Author: Aditya Rao
"""

analyse = open("metadata/ptbxl_database.csv", 'r') # read the file in metadata

while True:
    line = analyse.readline()
    if line == "":
        break
    print(line)

analyse.close()