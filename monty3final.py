# -*- coding: utf-8 -*-
"""
Created on Thu Feb 1 09:10:40 2019

"""
# Thuy Le - MHI 289I - Homework 2 - Part 1

import random

def montyalways():
    prize = random.randint(1,3)
    select = random.randint(1,3)
    if select == prize:
        return False
    else:
        return True

def montynever():
    prize = random.randint(1,3)
    select = random.randint(1,3)
    if select == prize:
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
g= gamesplayed + 1
    
countalways = 0
countnever = 0

for i in range(0,g,1):
    if montyalways() == True:
        countalways = countalways + 1

for i in range(0,g,1):
    if montynever() == True:
        countnever = countnever + 1

peralways = countalways / gamesplayed
pernever = countnever / gamesplayed


print("Out of %d games: " % (gamesplayed))
print("Always switching wins: %9.7f (%d games) " % (peralways, countalways))
print("Never switching wins: %9.7f (%d games) " % (pernever, countnever))

        