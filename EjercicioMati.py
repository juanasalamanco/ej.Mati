import json

i = 1
presupuestos = []

while i != 3:
    seleccion = int(input("Seleccione: 1.Calcular presupuestos 2.Ver presupuestos 3.Salir "))
    if seleccion == 1:
        nombre = input("ingresa el colegio: ")
        viajeros = input("ingresa la cantidad de viajeros:")
        acompañantes = int(viajeros) // 30
        precio = 50000 * (int(viajeros) + acompañantes)
        print("$" + str(precio))
        hola = ('nombre= ' + nombre, 'precio= $' + str(precio))
        presupuestos.append(hola)

    elif seleccion == 2: 
        print(presupuestos)
        
    else:
        i = 3

jsonString = json.dumps(presupuestos)
jsonFile = open("datos.json" , "w")
jsonFile.write(jsonString)
jsonFile.close()

