fmt=3
def tablas(n:int, t:int):
    for i in range(t):
        multi(n, i+1)
        print(f"{16:c}")

def multi(number:int, table:int):
    for i in range(number):
        print(f"{table:^{fmt}}{'x':^{fmt}}{i+1:^{fmt}}{'=':^{fmt}}{table*(i+1):^{fmt}}")
    
if __name__=="__main__":

    if 10>15: #si 10 es mayor que 15 entonces...
        print("Hola") # No se ejecuta
    elif 10<15: #si 10 es menor que 15 entonces...
        print("Mundo") # Se ejecuta
    else:  #si no es ninguno de esos, entonces...
        print("Adios") # Se ejecuta  

