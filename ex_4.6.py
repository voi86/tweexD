def computepay(h,r):
    if h>40:
        otp = (40*r) + ((h-40)*(r*1.5))
        return otp
    else :
        pay=h*r
        return pay
hrs= input("Enter Hours: ")
rph= input("Enter Rate per hour: ")
hr= float(hrs)
rp= float(rph)

p= computepay(hr,rp)
print("Pay= ", p)