def numero(x,n):
    num1 = x % 10
    num2 = x // 10
    n.append(num1)
    if num2 != 0:
        return numero(num2,n)
    else:
        return n[::-1]

def vector(v):
    if sum(v) < 1:
        return False 
    return v[0]*1000 + v[1]*100 + v[2]*10 + v[3]*1

def product_mean(Seed1,Seed2):
    v1 = [] 
    v1 = numero(Seed1*Seed2,v1)
    while len(v1) % 2 != 0:
      v1.append(0)
      v1 = v1[-1::] + v1[:-1:]
    if len(v1) == 8:
       v1 = v1[2:-2]
    else:
       add = 8-len(v1)
       c = add/2
       v1 = v1[int(c):int(-c)]
    x = vector(v1)
    r = x/(10**4)
    return x,r

if __name__ == '__main__':
    try:
        seed1 = int(input('Ingresa el valor de la primera semilla:     '))
        seed2 = int(input('Ingresa el valor de la segunda semilla:     '))
        if seed1 < 1005 and seed2 < 1005:
            raise ValueError 
        N = int(input('Ingresa la cantidad de valores aleatorios:     ')) + 2
        seeds = [0 for i in range(N)]    
        seeds[0] = seed1
        seeds[1] = seed2
        random_numbers = [0 for i in range(N-1)]
    
        for i in range(1,N-1):
            seeds[i+1] , random_numbers[i] = product_mean(seeds[i],seeds[i-1])
        random_numbers.pop(0)
        print(random_numbers)
    except ValueError:
        print('Al menos una de las dos semillas debe tener sus cuatro digitos diferentes')
