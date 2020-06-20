# Title: TCX to CSV formatter 
# Description: Fitness trackers commonly use TCX.  Here we are just abstracting the time and Heart Rate data
# Author: Kenny Sexton
# Date: May 2020

import sys
from xml.dom import minidom

# Default input file if argument is not specified
inputFileName = 'input.tcx'

# Check if filename is given via command line
if(len(sys.argv) != 2):
    print("Usage: python tcxToCSV.py {filename}")
else:
    inputFileName = sys.argv[1];

xmldoc = minidom.parse(inputFileName)

# Get lists of relevant Data
timeElementList = xmldoc.getElementsByTagName('Time')
hrElementList = xmldoc.getElementsByTagName('Value')

print("Number of Time Elements: ", len(timeElementList))
print("Number of HR Elements: ", len(hrElementList))

# Check that these two numbers match
if(len(timeElementList) != len(hrElementList)):
    print("WARNING: The number of time elements does not match the number of heart rate elements")

# Remove tcs file extension
baseFileName = inputFileName.split('.tcx', 1)[0] 

# Open an output file for printing
fp = open('outputs/' + baseFileName + '.csv', 'w')
  
#print('test', file = fp) 

#print(timeElementList[0].firstChild.nodeValue)
for (i, j) in zip(timeElementList, hrElementList):
    print(i.firstChild.nodeValue + "," + j.firstChild.nodeValue, file = fp)

fp.close() 