def fibo_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursion(n-2) + fibo_recursion(n-1)



