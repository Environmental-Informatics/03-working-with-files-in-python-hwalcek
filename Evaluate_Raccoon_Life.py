#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Due February 7, 2020
Created on Wed Feb  5 12:54:57 2020
by Hannah Walcek
Assignment 03 - Using Files and Simple Data Structures with Python

This program reads the file 2008Male00006.txt, does various calculations, and
outputs the file Georges_life.txt
"""

##Part 1: open data file
file = open("2008Male00006.txt","r")

##Part 2: store data from the file in a dictionary
lines = file.readlines()

#create list of lines from file and remove end of line character and split by ,
for i in range(len(lines)):
    lines[i] = lines[i].rstrip().split(',')

#create blank dictionary
dictionary = {}

#create list, key
key = lines[0]

#fill dictionary with blank lists
for j in range(len(lines[0])):
    dictionary[key[j]] = []  
    
#append lists in dictionary with input from text file
for i in range(1,len(lines)-1):
    for j in range(len(lines[0])):
        dictionary[key[j]].append(lines[i][j])
        
dictionary.update({'End State': lines[len(lines)-1]})

#close file
file.close()
        
##Part 3: convert columns of numbers into lists of the correct number type
for i in range(0, len(dictionary[' X'])):
    dictionary[' X'][i] = float(dictionary[' X'][i])
for i in range(0, len(dictionary[' Y'])):
    dictionary[' Y'][i] = float(dictionary[' Y'][i])
for i in range(0, len(dictionary['Energy Level'])):
    dictionary['Energy Level'][i] = float(dictionary['Energy Level'][i])
for i in range(0, len(dictionary['MSL'])):
    dictionary['MSL'][i] = float(dictionary['MSL'][i])
for i in range(0, len(dictionary['MVL'])):
    dictionary['MVL'][i] = float(dictionary['MVL'][i])  
for i in range(0, len(dictionary['Percent Step'])):
    dictionary['Percent Step'][i] = float(dictionary['Percent Step'][i]) 
for i in range(0, len(dictionary['PercptionDist'])):
    dictionary['PercptionDist'][i] = float(dictionary['PercptionDist'][i])
for i in range(0, len(dictionary['ProbFoodCap'])):
    dictionary['ProbFoodCap'][i] = float(dictionary['ProbFoodCap'][i])
for i in range(0, len(dictionary['Risk'])):
    dictionary['Risk'][i] = float(dictionary['Risk'][i])
    
##Part 4: write functions
def list_sum(lst):
    """Function that returns the cumulative sum of a list, lst
    """
    total = 0
    for ele in range(0, len(lst)):
            total = total + lst[ele]
    return total

def list_mean(lst):
    """Function that returns the mean of a list, lst
    """
    return list_sum(lst) / len(lst)

def distance(x, y):
    """Function that returns a list of the distance between points from two 
    lists, x and y
    """
    dist = []
    for i in range(0, len(x)):
        dist.append(abs(x[i]-y[i]))
    return dist

##Part 5: use functions to create new keys and values in dictionary
dictionary.update({'Movement':
    distance(dictionary[' X'], dictionary[' Y'])})
dictionary.update({'Avg Energy Level':
    list_mean(dictionary['Energy Level'])})
dictionary.update({'Avg X':
    list_mean(dictionary[' X'])})
dictionary.update({'Avg Y':
    list_mean(dictionary[' Y'])})
dictionary.update({'Total Dist Moved': 
    list_sum(distance(dictionary[' X'], dictionary[' Y']))})
    
##Part 6: create output file Georges_life.txt
output = open("Georges_life.txt", "w")
    
#create string variables
raccoon_name = "Raccoon name: George #" + str(dictionary['George #'][0])
avg_location = "Average location: " + str(dictionary['Avg X']) + ", " \
+ str(dictionary['Avg Y'])
distance_traveled = "Distance traveled: " + str(dictionary['Total Dist Moved'])
avg_energy = "Average energy level: " + str(dictionary['Avg Energy Level'])
raccoon_end = "Raccoon end state: " + str(dictionary['End State'][0])

#write string variables into output
output.writelines(raccoon_name + '\n')
output.writelines(avg_location + '\n')
output.writelines(distance_traveled + '\n')
output.writelines(avg_energy + '\n')
output.writelines(raccoon_end + '\n')

output.writelines('\n')

#write in headings from dictionary
output.write("Date" + '\t' + "Time" + '\t' + "X" + '\t' + "Y" 
             + '\t' + "Asleep Flag" + '\t' + "Behavior Mode" 
             + '\t' "Distance Traveled" + '\n')

#write in values with corresponding headings
for i in range(1, len(dictionary[' X'])):
    output.write(str(dictionary['Day'][i]) + '\t' + str(dictionary['Time'][i]) 
    + '\t' + str(dictionary[' X'][i]) + '\t' + str(dictionary[' Y'][i]) + '\t' 
    + str(dictionary[' Asleep'][i]) + '\t' 
    + str(dictionary['Behavior Mode'][i]) + '\t' 
    + str(dictionary['Movement'][i]) + '\n')

#close output
output.close()

