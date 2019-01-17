# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 02:21:39 2019

@author: tweeb
"""
# variables
PV = float(input("How much is being borrowed (no commas)?"))
ra = float(input("What is the annual interest rate (enter it without the % sign)?"))
na = int(input("How many years is the loan for?"))

#conversions
r = (ra/100)/12
n = na*12

P = r*PV/(1-(1+r)**(-n))

print("Payment schedule for a loan of $%2d at %.1f" % (PV, ra) + "% interest, repaid over", int(na), "year:")
print("month", "payment", "remaining")
for m in range(1,13,1):
    RP = ((PV)*(1-((1+r)**(m-n))))/(1-((1+r)**(-n)))
    print(" %3d %7.2f %9.2f" % (m, P, RP))