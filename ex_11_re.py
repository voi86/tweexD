import re

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_177104.txt"
handle = open(name)

lst=list()

for line in handle:
    line = line.rstrip()
    number=re.findall("[0-9]+", line)
    if len(number) ==0: continue
    for word in number:
        word = int(word)
        lst.append(word)
        
total=sum(lst)
print(total)
