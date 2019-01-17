def math1(a,b,c):
    pay = (a*b) / (1-((1+a)**(-c)))
    return pay

def math2(a,b,c,d):
    remain = (b*(1-(1+a)**(d-c))) / (1-(1+a)**(-c))
    return remain

def principle(a,b):
    prin= (a-b)
    return prin

def interest(a,b,c):
    intleft= (a)*(b)*((1/c))
    return intleft

def totalint(a,b):
    totint= (a+b)
    return totint

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

b=float(v)/100
VX=0
m=0
P=0
RP=0
IR=0
PP=0
TI=0
print("Payment schedule for a loan of $%8.2f at%4.1f interest, repaid over 1 year:" % (PV, float(v)))
print("month  payment  principle  interest  total int  remaining")

x=1
while x<13:
    m=x
    P=math1(r,PV,n)
    RP=math2(r,PV,n,m)
    if x==1:
        VX=PV
    IR=interest(VX,b,n)
    RP=math2(r,PV,n,m)
    VX=RP
    PP=principle(P,IR)
    TI=totalint(IR,TI)
    print(" %3d   %7.2f   %7.2f    %6.2f     %6.2f   %9.2f" % (m,P,PP,IR,TI,RP))
    x= x+1
    
    