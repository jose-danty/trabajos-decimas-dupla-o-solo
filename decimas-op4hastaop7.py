def eliminar_reserva(lista):
    codigo = input("ingrese codigo de reserva: ")
    posicion = buscar_reserva(lista, codigo)

    if posicion == -1:
        print("error: ingrese un codigo de reserva existente")
    else:
        lista.pop(posicion)
        print("reserva eliminada correctamente")
def mostrar_reservas(lista):
    if len(lista) == 0:
        print("no hay reservas registradas")
    else:
        print("\nlistado de reservas: ")
        for reserva in lista:
            print(reserva)
def mostrar_estadisticas(lista):
    if len(lista) == 0:
        print("no hay reservas registradas")
        return
    cantidad = len(lista)
    ingresos_totales = 0
    mayor = lista()

    for reserva in lista:
        ingresos_totales += reserva["total"]
        if reserva["total"] > mayor["total"]:
            mayor = reserva

    promedio = ingresos_totales / cantidad

    print("estadisticas: ").upper()
    print(f"Cantidad total de reservas: {cantidad}")
    print(f"Ingresos totales: {ingresos_totales}")
    print(f"Reserva de mayor valor: {mayor}")
    print(f"Promedio de ingresos por reserva: {promedio}")
# FLUJO PRINCIPAL
while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        registrar_reserva(reservas)

    elif opcion == 2: 
        codigo = input("Ingrese codigo a buscar: ")
        posicion = buscar_reserva(reservas, codigo)

        if posicion == -1:
            print("Reserva no Encontrada")
        else:
            print(f"Reserva Encontrada en la posicion {posicion}:")
            print(reservas[posicion])

    elif opcion == 3:
        actualizar_reserva(reservas)

    elif opcion == 4:
        eliminar_reserva(reservas)

    if opcion == 5:
        mostrar_reservas (reservas)

    elif opcion == 6:
        mostrar_estadisticas(reservas)
    if opcion == 7:
        print("finalizando programa").upper()
        exit(opcion == 7)
        break