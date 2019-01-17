PV=5000
r=0.065/12
t=r*1200
n=12
m=0
P=0
RP=0
print("Payment schedule for a loan of $%8.2f at%4.1f interest, repaid over 1 year:" % (PV, t))
print("month  payment  remaining")

x=1
while x<13:
    m=x
    P = (r*PV) / (1-((1+r)**(-n)))
    RP = (PV*(1-(1+r)**(m-n))) / (1-(1+r)**(-n))
    print(" %3d   %7.2f  %9.2f" % (m,P,RP))
    x= x+1
    
    