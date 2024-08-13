

def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True

# num = 600851475143
num = 600851475143

def prime_finder(n):
    seive = [True]*(n+1)
    for i in range(1,n+1):
        if seive[i]:
            for j in range(i+i, n+1, i):
                seive[i] = False
    return seive

seive = prime_finder(num)

for i in range(num, -1, -1):
    if seive[i]:
        if num % i == 0:
            print(i)
            break
        



