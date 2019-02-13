fibdict = {}

def fib(n):
    global fibdict
    if n in fibdict:
        return fibdict[n]
    
    if n ==0:
        fibdict[0] = 0
        return 0 
    elif n == 1:
        fibdict[1] = 1
        return 1
    fibdict[n] = fib(n-1) + fib(n-2)
    return fibdict[n]

def main():
    count = 35
    for i in range(count-2):
        print("Fibonacci number", i+1, "is", fib(i))

main()