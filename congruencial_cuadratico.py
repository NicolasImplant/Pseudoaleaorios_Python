def multiplicativo(x,a,b,c,m):
    x1 = ((a*x**2) + (b*x) + c) % m
    x2 = x1 / (m-1)
    return x1, x2

if __name__ == '__main__':
    try:
        seed = int(input('Digita el valor de la semilla:   '))    
        a = int(input('Digita el valor de la constante de a:   '))
        b = int(input('Digita el valor de la constante de b:   '))
        c = int(input('Digita el valor de la constante de c:   '))
        if a == 1 and b == 0 and c == 0:
            raise ValueError  
        g = int(input('Digita el valor de la constante de g (m = 2^g) :   '))
        N = int(input('Digita la cantidad de números aleatorios requerida:  ')) + 1        
        m = 2**g        

        x = [0 for i in range(N)]
        r = [0 for i in range(N)]
        x[0] = seed

        for i in range(N-1):
            x[i+1], r[i] = multiplicativo(x[i],a,b,c,m)
        print(r)

    except ValueError:
        print('Para a = 1, b = 0, y c = 0; aplicar el agoritmo Blum, Blum y Shub')