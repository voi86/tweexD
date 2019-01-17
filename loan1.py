# variables
PV = 5000
ra = 6.5
r = 0.065/12
n = 12

P = r*PV/(1-(1+r)**(-n))

print("Payment schedule for a loan of $%2d at %.1f" % (PV, ra) + "% interest, repaid over", int(n), "year:")
print("month", "payment", "remaining")
for m in range(1,13,1):
    RP = ((PV)*(1-((1+r)**(m-n))))/(1-((1+r)**(-n)))
    print(" %3d %7.2f %9.2f" % (m, P, RP)) 
