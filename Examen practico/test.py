## Mostrar las parejas a,b de números amigos menores a 3000,
# una pareja de números a y b son amigos, si son números diferentes y
# si la suma de divisores de 'A' es menor a 'A' y su suma da 'B' y viceversa

if __name__ == "__main__":
    i=0
    for o in range(1,3000):
        for j in range(1,3000):
            if i != j:
                suma_divisores_i = 0
                suma_divisores_j = 0
                for k in range(1,i):
                    if i % k == 0:
                        suma_divisores_i += k
                for k in range(1,j):
                    if j % k == 0:
                        suma_divisores_j += k
                if suma_divisores_i == j and suma_divisores_j == i:
                    print(i,j)