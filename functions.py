import random as rd

def numero(x:int,n:list=[]) -> list:
    num1 = x % 10
    num2 = x // 10
    n.append(num1)
    if num2 != 0:
        return numero(num2,n)
    else:
        return n[::-1]

def vector(v:list) -> int:
    if sum(v) < 1:
        return 0
    return v[0]*1000 + v[1]*100 + v[2]*10 + v[3]*1

def square_mean(Seed:int, v:list=[], random:dict={}) -> list:
    try:
        return random[Seed]
    except KeyError:
        w = []
        v = numero(Seed**2,w)
        while len(v) % 2 != 0:
            v.append(0)
            v = v[-1::] + v[:-1:]
        if len(v) == 8:        
            v = v[2:-2]
        else:
            v = v[int((8-len(v))/2):int(-(8-len(v))/2)]
    random[Seed] = [vector(v),vector(v)/(10**4)]        
    return random[Seed]

def primeNumber(primes:list=[]):
    x = {n:[i for i in range(1,n+1) if n % i == 0] for n in range(2000,6000)}
    for key, value in x.items():
        if len(value) == 2:
            primes.append(key)
    return primes[rd.randint(0,len(primes))]