#suma superior e inferior de la matriz

def adelante(matriz):
    for i in range(len(matriz)):
        h=matriz[0][i]-matriz[0][i+1]
        Fp=(matriz[1][i]-matriz[1][i+1])/h
        print (Fp)
    return Fp

def atras(matriz):
    for i in range(len(matriz)):
        h=matriz[0][i]-matriz[0][i-1]
        Fp=(matriz[1][i]-matriz[1][i-1])/h
        print (Fp)
    return Fp

if __name__ == '__main__': 
    matriz = [[.5, .6,.7], [.4794, .5646, .6442]]
    adelante(matriz)
    atras(matriz)

