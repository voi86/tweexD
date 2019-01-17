v=input("What is the annual interest rate (enter it without the % sign)?")
try:
    float(v)
except:
    print("Enter a number")
r=float(v)/1200

pPV=input("How much is being borrowed (no commas)?")
PV=int(pPV)

z=input("How many years is the loan for?")
n=int(z)*12

m=0
P=0
RP=0
print("Payment schedule for a loan of $%8.2f at%4.1f interest, repaid over 1 year:" % (PV, float(v)))
print("month  payment  remaining")

x=1
while x<13:
    m=x
    P = (r*PV) / (1-((1+r)**(-n)))
    RP = (PV*(1-(1+r)**(m-n))) / (1-(1+r)**(-n))
    print(" %3d   %7.2f  %9.2f" % (m,P,RP))
    x= x+1
    
    