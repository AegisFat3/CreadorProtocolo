#Romero Trujillo Brian Adán 4IM10

#Creador de protocolos

pasos=[]


print("Bienvenido! \n")
print("Aqui podrás crear tu protocolo")

def menu():
     print("")
     print("******* Menú ******* \n")
     print("Elije la acción que quieras realizar: \n")
     print("1. Agregar un paso en una posición")
     print("2. Agregar un paso")  
     print("3. Borrar un paso")
     print("4. Modificar un paso")
     print("5. Desplegar protocolo")
     print("6. Salir \n")
     print("Considere que al paso 1 le pertenece la posición 0 \n")



long = int(input("¿Cuántos pasos inicalmente deseas agregar? (Considere que al paso 1 le pertenece la posición 0): "))
i=0

while i < long:
    step = input("Ingrese la descripción del paso "+str(i+1)+" : ")

    pasos.append(step)

    i = i + 1


while True:
    menu()
    opc=int(input("Escoge una opción: "))
    
    if opc == 1:
        i=0
        loc=int(input("Escribe la posición en la que desea añadir el paso: "))
        no=input("Describe el nuevo paso: ")
        print("")
        pasos.insert(loc,no)
        for m in range (0,(len(pasos))):
            print("Paso " +str(i+1)+" : "+pasos[i])
            i = i + 1
            print("")
            
    elif opc == 2:
         i=0
         add=input("Describe el nuevo paso: ")
         pasos.append(add)
         print("")
         for p in range (0,(len(pasos))):
             print("Paso " +str(i+1)+" : "+pasos[i])
             i = i + 1
             print("")

    elif opc == 3:
        i=0
        dele = int(input("Escribe la posición del paso que deseas eliminar: "))
        print("")
        pasos.pop(dele)
        for n in range (0,(len(pasos))):
            print("Paso " +str(i+1)+" : "+pasos[i])
            i = i + 1
            print("")
                     

    elif opc == 4:
         i=0
         mod = int(input("Escribe la posición del paso que deseas modificar: "))
         pasos.pop(mod)
         new = input("Escribe el paso modificado: ")
         print("")
         pasos.insert(mod,new)
         for y in range (0,(len(pasos))):
            print("Paso " +str(i+1)+" : "+pasos[i])
            i = i + 1
            print("")

    elif opc == 5:
         i=0
         print("Este es tu protocolo:")
         print("")
         for j in range (0,(len(pasos))):
                print("Paso " +str(i+1)+" : "+pasos[i])
                i = i + 1
                print("")
            
    elif opc == 6:
          print("")
          print("Hasta pronto!")

          break
    else:
          print("")
          print("Opción inválida, intentalo de nuevo. \n")
