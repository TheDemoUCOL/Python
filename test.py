# clase 1

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
    


def msg_edad(name:str,b_year:int,a_year)->str:    
    return f"Hola {name} tienes {a_year-b_year} años"

if __name__=="__main__":
    b_year=2002
    a_year=2022
    name="Ruben"
    res=msg_edad(name, b_year, a_year)
    #print(res)    
    

print(f"{'hola':^60}")