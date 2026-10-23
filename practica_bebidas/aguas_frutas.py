# Programa que permite vender bebidas
# solicita una opcion para elegir la bebida 
# Pegunta cantidad de bebida 
# Muestra cantidad a pagar 

print("Aguas de litro UAGRO")
print("Elije una opcion del menu")
print("1. Agua de mango - $40")
print("2. Agua de Jamaica - $45")
print("3. Agua de Horchata - $35")

opcion = int(input("Elige una opcion del menú:"))
cantidad = int(input("¿Cuantos litros quieres?:"))
if opcion == 1:
    cantidadM = cantidad*40
    print("Agua de mango")
    print("Precio a pagar: $",cantidadM)
elif opcion == 2:
    cantidadJ = cantidad*45
    print("Agua de Jamaica")
    print("Precio a pagar: $",cantidadJ)
elif opcion == 3:
    cantidadH = cantidad*35
    print("Agua de Horchata")
    print("precio a pagar: $",cantidadH)
    print("que onda aliiii")
