#import statistics module to use function to solve for standard deviation
import statistics

#define functions for all equations in program: standard deviation, average, max difference, and min difference
def stddev(s):
    return statistics.stdev(s)

def average(s):
    return sum(s) / len(s)

#identify the file and open it    
name = "data_hw_3.txt"
handle = open(name)

#create two lists that will be populated later with values from the file
inspired=list()
expired=list()
diff=list()

#for loop to read from each line in file and organize it
for line in handle:
    #rstrip function gets rid of the spaces
    line = line.rstrip()
    #split up into 3 strings on each line and add them to lst
    lst = line.split()
    #for loop for the 3 strings on each line
    for word in lst:
        #for each line, add the second string to one list and the third string to another list
        if word == lst[0]:
            inspired.append(int(lst[1]))
            expired.append(int(lst[2]))
            #subtract column 2 from column 3 for each line, take absolute value of it, then add to list diff
            diff.append(abs(int(lst[1])-int(lst[2])))
        
#print statements that calls the 4 define functions to solve for everything
print("Average volume of air inspired is %6.2f ml with a standard deviation of%6.2f" % (average(inspired),stddev(inspired)))
print("Average volume of air expired is %6.2f ml with a standard deviation of%6.2f" % (average(expired),stddev(expired)))
print("The maximum difference between air inspired and expired is %d" % (max(diff)))
print("The minimum difference between air inspired and expired is %d" % (min(diff)))
   