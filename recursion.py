def fact(n):
    if n < 2:
        return 1
    return n * fact(n-1)

def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)


print(fact(4))
print(fib(4))