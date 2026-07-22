from sympy import isprime, totient

n = 6_148_888_817
steps = 0

while not isprime(n):
    n = int(totient(n)) + 1
    steps += 1

print(steps, n)
