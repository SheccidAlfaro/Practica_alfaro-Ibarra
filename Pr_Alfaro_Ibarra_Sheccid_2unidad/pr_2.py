print("")
print("Alfaro Ibarra Sheccid 3w")
print("5 numeros triunfadores de la loteria")
#Se crea la lista vacia para poder llenarla
lista=[]
#Utiliza for para un  ciclo de cinco vueltas(repetir hasta que se pongan los cinco valores)
for x in range  (5):
    numdlo= int(input("Ingrese los numeros de loteria triunfadores:"))
    #Utilizar append para llenar la lista
    lista.append(numdlo)
#Utilizar sort para ordenar de menor a mayor
lista.sort()
print("De menor a mayor")
#se muestra en pantalla
print(lista)