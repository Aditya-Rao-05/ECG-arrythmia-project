"""
This file is to read and analyse the data within the ptb-xl dataset files.
Author: Aditya Rao
"""

analyse = open("metadata/ptbxl_database.csv", 'r') # read the file in metadata

header = analyse.readline() # read the first line
print(header)
analyse.close() # close the analysis.