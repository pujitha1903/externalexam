n=5
def fact(n):
    if(n==0):
        return 1
    else:
        return n * fact(n-1)
print("factorial is",factorial(n))

