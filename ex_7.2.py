# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Cannot find that file name")

    quit()

total=0
count=0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    value=line[20:26]
    number=float(value)
    total = number + total
    count= count + 1
 
average = total / count
print("Average spam confidence: %15.12f" % (average))
