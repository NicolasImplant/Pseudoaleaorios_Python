from functions import constantMultiplier, primeNumber

def pseudoRandNumbers(seeds:list, random_numbers:list):
    for i in range(1,N-1):
        seeds[i+1] , random_numbers[i] = constantMultiplier(seeds[i],seeds[i-1])
    return random_numbers

if __name__ == '__main__':
    seed1 = primeNumber()
    seed2 = primeNumber()
    N = int(input('Ingresa la cantidad de valores aleatorios:     ')) + 2
    seeds = [0 for i in range(N)]    
    seeds[0] = seed1
    seeds[1] = seed2
    random_numbers = [0 for i in range(N-1)]
    print(pseudoRandNumbers(seeds, random_numbers))