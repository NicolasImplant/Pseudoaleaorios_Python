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

def square_mean(Seed):
    v1 = [] 
    v1 = numero(Seed**2,v1)
    while len(v1) % 2 != 0:
      v1.append(0)
      v1 = v1[-1::] + v1[:-1:]
    if len(v1) == 8:
       v1 = v1[2:-2]
    else:
       c = (8-len(v1))/2
       v1 = v1[int(c):int(-c)]
    x = vector(v1)
    r = x/(10**4)
    return x,r

if __name__ == '__main__':
    try:
        seed = int(input('Ingresa los cuadro digitos de la semilla:     '))
        if seed < 1006:
            raise ValueError
        N = int(input('Ingresa la cantidad de valores aleatorios:     ')) + 1
        seeds = [0 for i in range(N)]
        seeds[0] = seed
        random_numbers = [0  for i in range(N-1)]
        for i in range(N-1):
            seeds[i+1] , random_numbers[i] = square_mean(seeds[i])
            if random_numbers[i] == random_numbers[i-1]:
                break
        print(f'La semilla degeneró despues de generar {i} valores aleatorios')
        print(random_numbers)
    except ValueError:
        print("El algoritmo degenera rapidamente con esta semilla, procura un numero con todas sus cifras diferentes")