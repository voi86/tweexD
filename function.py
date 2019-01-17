def math1(a,b,c):
    pay = (a*b) / (1-((1+a)**(-c)))
    return pay

def math2(a,b,c,d):
    remain = (b*(1-(1+a)**(d-c))) / (1-(1+a)**(-c))
    return remain

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
    P=math1(r,PV,n)
    RP=math2(r,PV,n,m)
    print(" %3d   %7.2f  %9.2f" % (m,P,RP))
    x= x+1
    
    