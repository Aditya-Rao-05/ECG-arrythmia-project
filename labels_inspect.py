"""
File Name: labels_inspect.py
This file is to read and analyse the data within the ptb-xl dataset files.
Author: Aditya Rao
"""


import csv
import ast


analyse = open("metadata/ptbxl_database.csv", 'r') # this opens and reads the file
rows = csv.DictReader(analyse) # this extracts the rows

code_counts = {}
for r in rows:
    codes = ast.literal_eval(r["scp_codes"])
    for code in codes:
        if code in code_counts: # if key already in the dictionary then increment
            code_counts[code] += 1 # add the code into dict as key
        else:              # if key not in dict then start it off with one count
            code_counts[code] = 1

# sort by descending order where lambda retrieves for ordering purposes from tuples.
print(sorted(code_counts.items(), key=lambda item:item[1], reverse=True))






analyse.close()




