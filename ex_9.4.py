name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

names=dict()

for line in handle:
    if not line.startswith("From:"): continue
    line = line.rstrip()
    word= line.split()
    addy=word[1]
    names[addy] = names.get(addy,0)+1
    
largest=-1
theword=None

for a,b in names.items():
    if b>largest:
        largest = b
        theword = a

print(theword,largest)

