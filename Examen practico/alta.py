
def alta(id, name, price, lot):
    ok=0
    while ok==0:
        try: #validación de ID
            id_new = int(input("Ingrese el id del producto: "))
        except ValueError:
            print("Ingrese un número!")
            ok=+1
            break
        if id_new in id:
            print("El id ya existe!")
            ok=+1            
            break

        #ingreso de nombre
        name_new = input("Ingrese el nombre del producto: ")
        

        #validación de precio
        try:
            price_new = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("Ingrese un número!")
            ok=+1
            break
        if price_new < 0:
            print("Ingrese un número positivo!")
            ok=+1
            break

        #validación de lote
        try:
            lot_new = int(input("Ingrese la cantidad del producto: "))
        except ValueError:
            print("Ingrese un número!")
            ok=+1   
            break
        if lot_new <= 0:
            print("Ingrese un número positivo!")
            ok=+1
            break
            
        if ok==0:
            id.append(id_new)
            price.append(price_new)
            name.append(name_new)
            lot.append(lot_new)
            print("Producto agregado!")
            break
        
    return id, name, price, lot