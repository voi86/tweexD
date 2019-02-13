def fib(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

try:
    n = int(input("Fibonacci sequence from f0 to f: "))
except:
    print("Need an integer")
else:
    if n<0:
        print("Need a non-negative integer")
    else:
        for i in range(n+1):
            print("Fibonacci number", i, "is", fib(i))