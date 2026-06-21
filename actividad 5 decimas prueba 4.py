reservas = []

# VALIDACIONES
def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_noches(noches):
    return noches > 0

def validar_valor_noche(valor_noche):
    return valor_noche > 0

# MENU
def mostrar_menu():
    print("\n========= MENU PRINCIPAL ========")
    print("1.- Registrar reserva")
    print("2.- Buscar reserva")
    print("3.- Actualizar reserva")
    print("4.- Salir")
    print("===================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            if 1 <= opcion <= 4:
                return opcion
            print("Debe ingresar una opcion entre 1 y 4.")
        except ValueError:
            print("Ingrese un numero valido.")

# BUSCAR
def buscar_reserva(lista, codigo):
    for i, reserva in enumerate(lista):
        if reserva["codigo"] == codigo:
            return i
    return -1

# REGISTRAR
def registrar_reserva(lista):
    codigo = input("Codigo de reserva: ")
    nombre = input("Nombre del huesped: ")

    try:
        noches = int(input("Cantidad de noches: "))
        valor_noche = float(input("Valor por noche ($): "))
    except ValueError:
        print("Error: noches o valor invalido") 
        return 

    if not validar_codigo(codigo):
        print("Error: Codigo Invalido")
        return

    if not validar_nombre(nombre):
        print("Error: Nombre Invalido")  
        return
    
    if not validar_noches(noches):
        print("Error: Las noches deben ser mayores a cero")
        return
    
    if not validar_valor_noche(valor_noche):
        print("Error: El valor por noche debe ser mayor a cero")
        return
            
    # Comprobar que el codigo no exista previamente en la lista
    if buscar_reserva(lista, codigo) != -1:
        print("Error: El codigo de reserva ya se encuentra registrado")
        return

    # Calculos automatizados de negocio
    total = noches * valor_noche

    if total < 200000:
        categoria = "Economica"
    elif total <= 500000:
        categoria = "Estandar"
    else:
        categoria = "Premium"

    reserva = {
        "codigo": codigo,
        "nombre": nombre,
        "noches": noches,
        "valor_noche": valor_noche,
        "total": total,
        "categoria": categoria
    }
    
    lista.append(reserva)
    print("Reserva registrada correctamente")

# ACTUALIZAR RESERVA
def actualizar_reserva(lista):
    codigo = input("Ingrese codigo de reserva a modificar: ")
    posicion = buscar_reserva(lista, codigo)

    if posicion == -1:
        print("Error: El codigo de reserva ingresado no existe")
    else:
        print(f"\nModificando los datos de la reserva actual.")
        nombre = input("Nuevo nombre del huesped: ")
        
        try:
            noches = int(input("Nueva cantidad de noches: "))
            valor_noche = float(input("Nuevo valor por noche ($): "))
        except ValueError:
            print("Error: noches o valor invalido")
            return

        if not validar_nombre(nombre) or not validar_noches(noches) or not validar_valor_noche(valor_noche):
            print("Error: Uno o más datos ingresados son invalidos")
            return

        # Calcular los nuevos valores automaticos
        total = noches * valor_noche

        if total < 200000:
            categoria = "Economica"
        elif total <= 500000:
            categoria = "Estandar"
        else:
            categoria = "Premium"

        # Actualizar datos dentro de la lista de diccionarios
        lista[posicion]["nombre"] = nombre
        lista[posicion]["noches"] = noches
        lista[posicion]["valor_noche"] = valor_noche
        lista[posicion]["total"] = total
        lista[posicion]["categoria"] = categoria

        print("Reserva actualizada correctamente")


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
        print("Programa Finalizado")
        break