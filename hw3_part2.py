#import statistics module to use function to solve for standard deviation
import statistics

#define functions for all equations in program: standard deviation, average, max difference, and min difference
def stddev(s):
    return statistics.stdev(s)

def average(s):
    return sum(s) / len(s)

def maxdif(a,b):
    if max(a) > max(b):
        return max(a) - max(b)
    else:
        return max(b) - max(a)

def mindif(a,b):
    if min(a) > min(b):
        return min(a) - min(b)
    else:
        return min(b) - min(a)

#identify the file and open it    
name = "data_hw_3.txt"
handle = open(name)

#create two lists that will be populated later with values from the file
inspired=list()
expired=list()

#for loop to read from each line in file and organize it
for line in handle:
    #rstrip function gets rid of the spaces
    line = line.rstrip()
    #split up into 3 strings on each line and add them to lst
    lst = line.split()
    #for loop for the 3 strings on each line
    for word in lst:
        #if it's the second string on each line, add that string to the list inspired
        if word == lst[1]:
            inspired.append(int(lst[1]))
        #if it's the last string on each line, add that string to the list expired
        if word == lst[2]:
            expired.append(int(lst[2]))

#print statements that calls the 4 define functions to solve for everything
print("Average volume of air inspired is %6.2f ml with a standard deviation of%6.2f" % (average(inspired),stddev(inspired)))
print("Average volume of air expired is %6.2f ml with a standard deviation of%6.2f" % (average(expired),stddev(expired)))
print("The maximum difference between air inspired and expired is %d" % (maxdif(inspired,expired)))
print("The minimum difference between air inspired and expired is %d" % (mindif(inspired,expired)))
   