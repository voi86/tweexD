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

games = input("Number of games to play: ")
try:
    int(games)
except:
    print("Please enter a positive integer")
    quit()

gamesplayed = int(games)
g= gamesplayed - 1

countalways = 0
countnever = 0

for i in range(0,g,1):
    prize=rng(1,3)
    selection=rng(1,3)
    win = montyalways()
    if win==True:
        countalways = countalways + 1   

for i in range(0,g,1):
    prize=rng(1,3)
    selection=rng(1,3)
    win = montynever()
    if win==True:
        countnever = countnever + 1

percentagealways= countalways / gamesplayed
percentagenever = countnever / gamesplayed

print("Out of %d games: " % (gamesplayed))
print("Always switching wins: %9.7f (%d games) " % (percentagealways, gamesplayed))
print("Never switching wins: %9.7f (%d games) " % (percentagenever, gamesplayed))
    





