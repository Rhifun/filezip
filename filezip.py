#   Max Hampton
#  ​CSCI 101 – Section E
#   Create Project
#   References: None
#   Time: 120 minutes
import sys
import csv
def compress(filename):
    if(filename[-7:] == ".maxzip"):
        return False
    file = open(filename, "r")
    newfile = open((filename[:-4]+".maxzip"),"x")
    for line in file:
        line = line.replace(" the ", "%^")
        line = line.replace(" to ", "*#")
        line = line.replace(" a ", "&%")
        line = line.replace(" I ", "%@")
        line = line.replace(" had ", "&(")
        newfile.write(line)
    return True
def decompress(filename):
    if(filename[-4:] == ".txt"):
        return False
    file = open(filename, "r")
    newfile = open((filename[:-7]+".txt"),"x")
    for line in file:
        line = line.replace("%^", " the ")
        line = line.replace("*#", " to ")
        line = line.replace("&%", " a ")
        line = line.replace("%@", " I ")
        line = line.replace("&(", " had ")
        newfile.write(line)
    return True
print("Welcome to Max's File Compressor! Enter 0 if you want to compress, 1 if you want to extract.")
x = int(input("1/0 - "))
if(not(x == 1 or x == 0)):
    print("Please enter only a 1 or a 0")
    exit()
print("Now, please enter a txt file if you're compressing, or a .maxzip if you're extracting.")
name = input("Filename - ")
if(not(name[-4:] == ".txt" or name[-7:] == ".maxzip")):
    print("I'm sorry! This program only compresses .txt and .maxzip files currently")
    exit()
err = False
if(x == 0):
    err = compress(name)
elif(x == 1):
    err = decompress(name)
if(x == 0 and err):
    print("Your file has been compressed! Check the folder for your new .maxzip file.")
elif(x == 1 and err):
    print("Your file has been decompressed! Check the folder for your new .txt file.")
else:
    print("There's been an error. Check to make sure you're performing the right functions on the file (compressing a txt, decompressing a .maxzip)")
