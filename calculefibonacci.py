def fibonacci(n):
    a, b = 0, 1
    i=2
    fib = []
    fib.append(a)
    fib.append(b)
    while i <= n+1:
        fib.append(a+b)
        a, b = b, a + b
        i=i+1
    return fib

X=input('Entrez un nombre pour calculer la suite de Fibonacci jusqu\'à ce nombre : ')
print('Suite no :', X," est : ",fibonacci(int(X)))
