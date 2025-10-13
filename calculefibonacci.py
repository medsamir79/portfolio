def fibonacci(n):
    a, b = 0, 1
    resultats = []
    while a < n:
        resultats.append(a)
        a, b = b, a + b
    return resultats

# Exemple d'utilisation
for x in range(10)
print('Suite no :', x+1," est : ",fibonacci(x))
