import os

def ingreso_documentos():
    lista = []
    os.system('cls' if os.name == 'nt' else 'clear')
    rta = input("Desea ingresar un documento? (S/N) ").upper()
    while (rta == "S"):
        os.system('cls' if os.name == 'nt' else 'clear')
        doc = input("Ingrese un número de documento (sin puntos): ")
        while (not doc.isdigit()):
            input("Documento invalido! Debe ingresar solo digitos. Presione enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            doc = input("Ingrese un número de documento (sin puntos): ")
        lista.append(doc)
        rta = input("Desea ingresar algún otro documento? (S/N) ").upper()
    return lista

def conjuntos_digitos_unicos(lista):
    return [set(dni) for dni in lista]

def calculos_conjuntos(lista_conjunto):
    for i in range(len(lista_conjunto) - 1):
        print(f"Conjuntos {lista_conjunto[i]} y {lista_conjunto[i+1]}")
        print(f"{lista_conjunto[i]} ⋃ {lista_conjunto[i+1]} = {lista_conjunto[i].union(lista_conjunto[i+1])}")
        print(f"{lista_conjunto[i]} ⋂ {lista_conjunto[i+1]} = {lista_conjunto[i].intersection(lista_conjunto[i+1])}")
        print(f"{lista_conjunto[i]} - {lista_conjunto[i+1]} = {lista_conjunto[i].difference(lista_conjunto[i+1])}")
        print(f"{lista_conjunto[i+1]} - {lista_conjunto[i]} = {lista_conjunto[i+1].difference(lista_conjunto[i])}")
        print(f"{lista_conjunto[i]} ∆ {lista_conjunto[i+1]} = {lista_conjunto[i].symmetric_difference(lista_conjunto[i+1])}")
        print("------------------------------------------------------------------")
    input("Presione enter para continuar...")

def conteo(lista):
    for dni in lista:
        dic = {}
        for digito in dni:
            if digito in dic:
                dic[digito] += 1
            else:
                dic[digito] = 1
        print(f"Conteo de frecuencia en el DNI {dni}:")
        for digito, cantidad in dic.items():
            print(f"{digito}: {cantidad} veces")
    input("Presione enter para continuar...")

def suma_digitos(lista):
    for dni in lista:
        suma = 0
        for digito in dni:
            suma += int(digito)
        print(f"La suma de los digitos del DNI {dni} es de: {suma}")
    input("Presione enter para continuar...")

def main():
    lista = []
    lista_conjunto = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("------------------------------------------")
        print("TP INTEGRADOR MATEMÁTICA")
        print("------------------------------------------")
        print("1. Ingresar")
        print("2. Calculo de conjuntos")
        print("3. Conteo de frecuencia")
        print("4. Suma de digitos")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if (opcion == "1"):
            lista = ingreso_documentos()
            lista_conjunto = conjuntos_digitos_unicos(lista)
        elif (opcion == "2"):
            if (len(lista_conjunto) > 1):
                calculos_conjuntos(lista_conjunto)
            else:
                print("Debe ingresar al menos dos DNI's")
        elif (opcion == "3"):
            if (len(lista) != 0):
                conteo(lista)
            else:
                print("Debe ingresar primero algún documento")
        elif (opcion == "4"):
            if (len(lista) != 0):
                suma_digitos(lista)
            else:
                print("Debe ingresar primero algún documento")
        elif (opcion == "0"):
            print("Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
