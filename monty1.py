import random
def rng(a,b):
    ran = random.randint(a,b)
    return ran

x=0
while x<50:
    a=rng(1,3)
    print(a, end="")
    x=x+1
