# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 02:21:39 2019

@author: tweeb
"""
# variables #the try except loop wont work.
ra = float(input("What is the annual interest rate (enter it without the % sign)? "))
try: 
    r = float(ra)
except:
    print("Uh-oh! Please enter a real number between 0 to 100.")
r = (r/100)/12
print(r)

PV = input("How much is being borrowed (no commas)? ")
try:
    float(PV)
except:
    print("Uh-oh! Please enter a real number.")
    
na = int(input("How many years is the loan for? "))
try:
    int(na)
except:
    print("Uh-oh! Please enter a real number.")
n = na*12

# table headers
print("Payment schedule for a loan of $%2d at %.1f" % (PV, ra) + "% interest, repaid over", int(n), "year:")
print("month", "payment", "remaining")

for m in range(1,13,1): # generates sequence of numbers for each of the 12 months
    P = r*PV/(1-(1+r)**(-n)) # P is payment per month needed to pay off loan in 1 year
    RP = ((PV)*(1-((1+r)**(m-n))))/(1-((1+r)**(-n))) # RP is reamaining principal
    print(" %3d %7.2f %9.2f" % (m, P, RP)) # print statement for all 3 components