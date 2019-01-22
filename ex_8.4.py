fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    sp= line.split()
    for i in sp:
        if i not in lst:
            lst.append(i)

lst.sort()
print(lst)
