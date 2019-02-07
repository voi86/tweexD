import random
def rng(a,b):
    ran = random.randint(a,b)
    return ran

def montyalways():
    if selection == prize:
        return False
    else:
        return True

def montynever():
    if selection == prize:
        return True
    else: 
        return False

prize=rng(1,3)
selection=rng(1,3)
montynever()
