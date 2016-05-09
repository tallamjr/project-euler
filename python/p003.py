# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def factors(n):
    return [i for i in range(1, n + 1) if not n%i]

print factors(60)
