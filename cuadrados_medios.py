from functions import square_mean, primeNumber

def Pseudorandom_numbers(seeds:list,randoms:list,N:int) ->list:
    for i in range(N-1):
        seeds[i+1], randoms[i] = square_mean(seeds[i])
    return randoms

if __name__ == '__main__':

    N = int(input('Enter how many random numbers do you require:     '))
    seeds = [0 for i in range(N)]
    random_numbers = [0 for i in range(N-1)]
    seeds[0] = primeNumber()

    print(Pseudorandom_numbers(seeds,random_numbers,N))    