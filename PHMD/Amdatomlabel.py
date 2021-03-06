# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 14:17:46 2018

@author: Peter
"""

import glob

# To be used in post parametrised data, in the same folder as in files.

# Scan for all .data files in the directory
datas = glob.glob("*.data")

# For each .data file
for data in datas:
    hype = open(data, 'r')
    hype2 = hype.readlines()
    hype.close()

    # A counter for each element
    Cs = 0
    Fs = 0
    Hs = 0
    Ns = 0
    Ps = 0
    line = "dump_modify d1  element "

    #Search for Pair coeffs, which lists atoms
    for i in range(len(hype2)):
        if 'Pair Coeffs' in hype2[i]:
            start = i + 2
        if 'Bond Coeffs' in hype2[i]:
            end = i - 1

    # Count for each element
    for j in range(start,end):
        spl = hype2[j].split()
        if "C" in spl[-1]:
            Cs +=1
        if "F" in spl[-1]:
            Fs +=1
        if "H" in spl[-1]:
            Hs +=1
        if "N" in spl[-1]:
            Ns +=1
        if "P" in spl[-1]:
            Ps +=1

    # Add each element in alphabetical order
    for i in range(Cs):
        line += "C "
    for i in range(Fs):
        line += "F "
    for i in range(Hs):
        line += "H "
    for i in range(Ns):
        line += "N "
    for i in range(Ps):
        line += "P "
    line += " \n"

    #Open the input file
    hype = open(data[:-5] + ".in","r")
    hype2 = hype.readlines()
    hype.close()

    #Search for the existing dump_modify line
    for i in range(len(hype2)):
        if "dump_modify d1  element " in hype2[i]:
            hype2[i] = line

    #Replace the dump_modify line with the correct list of atoms
    output = open(data[:-5] + ".in", "w")
    for i in hype2:
        output.write(i)
    output.close()
