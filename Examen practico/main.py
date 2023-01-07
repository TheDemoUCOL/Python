id=[1,23,2,1.3,85,4]
name=[]
price=[]
lot=[]

from curses.ascii import isalpha
import time
import alta as a
import modi as m
import baja as b
import consulta as c
import os



def next():
  if input("Desea continuar? (s/n)").lower() == "s":
    return False
  else:
    return True

if __name__ == '__main__':
  print("""
      
 /$$$$$$                                           /$$                                  
|_  $$_/                                          | $$                                  
  | $$   /$$$$$$$  /$$    /$$ /$$$$$$  /$$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$  /$$   /$$
  | $$  | $$__  $$|  $$  /$$//$$__  $$| $$__  $$|_  $$_/   |____  $$ /$$__  $$| $$  | $$
  | $$  | $$  \ $$ \  $$/$$/| $$$$$$$$| $$  \ $$  | $$      /$$$$$$$| $$  \__/| $$  | $$
  | $$  | $$  | $$  \  $$$/ | $$_____/| $$  | $$  | $$ /$$ /$$__  $$| $$      | $$  | $$
 /$$$$$$| $$  | $$   \  $/  |  $$$$$$$| $$  | $$  |  $$$$/|  $$$$$$$| $$      |  $$$$$$$
|______/|__/  |__/    \_/    \_______/|__/  |__/   \___/   \_______/|__/       \____  $$
                                                                               /$$  | $$
                                                                              |  $$$$$$/
                                                                               \______/       
      """)

  
  while True:
    print("Seleccione una opción:")
    print("""
        1) Dar de alta un artículo.
        2) Modificar un artículo
        3) Eliminar un artículo
        4) Consultar las existencias
        5) Inventario total.""")

    opcion = input("Opción: ") 
    if opcion.isnumeric():
      opcion = int(opcion)
      if opcion == 1:
        a.alta(id, name, price, lot)
        if next():
          break
      elif opcion == 2:
        m.modi(id, name, price, lot)
        if next():
          break
      elif opcion == 3:
        b.baja(id, name, price, lot)
        if next():
          break
      elif opcion == 4:
        c.one(id, name, price, lot)
        if next():
          break
      elif opcion == 5:
        c.all(id, name, price, lot)
        if next():
          break
      else:
        os.system("cls")
        print("Ingrese una opción valida!")
        time.sleep(3)
    else:
        os.system("cls")
        print("Ingrese una opción valida!")
        time.sleep(3)

    os.system("cls")
    