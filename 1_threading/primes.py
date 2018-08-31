#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

n = 50
primes = []
for i in range(1,n,2):
    if isprime(i):
        #print(f'{i} is prime')
        primes.append(i)

print(f'found {len(primes)} primes from 1 to {n}')

