from random import randint
              
def binaria(n, ask):
    tam=len(n)
    it=0
    while True:
        tam=int(tam/2)
        if ask==n[tam]:
            print("numero encontrado en la posicion ",tam)
            print(f"En {it} ciclos")
            break
        else:
            if n[tam]>ask:
                tam=int(((tam/2)*3)+1)
                it=it+1
            else:
                tam=int((tam/2)+1)
                it=it+1
        if it == 25:
            print("numero no encontrado")
            break
                

if __name__=='__main__':
    n = []
    for i in range(50):
        n.append(randint(1, 20))
    n.sort()
    binaria(n, 5)
    
    



