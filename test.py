# -----------------clase 1

# def mensaje(msg:str,name:str)->str:
#     return(name+msg)

# def msg_edad(name:str,age:int):
#     print("adios ",name," tienes ",age," años")
    
# def edad(b_year:int,a_year:int):
#     return a_year-b_year


# if __name__=="__main__":
#     name="Ruben"
#     msg="adios "
#     age=19
from turtle import reset

#     print(mensaje(name, msg))
#     msg_edad(name, age)
#     print("adios ",name,"Tienes ",edad(b_year,a_year)," años")
#     print("adios mundo")
    
# clase 2 ----------fstrings

# def msg_edad(name:str,b_year:int,a_year)->str:    
#     return f"Hola {name} tienes {a_year-b_year} años"

# if __name__=="__main__":
#     b_year=2002
#     a_year=2022
#     name="Ruben"
#     res=msg_edad(name, b_year, a_year)
#     #print(res)    
   
#print(f"{'hola':^60}")

#----------------------------Report---------------------

# encabezad=["Nombre", "Est Dat", "Prog Func", "Ingles"]
# alumnos=["Hugo", "Paco", "Luis", "Lupita"]

# m_estadistica=[9,7,9,8]
# m_programacion=[10,8,7,9]
# m_ingles=[6,9,7,10]

# print(f"{encabezad[0]:^10}{encabezad[1]:^10}{encabezad[2]:^10}{encabezad[3]:^10}")
# for i in range(len(alumnos)):
#     print(f"{alumnos[i]:^10}{m_estadistica[i]:^10}{m_programacion[i]:|^10}{m_ingles[i]:^10}")

#listas
lista=[]
lista1=[10,20,30]
for i in range(1, 11):
    lista.append(i) #.append agrega todo a final de la lista
    
lista.extend(lista1) #de esta manera podemos agregar al final todo lo que querramos
del lista[2] #funcion del elimina el elemento de la posicion indicada
print(lista)


# print(lista)
# print(lista[-5:-7]) #lista[inicio : final] imprimirá en el rango 
# print(lista[-5:-7]) #imprimirá tomando de derecha a izquierda

# #copiar valores de una lista a otra

# lista1=lista[:] #al usar slices podemos cambiar la direccion de memoria de una variable a otra
# print(f"Direccion {id(lista)} lista: {lista}")
# print(f"Direccion {id(lista1)} lista: {lista1}")