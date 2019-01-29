name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts=dict()
time=list()

for line in handle:
    if not line.startswith("From "): continue
    line=line.rstrip()
    lst=line.split()
    for word in lst:
        if word == lst[5]:
            hour = word.split(':')
            time.append(hour[0])
            

            
for each in time:
    counts[each]=counts.get(each,0)+1


for k,v in sorted(counts.items()):
    print(k,v)    
   


