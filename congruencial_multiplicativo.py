def multiplicativo(a,x,m):
    x1 = (a*x) % m
    x2 = x1 / (m-1)
    return x1, x2

if __name__ == '__main__':
    try:
        seed = int(input('Digita el valor de la semilla:   '))    
        k = int(input('Digita el valor de la constante de k:   '))
        g = int(input('Digita el valor de la constante de g:   '))
        if seed < 10 or k < 10 or g < 10:
            raise ValueError  
        N = int(input('Digita la cantidad de números aleatorios requerida:  ')) + 1
        a = 5 + 8*k
        m = 2**g

        x = [0 for i in range(N)]
        r = [0 for i in range(N)]
        x[0] = seed

        for i in range(N-1):
            x[i+1], r[i] = multiplicativo(a,x[i],m)
        print(r)

    except ValueError:
        print('Para un ciclo de vida máximo, los valores de las constantes y la semilla deben ser mayores a 10')










  