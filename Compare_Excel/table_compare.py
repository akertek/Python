#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:07:16 2020

@author: egeakertek


"""
import argparse 
import pandas as pd
import datacompy
from io import StringIO

def terminal_parser():
    parser = argparse.ArgumentParser(description='Compare two tables.')
    
    parser.add_argument("-file1", type = str)
    parser.add_argument("-file2", type = str)
    parser.add_argument("-sheet1",type = int, nargs="?", default= 0)
    parser.add_argument("-sheet2",type = int, nargs="?", default= 0)
    
    args = parser.parse_args()
    
    file1 = args.file1
    file2 = args.file2
    sheet1 = args.sheet1
    sheet2 = args.sheet2
    

    return file1, file2, sheet1, sheet2

def excel_difference(file1, file2, sheet1, sheet2):
    pass
    
    

def main():
  
    file1, file2, sheet1, sheet2 = terminal_parser()

    table1 = pd.read_excel(file1, sheet1, header = None)
    table2 = pd.read_excel(file2, sheet2, header = None)
            
    

    
    new_dataframe = pd.DataFrame()
                        
    for row1 in table1.itertuples(index = False):
        for row2 in table2.itertuples(index = False):
            row_add = []
            for value in range(0, (max(len(row1),len(row2)))):
                try:
                    if row1[value] == row2[value]:
                        row_add.append(row1[value])
                        print(True)
                    else:
                        row_add.append(row1[value] + "/" + row2[value])
                        print(False)
                except IndexError:
                    try:
                        row_add.append("/" + row1[value])
                        print("1 de buldum")
                    except IndexError:
                        row_add.append("/" + row2[value])
                        print("2 DE BULDUM")
            
            sr_row_add = pd.Series(row_add)
            new_dataframe = new_dataframe.append(sr_row_add,ignore_index = True)
        break
        
if __name__ == "__main__":
    
    main()



