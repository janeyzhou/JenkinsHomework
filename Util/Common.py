import csv
import os


def readCSV(file_path):
    search_list = []
    with open(file_path, 'r') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            search_list.append(row)
        f.close()
    return search_list

